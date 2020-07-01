"""Superdense coding in cirq"""

# Imports
import cirq

# Helper function for viz
def bitstring(bits):
    return ''.join('0' if e else '1' for e in bits)

# Create two quantum and classical registers
qreg = [cirq.LineQubit(x) for x in range(2)]
circ = cirq.Circuit()

# Dictionary of operations for each message
message = {
    "00": [], 
    "01": [cirq.X(qreg[0])],
    "10": [cirq.Z(qreg[0])],
    "11": [cirq.X(qreg[0]), cirq.Z(qreg[0])]
    }

# Alice creates a bell pair
circ.append(cirq.H(qreg[0]))
circ.append(cirq.CNOT(qreg[0], qreg[1]))

# Alice picks a message to send
m = "01"
print("Alice's sent message =", m)

# Alice encodes her message with the appropriate quantum operations
circ.append(message[m])

# Bob measures in the Bell basis
circ.append(cirq.CNOT(qreg[0], qreg[1]))
circ.append(cirq.H(qreg[0]))
circ.append([cirq.measure(qreg[0]), cirq.measure(qreg[1])])

# Print the circuit
print("\nCircuit:")
print(circ)

# Run the quantum circuit on a simulator server
sim = cirq.Simulator()
res = sim.run(circ, repetitions=1)

# Print out Bob's received message: the outcome of circuit
print("\nBob's received message =",
    bitstring(res.measurements.values()))