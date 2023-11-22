import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)
qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.x(3)
circuit.barrier()

circuit.barrier()
circuit.cx(2,3)
circuit.barrier()
circuit.h(2)
circuit.h(1)
circuit.h(0)
circuit.barrier()
circuit.measure(2, 2)
circuit.measure(0, 0)
circuit.measure(1, 1)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()


simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(3, 3)

circuit.barrier(0,1,2)
circuit.cx(0,2)
circuit.barrier(0,1,2)

circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(3, 3)

circuit.barrier(0,1,2)
circuit.id(0)   
circuit.id(1)
circuit.id(2)
circuit.barrier(0,1,2)

circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()



simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.x(3)
circuit.h(3)
circuit.barrier()


circuit.h(1)
circuit.h(0)
circuit.h(2)
circuit.barrier()
circuit.measure(0, 0)
circuit.measure(1, 1)
circuit.measure(2, 2)
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)

result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()