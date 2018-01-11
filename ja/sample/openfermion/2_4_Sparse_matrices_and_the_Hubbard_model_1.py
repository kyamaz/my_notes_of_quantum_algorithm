from openfermion.hamiltonians import fermi_hubbard
from openfermion.transforms import get_sparse_operator, jordan_wigner
from openfermion.utils import get_ground_state

# Set model.
x_dimension = 2
y_dimension = 2
tunneling = 2.
coulomb = 1.
magnetic_field = 0.5
chemical_potential = 0.25
periodic = 1
spinless = 1

# Get fermion operator.
hubbard_model = fermi_hubbard(
  x_dimension, y_dimension, tunneling, coulomb, chemical_potential,
  magnetic_field, periodic, spinless)
print (hubbard_model)

# Get qubit operator under Jordan-Wigner.
jw_hamiltonian = jordan_wigner(hubbard_model)
jw_hamiltonian.compress()
print (jw_hamiltonian)

# Get scipy.sparse.csc representation.
sparse_operator = get_sparse_operator(hubbard_model)
print (sparse_operator)
print ('\nEnergy of the model is {} in units of T and J.'.format(
  get_ground_state(sparse_operator)[0]))
