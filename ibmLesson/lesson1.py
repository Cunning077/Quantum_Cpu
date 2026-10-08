from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

from qiskit_ibm_runtime import SamplerV2 as Sampler, QiskitRuntimeService

bell = QuantumCircuit(2)
bell.h(0) #creates a hammond gate on q[0]
bell.cx(0,1) #creates a cnot where q[o] is control and q[1] is output

bell.measure_all()
bell.draw("mpl")

def runCircuitGetCounts(circuit, backend, shots=1000):
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_circuit = pm.run(circuit)
    sampler = Sampler(mode=backend)
    job = sampler.run([isa_circuit], shots=shots)
    result = job.result()
    return result[0].data.meas.get_counts()
