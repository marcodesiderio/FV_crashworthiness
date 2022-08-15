import os.path
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import seaborn as sns
from read_abaqus_data import data
from class_acceleration import acceleration
sns.set()


rootdir = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0'
filename = 'AT3_floor'
data_class = data(rootdir, filename, '.csv', filter_data='False')
data_filtered = data_class.data_filtered
time = data_class.time

DRI = acceleration(data_class.data, time).DRI

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
plt.legend()
plt.show()
