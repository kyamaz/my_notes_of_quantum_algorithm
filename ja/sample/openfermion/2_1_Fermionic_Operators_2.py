from openfermion.ops import FermionOperator
good_way_to_initialize = FermionOperator('3^ 1', -1.7)
print (good_way_to_initialize)
bad_way_to_initialize = -1.7 * FermionOperator('3^ 1')
print (bad_way_to_initialize)
identity = FermionOperator('')
print (identity)
zero_operator = FermionOperator()
print (zero_operator)
