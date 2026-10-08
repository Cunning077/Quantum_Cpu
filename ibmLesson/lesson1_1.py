from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.executor_sampler import Sampler
from dotenv import load_dotenv
import os

def runCircuitGetCounts(circuit, backend, shots=1000):
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_circuit = pm.run(circuit)
    sampler = Sampler(mode=backend)
    job = sampler.run([isa_circuit], shots=shots)
    result = job.result()
    return result[0].data.meas.get_counts()



# Load saved credentials
service = QiskitRuntimeService(instance="open-instance")

# Use the least busy backend, or uncomment the loading of a specific backend like "ibm_fez".
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)
# backend = service.backend("ibm_fez")

bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0,1)
bell.measure_all()
bell.draw("mpl")
counts = runCircuitGetCounts(bell, backend, shots=1000)
plot_histogram(counts)
