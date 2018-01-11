from openfermion.ops import FermionOperator
my_operator = FermionOperator('4^ 1^ 3 9', 1. + 2.j)
print (my_operator)
print (my_operator.terms)
