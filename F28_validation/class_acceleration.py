import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from functions import closest_idx


class acceleration:
    __slots__ = ['data', 'DRI', 'time', 'filtered', 'label']

    def __init__(self, data, filtered, time, label):
        self.label = label
        self.data = data
        self.time = time
        self.filtered = filtered

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
    def plot_time_history(self, savefig = False):
        fig, ax = plt.subplots()
        ax.minorticks_on()
        ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

        for i in range(self.filtered.shape[1]):
            filtered_data_temp = self.filtered[:, i]
            linestyle = '-'
            if i > 5:
                linestyle = '--'
            label = 'Accel. position ' + str(i+1)
            ax.plot(self.time * 1e3, filtered_data_temp / 9.81, label=label, linestyle = linestyle)


        ax.set_xlabel('Time [ms]')
        ax.set_ylabel(r'$g$ [-]')
        ax.set_title('Butterworth 60Hz accelerometers data, ' + self.label)
        ax.legend()
        fig.set_size_inches(8 * 1.125, 6 * 1.125)
        fig.tight_layout()
        if savefig:
            savestr = 'acc_z_' + self.label.replace(' ', '') + '.pdf'
            fig.savefig(savestr, dpi=900, format='pdf')

    def get_mean_accel(self, t_stop):
        idx_1 = closest_idx(self.time, t_stop)
        mean_accels = np.empty(0)

        for i in range(self.data.shape[1]):
            temp = np.trapz(self.data[:idx_1, i], self.time[:idx_1]) / self.time[idx_1] / 9.81
            mean_accels = np.append(mean_accels, temp)
        return mean_accels




