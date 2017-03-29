import matplotlib.pyplot as plt
import numpy as np

class graph:
    def __init__(self, func):
        self.func = func

    def plot(self, func):
        x = np.arange(0,5,0.001)
        self.y = func(x)
        plt.plot(x, self.y)
        plt.show()

def f(x):
    return x**2

g1 = graph(f)
g1.plot(f)
