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


rootdir_4 = r'C:\Users\Marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0\4frames'
rootdir_5 = r'C:\Users\Marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0\5frames'
rootdir_6 = r'C:\Users\Marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0\6frames'
filename = 'AT3_Floor'

FR4 = data_class(rootdir_4, filename, '.csv', filter_data=True)
FR5 = data_class(rootdir_5, filename, '.csv', filter_data=True)
FR6 = data_class(rootdir_6, filename, '.csv', filter_data=True)

FR4_filtered = FR4.data_filtered
FR5_filtered = FR5.data_filtered
FR6_filtered = FR6.data_filtered

time = FR4.time

# determine DRI
DRI4 = acceleration(FR4.data, FR4.time).DRI
DRI5 = acceleration(FR5.data, FR5.time).DRI
DRI6 = acceleration(FR6.data, FR6.time).DRI

fig_dri, ax_dri = plt.subplots()
ax_dri.set_xlabel(r'Position ID')
ax_dri.set_ylabel(r'DRI [-]')
ax_dri.minorticks_on()
ax_dri.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
ax_dri.set_ylim(bottom = 0, top = np.hstack([DRI4, DRI5, DRI6]).max() * 1.1)
ax_dri.set_xticks(mean_accel.x[::1])
ax_dri.set_xticklabels(mean_accel.x.astype(int))
ax_dri.scatter(mean_accel.x, DRI4, label = '4 Frames Section', s=16)
ax_dri.scatter(mean_accel.x, DRI5, label = '5 Frames Section', s=16)
ax_dri.scatter(mean_accel.x, DRI6, label = '6 Frames Section', s=16)
ax_dri.legend()



# determine mean acceleration data
idx_0 = 0
idx_1 = closest_idx(time, 0.11)

mean_accels_4 = np.empty(0)
mean_accels_5 = np.empty(0)
mean_accels_6 = np.empty(0)

for i in range(FR4.data.shape[1]):
    temp4 = np.trapz(FR4.data[:idx_1, i], FR4.time[:idx_1]) / FR4.time[idx_1] / 9.81
    temp5 = np.trapz(FR5.data[:idx_1, i], FR5.time[:idx_1]) / FR5.time[idx_1] / 9.81
    temp6 = np.trapz(FR6.data[:idx_1, i], FR6.time[:idx_1]) / FR6.time[idx_1] / 9.81
    mean_accels_4 = np.append(mean_accels_4, temp4)
    mean_accels_5 = np.append(mean_accels_5, temp5)
    mean_accels_6 = np.append(mean_accels_6, temp6)


# ## initialize plotting
# fig, ax = plt.subplots()
# ax.minorticks_on()
# ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#
# for i in range(data_filtered.shape[1]):
#     filtered_data_temp = data_filtered[:, i]
#     linestyle = '-'
#     if i > 5:
#         linestyle = '--'
#     label = 'Accel. position ' + str(i+1)
#     ax.plot(time * 1e3, filtered_data_temp / 9.81, label=label, linestyle = linestyle)
#
#
# ax.set_xlabel('Time [ms]')
# ax.set_ylabel(r'$g$ [-]')
# ax.set_title('Butterworth 60Hz accelerometers data')
# ax.legend()



fig1, ax1 = plt.subplots()
ax1.set_xlabel(r'Position ID')
ax1.set_ylabel(r'$g$ [-]')
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
ax1.set_ylim(bottom = 0, top = np.hstack([mean_accel.upper, mean_accels_4, mean_accels_5, mean_accels_6]).max() * 1.1)
ax1.set_xticks(mean_accel.x[::1])
ax1.set_xticklabels(mean_accel.x.astype(int))

ax1.plot(mean_accel.x, mean_accel.upper, label = 'Upper bound', color = 'k', marker = 'o',markersize=6)
ax1.plot(mean_accel.x, mean_accel.lower, label = 'Lower bound', color = 'k', marker = 'x',markersize=6)
ax1.scatter(mean_accel.x, mean_accel.a_exp, s = 15, label = 'NASA Drop Test')
ax1.scatter(mean_accel.x, mean_accels_4, s=15, label = 'Current work, 4 frames')
ax1.scatter(mean_accel.x, mean_accels_5, s=15, label = 'Current work, 5 frames')
ax1.scatter(mean_accel.x, mean_accels_6, s=15, label = 'Current work, 6 frames')
ax1.legend()

fig1.set_size_inches(8 * 1.125, 6 * 1.125)
fig1.savefig('mean_accelerations.pdf', dpi = 900, format = 'pdf')


plt.show()
