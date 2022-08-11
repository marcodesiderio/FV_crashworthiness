import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import latextable
from texttable import Texttable

sns.set()

#directory stuff
rootdir = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\LS Dyna\FV\tensile_testing\TensileHighStrain_Smert_et_al'
xforce_name = 'xforce'
xstrain_name = 'xstrain'
data_extension = '.csv'

#specimen dimensions and properties
# rectangular cross section
w = 1.75 #width, mm
t = 1.6 #thickness, mm
A = w * t #mm2
E = 7.17e4 #MPa
e02s = np.linspace(0, 800, 801) / E + 0.002


# initialize plotting

## to plot over an image:
# img = plt.imread("CAI_Energy.png")
# fig1, ax1 = plt.subplots()
#
# ax1.imshow(img)
# ax1.axis('off')
# ax1.scatter(1937, 957, label = 'Current Work', color = 'orange', s=150)
# ax1.legend(fontsize=15, loc= (0.855, 0.485))
fig, ax = plt.subplots()
ax.set_xlabel(r'$\epsilon$ [-]')
ax.set_ylabel(r'$\sigma_x$ [MPa]')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

sig_ys = np.empty(0)
e_dots = np.empty(0)

ID = 0
test_IDs = []
for dir in os.listdir(rootdir):
    subdir = os.path.join(rootdir, dir)
    if os.path.isdir(subdir):
        count_xforce = 0
        count_xstrain = 0
        files = os.listdir(subdir)
        for file in files:
            if xforce_name in file and data_extension in file:
                df_dir_force = os.path.join(subdir, file)
                # print(df_dir_force)
                # assert count_xforce == 0, f'multiple xforce files found, check {subdir}'
                count_xforce += 1
                if count_xforce > 1:
                    raise ValueError(f'multiple xforce files found, check {subdir}')
            if xstrain_name in file and data_extension in file:
                df_dir_strain = os.path.join(subdir, file)
                # print(df_dir_strain)
                # assert count_xstrain == 0, f'multiple xstrain files found, check {subdir}'
                count_xstrain += 1
                if count_xstrain > 1:
                    raise ValueError(f'multiple xstrain files found, check {subdir}')

        if count_xforce == 1 and count_xstrain == 1:
            #process force data to get stress
            force_df = pd.read_csv(df_dir_force, delimiter = ',', header = 1)
            time = force_df.to_numpy()[:,0]
            force = force_df.to_numpy()[:,1]
            sigma_x = force / A
            #process strain data
            strain_df = pd.read_csv(df_dir_strain, delimiter = ',', header = 1)
            ex = np.mean(strain_df.to_numpy()[:, 1:-1:2], axis = 1)
            # remove after failure data
            sigma_x = np.insert(sigma_x[ex > 0], 0, 0)
            #flip sign is avg stress is negative
            if np.mean(sigma_x) < 0:
                sigma_x = - sigma_x
            time = np.insert(time[ex > 0], 0, 0)
            ex = np.insert(ex[ex > 0], 0, 0)
            ex_argmax = np.argmax(ex)
            ex01_arg = np.argmax(ex>0.01)
            e_dot = round(ex[ex01_arg] / time[ex01_arg], 4)
            #plot stress-strain
            ax.plot(ex[:ex_argmax], sigma_x[:ex_argmax], label = r'$\dot{\epsilon}$ = ' + str(e_dot) + r'$s^{-1}$')
            ey = ex - sigma_x / E - 0.002 ## 0.2proof yield strain
            argyield = np.argmax(ey > 0)
            sigma_y = sigma_x[argyield]
            # print('Folder: ', dir)
            # print('Sigma_y0.2 = %1.4f' % sigma_y, '@ e_dot = %1.4f' % e_dot)
            sig_ys = np.append(sig_ys, sigma_y)
            e_dots = np.append(e_dots, e_dot)
            ID += 1
            test_ID = 'Tensile' + str(ID)

# rows = [['Test ID', r'$\dot{\epsilon}$ [\SI{mm/mm}]', '$\sigma_x$ [MPa]'],
#         []]

ax.legend()
plt.show()
