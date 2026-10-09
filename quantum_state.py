import numpy as np
import memory_d as Mem

class QuantumState:
    def __init__(self, num_q):
        self.num_q = num_q
        self.num_states = 2 ** num_q

        self.state = np.zeros(self.num_states, dtype=complex)
        self.state[0] = 1 

    def __str__(self):
        return str(self.state)


class QuantumWire:
    def __init__(self, num_q):
        self.num_q = num_q
        self.state = QuantumState(num_q)

    def calc_prob(self):
        self.prob = np.abs(self.state.state) ** 2
        return self.prob

    def measure(self):
        prob = self.calc_prob() #saved as local to represent its current measured val
        results = np.random.choice(len(self.state.state), p=prob)
        self.state.state[:] = 0
        self.state.state[results] = 1
        print('numq', self.num_q)
        return format(results, f"0{self.num_q}b")

    def h_gate(self, qubit):
        if 1 <= qubit <= self.num_q:
            H = np.array([[1, 1],[1,-1]]) / np.sqrt(2)
            rs = self.apply_gates(H, qubit)
            return rs
    def not_gate(self, qubit):
        if 1 <= qubit <= self.num_q:
            X = np.array([[0, 1],[1,0]])
            rs = self.apply_gates(X, qubit)
            return rs

    def z_gate(self, qubit):
        if 1 <= qubit <= self.num_q:
            Z = np.array([[0,1], [1,0]])
            rs = self.apply_gates(Z, qubit)
            return rs

    def y_gate(self, qubit):
        if 1 <= qubit <= self.num_q:
            Y = np.array([[0,-1j],[1j,0]])
            rs = self.apply_gates(Y, qubit)
            return rs

    def cnot_gate(self, control, target):
        new_state = np.zeros(self.state.num_states, dtype=complex)
        for i, amp in enumerate(self.state.state):
            bit = format(i, f"0{self.num_q}b")
            if int(bit[control - 1]) == 1:
               target_m = 1 << (self.num_q - target)
               new_index = i ^ target_m
               new_state[new_index] = amp
            else:
                new_state[i] = amp
        print(new_state)
        self.state.state = new_state

    def oracle(self, target):
        self.state.state[target] *= -1

    def cz_gate(self, control, target):
        for i, amp in enumerate(self.state.state):
            bit = format(i, f"0{self.num_q}b")
            if int(bit[control - 1]) == 1 and int(bit[target - 1]) == 1:
                self.state.state *= -1
    
    def tCZ_gate(self):
        t_mask = (2 ** (self.num_q)) - 1
        self.state.state[t_mask] *= -1

    def apply_gates(self, g, qubit):        
        self.state.state = self.single_gate_kron(self.state.state, g, self.num_q, qubit)
        return self.state.state

    def single_gate_kron(self, state, g, num_q, qubit):
        state_tensor = state.reshape((2,) * num_q)

        axis = qubit - 1
        state_tensor = np.moveaxis(state_tensor, axis, 0)
        shape = state_tensor.shape
        pairs = state_tensor.reshape(2, -1)
        updated = g @ pairs
        updated = updated.reshape(shape)
        updated = np.moveaxis(updated, 0, axis)
        return updated.reshape(-1)

    def diffusion(self):
        for i in range(1, self.num_q + 1):
            self.h_gate(i)
        for i in range(1, self.num_q + 1):
            self.not_gate(i)
        self.tCZ_gate()
        for i in range(1, self.num_q + 1):
            self.not_gate(i)
        for i in range(1, self.num_q + 1):
            self.h_gate(i)




