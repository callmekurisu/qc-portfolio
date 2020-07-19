import math
import sys

n = int(input('Enter fn: '))
phi = 1.618
psi = 1-phi
fn = math.ceil((phi**n-psi**n) / (phi - psi))
print(fn)