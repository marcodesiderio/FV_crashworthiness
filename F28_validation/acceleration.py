import os.path
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import seaborn as sns
sns.set()


rootdir = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0'

# acceleration history
## load data and clean up data set
df_accel = pd.read_csv(os.path.join(rootdir, 'AT3_floor.csv'), delimiter=',')
slice_rows = df_accel.index[df_accel['Time(s)']=='Time(s)']
n_rows = (df_accel['Time(s)'].shape[0] - slice_rows.shape[0]) // (slice_rows.shape[0]+1)
time = np.array(df_accel['Time(s)'][:slice_rows[0]]).astype(float)
## create Butterworth filter
fs = 1 / 0.005 #sampling frequency
fc = 60 # cut-off frequency
b_filter, a_filter = signal.butter(5, fc, 'low', fs= fs)

# initialize everything

## initialize plotting
fig, ax = plt.subplots()
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

acc_z = np.zeros((n_rows, slice_rows.shape[0] + 1))
acc_z_filtered = np.zeros((n_rows, slice_rows.shape[0] + 1))
start = 0
j = 0
for i in slice_rows:
    data = np.array(df_accel['Acceleration(m_s2)'][start:i]).astype(float)
    filtered_data = signal.filtfilt(b_filter, a_filter, data)
    acc_z[:, j] = data
    acc_z_filtered[:, j] = filtered_data
    start = i + 1
    j += 1

j = 1
for i in range(acc_z_filtered.shape[1]):
    filtered_data = acc_z_filtered[:, i]
    linestyle = '-'
    if j > 6:
        linestyle = '--'
    label = 'Accel. position ' + str(j)
    ax.plot(time * 1e3, filtered_data / 9.81, label=label, linestyle = linestyle)
    j += 1



ax.set_xlabel('Time [ms]')
ax.set_ylabel(r'$g$ [-]')
ax.set_title('Butterworth 60Hz filtered accelerometers data')
plt.legend()
plt.show()
