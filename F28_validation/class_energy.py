import numpy as np
from numpy.linalg import inv

class crash_energy:
    __slots__ = ['E_init', 'E_final', 'E_t', 'E_frac']

    def __init__(self, data):
        self.E_init = data[0]
        self.E_final = data[-1]

