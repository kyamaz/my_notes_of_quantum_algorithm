from openfermion.hamiltonians import MolecularData

# Set molecule parameters.
basis = 'sto-3g'
multiplicity = 1
bond_length_interval = 0.1
n_points = 25
# Generate molecule at different bond lengths.
hf_energies = []
fci_energies = []
bond_lengths = []
for point in range(3, n_points + 1):
  bond_length = bond_length_interval * point
  bond_lengths += [bond_length]
  description = str(round(bond_length,2))
  print(description)
  geometry = [('H', (0., 0., 0.)), ('H', (0., 0., bond_length))]
  molecule = MolecularData(
      geometry, basis, multiplicity, description=description)
  # Load data.
  molecule.load()

  # Print out some results of calculation.
  print('\nAt bond length of {} Bohr, molecular hydrogen has:'.format(
        bond_length))
  print('Hartree-Fock energy of {} Hartree.'.format(molecule.hf_energy))
  print('MP2 energy of {} Hartree.'.format(molecule.mp2_energy))
  print('FCI energy of {} Hartree.'.format(molecule.fci_energy))
  print('Nuclear repulsion energy between protons is {} Hartree.'.format (
        molecule.nuclear_repulsion))
  for orbital in range(molecule.n_orbitals):
    print('Spatial orbital {} has energy of {} Hartree.'.format(
        orbital, molecule.orbital_energies[orbital]))
  hf_energies += [molecule.hf_energy]
  fci_energies += [molecule.fci_energy]
