import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *
qvm = api.SyncConnection()
p = pq.Program()
p.inst(
  H(0),
  H(1),
  H(0),
  CNOT(1,0),
  H(0),
  H(0),
  H(1),
  X(0),
  X(1),
  H(0),
  CNOT(1,0),
  H(0),
  X(0),
  X(1),
  H(0),
  H(1),
  MEASURE(0, 0),
  MEASURE(1, 1))
result = qvm.run(p,[0,0],20)
print(result)
