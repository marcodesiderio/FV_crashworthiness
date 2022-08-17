import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from functions import closest_idx
import os


class acceleration:
    __slots__ = ['data', 'DRI', 'time', 'filtered', 'label', 'data_class']

    def __init__(self, data_class, label):
        self.label = label
        self.data = data_class.data
        self.time = data_class.time
        self.filtered = data_class.data_filtered
        self.data_class = data_class

        if len(self.data.shape) == 1:
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
    def plot_time_history(self, savefig = False, savepath = ''):
        fig, ax = plt.subplots()
        ax.minorticks_on()
        ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        switch = 1
        for i in range(self.filtered.shape[1]):
            filtered_data_temp = self.filtered[:, i]
            linestyle = '-'
            if i > 5:
                linestyle = '--'
            if switch == 1:
                marker = 'x'
            elif switch == -1:
                marker = 'o'
            if (i+1) % 3 == 0:
                switch = - switch
            label = 'Accel. position ' + str(i+1)
            ax.plot(self.time * 1e3, filtered_data_temp / 9.81, label=label, linestyle = linestyle, marker= marker, markevery= 10, markersize = 5)


        ax.set_xlabel('Time [ms]')
        ax.set_ylabel(r'$g$ [-]')
        ax.set_title('Butterworth ' + str(self.data_class.fc) + 'Hz accelerometers data, ' + self.label + ' fuselage section')
        ax.legend()
        fig.set_size_inches(8 * 1.125, 6 * 1.125)
        fig.tight_layout()
        if savefig:
            savestr = 'butterworth' + str(self.data_class.fc) + 'Hz_acc_z_' + self.label.replace(' ', '') + '.pdf'
            savestr = os.path.join(savepath, savestr)
            fig.savefig(savestr, dpi=900, format='pdf')

    def get_mean_accel(self, t_stop):
        idx_1 = closest_idx(self.time, t_stop)
        mean_accels = np.empty(0)

        for i in range(self.data.shape[1]):
            temp = np.trapz(self.data[:idx_1, i], self.time[:idx_1]) / self.time[idx_1] / 9.81
            mean_accels = np.append(mean_accels, temp)
        return mean_accels




