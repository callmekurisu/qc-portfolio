import math
import sys

# pass fn as argument to script for fibonacci value
n = int(input('Enter fn: '))
phi = 1.618
psi = 1-phi
fn = math.ceil((phi**n-psi**n) / (phi - psi))
print(fn)