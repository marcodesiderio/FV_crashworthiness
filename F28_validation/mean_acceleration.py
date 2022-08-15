import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()


rootdir = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0'
#mean accelerations
df = pd.read_csv('plot-data.csv', delimiter=',')
df['x'] = np.round(df['x'])
x = np.array(df['x'][:12])
a_exp = df[' y'][:12]
upper = df[' y'][12:24]
lower = df[' y'][24:]
a_numerical = np.array([10.7, 10.7, 10.2, 9.55, 9.4, 9.0, 10.3, 10.1, 9.7, 9.1, 8.6, 8.2])
fig, ax = plt.subplots()
ax.set_xlabel(r'Position ID')
ax.set_ylabel(r'$g$ [-]')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
ax.set_ylim(bottom = 0, top = 12)
ax.set_xticks(x[::1])
ax.set_xticklabels(x.astype(int))

ax.plot(x, upper, label = 'Upper bound', color = 'k', marker = 'o',markersize=6)
ax.plot(x, lower, label = 'Lower bound', color = 'k', marker = 'x',markersize=6)
ax.scatter(x, a_exp, s = 15, label = 'NASA Drop Test')
ax.scatter(x, a_numerical, s=15, label = 'Current work')
plt.legend()

plt.show()
