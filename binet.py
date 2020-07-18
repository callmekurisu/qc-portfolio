import math
import sys

# pass fn as argument to script for fibonacci value
input = int(sys.argv[1])
phi = 1.618
psi = 1-phi
fn = math.ceil((phi**input-psi**input) / (phi - psi))
print(fn)