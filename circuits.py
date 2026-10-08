from quantum_state import QuantumWire

def bell_state():
    circuit = QuantumWire(2) #init a 2 quibit circuit
    circuit.h_gate(1) #apply a h-gate to quibit 1
    circuit.cnot_gate(1, 2) #apply a cnot gate, c=1, t=2
    result = circuit.measure() #measure each quibits state
    print(result)

bell_state()

