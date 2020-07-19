import math
import sys

# pass fn as argument to script for fibonacci value
ui = int(input('Enter fn: '))
phi = 1.618
psi = 1-phi
fn = math.ceil((phi**ui-psi**ui) / (phi - psi))
print(fn)