import numpy as np
from phonopy.harmonic.displacement import (get_least_displacements,
                                           directions_axis, get_displacement,
                                           is_minus_displacement)
from phonopy.structure.cells import get_smallest_vectors


def direction_to_displacement(dataset,
                              distance,
                              supercell,
                              cutoff_distance=None):
    lattice = supercell.get_cell().T
    new_dataset = {}
    new_dataset['natom'] = supercell.get_number_of_atoms()
    if cutoff_distance is not None:
        new_dataset['cutoff_distance'] = cutoff_distance
    new_first_atoms = []
    for first_atoms in dataset:
        atom1 = first_atoms['number']
        direction1 = first_atoms['direction']
        disp_cart1 = np.dot(direction1, lattice.T)
        disp_cart1 *= distance / np.linalg.norm(disp_cart1)
        new_second_atoms = []
        for second_atom in first_atoms['second_atoms']:
            atom2 = second_atom['number']
            pair_distance = second_atom['distance']
            included = (cutoff_distance is None or
                        pair_distance < cutoff_distance)
            for direction2 in second_atom['directions']:
                disp_cart2 = np.dot(direction2, lattice.T)
                disp_cart2 *= distance / np.linalg.norm(disp_cart2)
                if cutoff_distance is None:
                    new_second_atoms.append({'number': atom2,
                                             'direction': direction2,
                                             'displacement': disp_cart2,
                                             'pair_distance': pair_distance})
                else:
                    new_second_atoms.append({'number': atom2,
                                             'direction': direction2,
                                             'displacement': disp_cart2,
                                             'pair_distance': pair_distance,
                                             'included': included})
        new_first_atoms.append({'number': atom1,
                                'direction': direction1,
                                'displacement': disp_cart1,
                                'second_atoms': new_second_atoms})
    new_dataset['first_atoms'] = new_first_atoms

    return new_dataset


def get_third_order_displacements(cell,
                                  symmetry,
                                  is_plusminus='auto',
                                  is_diagonal=False):
    """Create dispalcement dataset

    Note
    ----
    Atoms 1, 2, and 3 are defined as follows:

    Atom 1: The first displaced atom. Third order force constant
            between Atoms 1, 2, and 3 is calculated.
    Atom 2: The second displaced atom. Second order force constant
            between Atoms 2 and 3 is calculated.
    Atom 3: Force is mesuared on this atom.

    Parameters
    ----------
    cell : PhonopyAtoms
        Supercell
    symmetry : Symmetry
        Symmetry of supercell
    is_plusminus : str or bool, optional
        Type of displacements, plus only (False), always plus and minus (True),
        and plus and minus depending on site symmetry ('auto').
    is_diagonal : bool, optional
        Whether allow diagonal displacements of Atom 2 or not

    Returns
    -------
    dict
        Data structure is like:
        {'natom': 64,
         'cutoff_distance': 4.000000,
         'first_atoms':
          [{'number': atom1,
            'displacement': [0.03, 0., 0.],
            'second_atoms': [ {'number': atom2,
                               'displacement': [0., -0.03, 0.],
                               'distance': 2.353},
                              {'number': ... }, ... ] },
           {'number': atom1, ... } ]}

    """

    positions = cell.get_scaled_positions()
    lattice = cell.get_cell().T

    # Least displacements of first atoms (Atom 1) are searched by
    # using respective site symmetries of the original crystal.
    # 'is_diagonal=False' below is made intentionally to expect
    # better accuracy.
    disps_first = get_least_displacements(symmetry,
                                          is_plusminus=is_plusminus,
                                          is_diagonal=False)

    symprec = symmetry.get_symmetry_tolerance()

    dds = []
    for disp in disps_first:
        atom1 = disp[0]
        disp1 = disp[1:4]
        site_sym = symmetry.get_site_symmetry(atom1)

        dds_atom1 = {'number': atom1,
                     'direction': disp1,
                     'second_atoms': []}

        # Reduced site symmetry at the first atom with respect to
        # the displacement of the first atoms.
        reduced_site_sym = get_reduced_site_symmetry(site_sym, disp1, symprec)
        # Searching orbits (second atoms) with respect to
        # the first atom and its reduced site symmetry.
        second_atoms = get_least_orbits(atom1,
                                        cell,
                                        reduced_site_sym,
                                        symprec)

        for atom2 in second_atoms:
            dds_atom2 = get_next_displacements(atom1,
                                               atom2,
                                               reduced_site_sym,
                                               lattice,
                                               positions,
                                               symprec,
                                               is_diagonal)

            min_vec = get_equivalent_smallest_vectors(atom1,
                                                      atom2,
                                                      cell,
                                                      symprec)[0]
            min_distance = np.linalg.norm(np.dot(lattice, min_vec))
            dds_atom2['distance'] = min_distance
            dds_atom1['second_atoms'].append(dds_atom2)
        dds.append(dds_atom1)

    return dds


def get_next_displacements(atom1,
                           atom2,
                           reduced_site_sym,
                           lattice,
                           positions,
                           symprec,
                           is_diagonal):
    # Bond symmetry between first and second atoms.
    reduced_bond_sym = get_bond_symmetry(
        reduced_site_sym,
        lattice,
        positions,
        atom1,
        atom2,
        symprec)

    # Since displacement of first atom breaks translation
    # symmetry, the crystal symmetry is reduced to point
    # symmetry and it is equivalent to the site symmetry
    # on the first atom. Therefore site symmetry on the
    # second atom with the displacement is equivalent to
    # this bond symmetry.
    if is_diagonal:
        disps_second = get_displacement(reduced_bond_sym)
    else:
        disps_second = get_displacement(reduced_bond_sym, directions_axis)
    dds_atom2 = {'number': atom2, 'directions': []}
    for disp2 in disps_second:
        dds_atom2['directions'].append(disp2)
        if is_minus_displacement(disp2, reduced_bond_sym):
            dds_atom2['directions'].append(-disp2)

    return dds_atom2


def get_reduced_site_symmetry(site_sym, direction, symprec=1e-5):
    reduced_site_sym = []
    for rot in site_sym:
        if (abs(direction - np.dot(direction, rot.T)) < symprec).all():
            reduced_site_sym.append(rot)
    return np.array(reduced_site_sym, dtype='intc')


def get_bond_symmetry(site_symmetry,
                      lattice,
                      positions,
                      atom_center,
                      atom_disp,
                      symprec=1e-5):
    """
    Bond symmetry is the symmetry operations that keep the symmetry
    of the cell containing two fixed atoms.
    """
    bond_sym = []
    pos = positions
    for rot in site_symmetry:
        rot_pos = (np.dot(pos[atom_disp] - pos[atom_center], rot.T) +
                   pos[atom_center])
        diff = pos[atom_disp] - rot_pos
        diff -= np.rint(diff)
        dist = np.linalg.norm(np.dot(lattice, diff))
        if dist < symprec:
            bond_sym.append(rot)

    return np.array(bond_sym)


def get_least_orbits(atom_index, cell, site_symmetry, symprec=1e-5):
    """Find least orbits for a centering atom"""
    orbits = _get_orbits(atom_index, cell, site_symmetry, symprec)
    mapping = np.arange(cell.get_number_of_atoms())

    for i, orb in enumerate(orbits):
        for num in np.unique(orb):
            if mapping[num] > mapping[i]:
                mapping[num] = mapping[i]

    return np.unique(mapping)


def _get_orbits(atom_index, cell, site_symmetry, symprec=1e-5):
    lattice = cell.get_cell().T
    positions = cell.get_scaled_positions()
    center = positions[atom_index]

    # orbits[num_atoms, num_site_sym]
    orbits = []
    for pos in positions:
        mapping = []

        for rot in site_symmetry:
            rot_pos = np.dot(pos - center, rot.T) + center

            for i, pos in enumerate(positions):
                diff = pos - rot_pos
                diff -= np.rint(diff)
                dist = np.linalg.norm(np.dot(lattice, diff))
                if dist < symprec:
                    mapping.append(i)
                    break

        if len(mapping) < len(site_symmetry):
            print("Site symmetry is broken.")
            raise ValueError
        else:
            orbits.append(mapping)

    return np.array(orbits)


def get_equivalent_smallest_vectors(atom_number_supercell,
                                    atom_number_primitive,
                                    supercell,
                                    symprec):
    s_pos = supercell.get_scaled_positions()
    svecs, multi = get_smallest_vectors(supercell.get_cell(),
                                        [s_pos[atom_number_supercell]],
                                        [s_pos[atom_number_primitive]],
                                        symprec=symprec)
    return svecs[0, 0]
