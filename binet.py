import math
import sys

# pass n as argument to script for fibonacci value
arg = int(sys.argv[1])
def binet_algo(n):
    phi = 1.618
    psi = 1-phi
    return math.ceil((phi**n-psi**n)/(phi-psi))
print(binet_algo(arg))