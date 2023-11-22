#juan andres rodriguez

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.x(0)

circuit.barrier()
circuit.x(0)
circuit.cx(0, 1)
circuit.x(0)
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

#############################

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)


circuit.barrier(0,1)

circuit.x(0)
circuit.cx(0,1)
circuit.x(0)
circuit.barrier(0,1)

circuit.measure([0,1], [1,0])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

##########################
simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.x(0)
circuit.x(0)
circuit.barrier()
circuit.x(0)
circuit.barrier()
circuit.measure(0,1)
circuit.measure(1,0)


compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

###################
simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


circuit.barrier(0,1)

circuit.id(0)
circuit.id(1)

circuit.barrier(0,1)

circuit.measure([1,0], [0,1])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()
