import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
import pandas as pd
import seaborn as sns
sns.set()

# variables
xi = 0.224
wn = 52.9


df = pd.read_csv('z_acc_totfloor.csv', delimiter = ',', header = 1, index_col=None, encoding = 'ISO-8859-1')
# df = df.reset_index()
df.dropna(axis=1, inplace = True)
time = df.to_numpy()[:-1,0]
z_t = df.to_numpy()[:-1,1:] / 1000

# # initial state
y = np.array([0,0])   # [velocity, displacement]

A = np.array([[1,0],[0,1]])
B = np.array([[2 * xi * wn,wn**2],[-1,0]])
F = np.array([0.0,0.0])

Y = []
force = []
DRIs = []
z_t_col = 0


# time-stepping solution
progress_i = 1
for j in range(z_t.shape[1]):
    Y = []
    force = []
    for i in range(time.shape[0]-1):
        F[0] = z_t[i, j]
        delta_t = time[i+1] - time[i]
        y = y + delta_t * inv(A).dot( F - B.dot(y) )
        Y.append(y[1])
        force.append(F[0])



    Y = np.array(Y)
    Y_max = np.max(np.abs(Y))
    DRI = wn**2 * Y_max / 9.81
    # print('DRI = %1.2f' %DRI)
    DRIs.append(DRI)
    progress = round(j / z_t.shape[1] * 100)
    if progress%10==0 and progress > 0:
        if progress / progress_i == 10:
            progress_i += 1
            print(progress, '% completed')


DRIs = np.array(DRIs)
DRI = np.average(DRIs)
print('DRI = %1.3f' %DRI)
fig, ax = plt.subplots()
ax.set_xlabel(r'$DRI$ [-]')
ax.set_ylabel(r'Recurrence [%]')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

ax.hist(DRIs, density = True, bins=30)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

