from openfermion.ops import QubitOperator
my_first_qubit_operator = QubitOperator('X1 Y2 Z3')
print (my_first_qubit_operator)
print (my_first_qubit_operator.terms)
operator_2 = QubitOperator('X3 Z4', 3.17)
operator_2 -= 77.  * my_first_qubit_operator
print (operator_2)
