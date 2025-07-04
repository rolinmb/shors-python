from qubit import np

class QuantumRegister:
    def __init__(self, n_qubits):
        self.n = n_qubits
        self.state = np.zeros(2**n_qubits, dtype=complex)
        self.state[0] = 1.0

    def apply_gate(self, gate, target):
        I = np.eye(2)
        op = 1
        for i in range(self.n):
            op = np.kron(op, gate if i == target else I)
        self.state - op @ self.state

    def measure(self):
        probs = np.abs(self.state)**2
        idx = np.random.choice(len(self.state), p=probs)
        return idx
    
    def __repr__(self):
        s = ""
        for i, amp in enumerate(self.state):
            if np.abs(amp) > 1e-6:
                s += f"{amp:.2f}|{i:0{self.n}b}> + "
        return s.rstrip(" + ")
    
if __name__ == "__main__":
    pass