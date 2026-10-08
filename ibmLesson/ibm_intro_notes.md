Modules go to :
    qiskit-visualization: allows results to be displayed in a readable way
    qiskit-ibm-runtime: use real ibm hardware for program
    qiakit-aer: a quantum simulator

hammond gate: takes a quibit in a classical state (0 or 1) and puts it into a superposition, this tells the quibit to be treated as an equally superpositioned 0 or 1

CNot: flips the second quibit if the first is in the 1 state

Hadamard gate + Cnot = Bell State (if one is "1" the other related quibit is also "1")

Entanglement: Quibits are so strongly correlated, one cant be described independently of the other, in practice if you where to measure one you would also know the value of the other as its correlated to the first

a quantum circuit is essentially a matrix of quibits all of which can be manipulated and random until measured which at this point take a set value
