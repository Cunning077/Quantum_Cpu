from quantum_state import QuantumWire
import memory_d as Mem
import math

def bell_state():
    circuit = QuantumWire(2) #init a 2 quibit circuit
    circuit.h_gate(1) #apply a h-gate to quibit 1
    circuit.cnot_gate(1, 2) #apply a cnot gate, c=1, t=2
    result = circuit.measure() #measure each quibits state
    print(result)

def GHZ_gate():
    circuit = QuantumWire(3)
    circuit.h_gate(1)
    circuit.cnot_gate(1, 2)
    circuit.cnot_gate(1, 3)
    result = circuit.measure()
    print(result)

def grovers_algorithm(num_q, target):
    circuit = QuantumWire(num_q)
    for i in range(1, num_q + 1):
        circuit.h_gate(i)

    iterations = int((math.pi / 4) * math.sqrt(2 ** num_q))
    for i in range(int(iterations)):
        print(f"{i}/{iterations}")
        circuit.oracle(target)
        circuit.diffusion()
    
    result = circuit.measure()
    return result


