from openfermion.ops import FermionOperator
my_term = FermionOperator(((3, 1), (1, 0)))
print (my_term)
my_term = FermionOperator('3^ 1')
print (my_term)
