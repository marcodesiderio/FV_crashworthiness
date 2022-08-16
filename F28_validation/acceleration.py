import os.path
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
from functions import closest_idx
import mean_acceleration as mean_accel
import seaborn as sns
from read_abaqus_data import data as data_class
from class_acceleration import acceleration
import matplotlib
matplotlib.use('TkAgg')
sns.set()


rootdir = r'C:\Users\Marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0\4frames'
filename = 'AT3_floor'
data = data_class(rootdir, filename, '.csv', filter_data='False')
data_filtered = data.data_filtered
time = data.time

# determine DRI
DRI = acceleration(data.data, time).DRI

# determine mean acceleration data
idx_0 = 0
idx_1 = closest_idx(time, 0.11)

mean_accels = np.empty(0)

for i in range(data.data.shape[1]):
    temp = np.trapz(data.data[:idx_1, i], time[:idx_1]) / time[idx_1] / 9.81
    mean_accels = np.append(mean_accels, temp)





## initialize plotting
fig, ax = plt.subplots()
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

for i in range(data_filtered.shape[1]):
    filtered_data_temp = data_filtered[:, i]
    linestyle = '-'
    if i > 5:
        linestyle = '--'
    label = 'Accel. position ' + str(i+1)
    ax.plot(time * 1e3, filtered_data_temp / 9.81, label=label, linestyle = linestyle)


ax.set_xlabel('Time [ms]')
ax.set_ylabel(r'$g$ [-]')
ax.set_title('Butterworth 60Hz accelerometers data')
ax.legend()



fig1, ax1 = plt.subplots()
ax1.set_xlabel(r'Position ID')
ax1.set_ylabel(r'$g$ [-]')
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
ax1.set_ylim(bottom = 0, top = np.hstack([mean_accel.upper, mean_accels]).max() * 1.1)
ax1.set_xticks(mean_accel.x[::1])
ax1.set_xticklabels(mean_accel.x.astype(int))

ax1.plot(mean_accel.x, mean_accel.upper, label = 'Upper bound', color = 'k', marker = 'o',markersize=6)
ax1.plot(mean_accel.x, mean_accel.lower, label = 'Lower bound', color = 'k', marker = 'x',markersize=6)
ax1.scatter(mean_accel.x, mean_accel.a_exp, s = 15, label = 'NASA Drop Test')
ax1.scatter(mean_accel.x, mean_accels, s=15, label = 'Current work')
ax1.legend()


plt.show()
