import numpy as np

class Qubit:
    def __init__(self, state=None):
        if state is None:
            self.state = np.array([1+0j, 0+0j])
        else:
            self.state = np.array(state, dtype=complex)
        self.normalize()
    
    def normalize(self):
        norm = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError("Zero state norm")
        self.state = self.state / norm

    def measure(self):
        probs = np.abs(self.state) ** 2
        return np.random.choice([0, 1], p=probs)
    
    def __repr__(self):
        return f"{self.state[0]:.3f}|0> + {self.state[1]:.3f}|1>"
    
if __name__ == "__main__":
    pass