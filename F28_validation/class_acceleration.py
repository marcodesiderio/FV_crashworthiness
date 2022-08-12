import numpy as np
from numpy.linalg import inv


class acceleration:
    __slots__ = ['data', 'DRI', 'time']

    def __init__(self, data, time):
        self.data = data
        self.time = time

        if len(data.shape) == 1:
            z_t = self.data
            self.DRI = self.get_DRI(z_t)
        else:
            self.DRI = np.empty(0)
            for i in range(self.data.shape[1]):
                z_t = self.data[:, i]
                DRI = self.get_DRI(z_t)
                self.DRI = np.append(self.DRI, DRI)


    def get_DRI(self, z_t):
        time = self.time
        # standard values for damping and nat. freq.
        xi = 0.224
        wn = 52.9
        y = np.array([0, 0])  # [velocity, displacement]
        A = np.array([[1, 0], [0, 1]])
        B = np.array([[2 * xi * wn, wn ** 2], [-1, 0]])
        F = np.array([0.0, 0.0])
        Y = []
        for i in range(time.shape[0] - 1):
            F[0] = z_t[i]
            delta_t = time[i + 1] - time[i]
            y = y + delta_t * inv(A).dot(F - B.dot(y))
            Y.append(y[1])
        Y = np.array(Y)
        Y_max = np.max(np.abs(Y))
        DRI = wn ** 2 * Y_max / 9.81
        return DRI

