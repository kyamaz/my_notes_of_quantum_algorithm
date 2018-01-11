from openfermion.ops import FermionOperator, hermitian_conjugated
from openfermion.transforms import jordan_wigner, bravyi_kitaev
from openfermion.utils import eigenspectrum

# Initialize an operator.
fermion_operator = FermionOperator('2^ 0', 3.17)
fermion_operator += hermitian_conjugated(fermion_operator)
print (fermion_operator)

# Transform to qubits under the Jordan-Wigner transformation and print its spectrum.
jw_operator = jordan_wigner(fermion_operator)
jw_spectrum = eigenspectrum(jw_operator)
print (jw_operator)
print (jw_spectrum)

# Transform to qubits under the Bravyi-Kitaev transformation and print its spectrum.
bk_operator = bravyi_kitaev(fermion_operator)
bk_spectrum = eigenspectrum(bk_operator)
print (bk_operator)
print (bk_spectrum)
