# import standard libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from class_energy import energy_data
matplotlib.use('TkAgg')
sns.set()

#import custom files

import abaqus_keyword_parser as parse

generalpath = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0'

path4 = os.path.join(generalpath, '4frames')
path5 = os.path.join(generalpath, '5frames')
path6 = os.path.join(generalpath, '6frames')

E4 = energy_data(path4)
E5 = energy_data(path5)
E6 = energy_data(path6)

pielabel = 'Frames and shear clips', 'Skin and stiffeners', 'Cabin floor', 'Struts', 'Cargo floor'
Xue_fraction = np.array([59.08, 13.59, 2.31, 7.96, 16.33])
E4_f = 100 * np.array([E4.frames_f + E4.shear_clips_f, E4.skin_f + E4.stiffeners_f, E4.floor_f, E4.struts_f, 0])
E5_f = 100 * np.array([E5.frames_f + E5.shear_clips_f, E5.skin_f + E5.stiffeners_f, E5.floor_f, E5.struts_f, 0])
E6_f = 100 * np.array([E6.frames_f + E6.shear_clips_f, E6.skin_f + E6.stiffeners_f, E6.floor_f, E6.struts_f, 0])

# fig, ax = plt.subplots()
# ax.set_xlabel(r'Time [ms]')
# ax.set_ylabel(r'$E$ [kJ]')
# ax.set_title(case_label)
# ax.minorticks_on()
# ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#
# ax.plot(time * 1e3, ALLKE / 1e3, label = 'Kinetic Energy', linestyle = '--')
# ax.plot(time * 1e3, ALLPD_frames / 1e3, label = 'Frames Plastic Energy')
# ax.plot(time * 1e3, ALLPD_shear_clips / 1e3, label = 'Shear Clips Plastic Energy')
# ax.plot(time * 1e3, ALLPD_skin / 1e3, label = 'Skin Plastic Energy')
# ax.plot(time * 1e3, ALLPD_stiffeners / 1e3, label = 'Stiffeners Plastic Energy')
# ax.plot(time * 1e3, ALLPD_struts / 1e3, label = 'Struts Plastic Energy')
# ax.plot(time * 1e3, ALLPD_beams / 1e3, label = 'Floor Beams Plastic Energy')
# ax.plot(time * 1e3, ALLPD_longbeams / 1e3, label = 'Floor Long. Beams Plastic Energy')
# ax.legend()
#
fig1, ax1 = plt.subplots(2,2)
explode = (0,0,0,0,0)
ax1[0, 0].pie(Xue_fraction, labels = pielabel, explode = explode, autopct='%1.1f%%')
ax1[0, 0].axis('equal')
ax1[0, 0].set_title('Xue et al.')

ax1[0, 1].pie(E4_f, labels = pielabel, explode = explode, autopct='%1.1f%%')
ax1[0, 1].axis('equal')
ax1[0, 1].set_title('Current work, 4 frames')

ax1[1, 0].pie(E5_f, labels = pielabel, explode = explode, autopct='%1.1f%%')
ax1[1, 0].axis('equal')
ax1[1, 0].set_title('Current work, 5 frames')

ax1[1, 1].pie(E6_f, labels = pielabel, explode = explode, autopct='%1.1f%%')
ax1[1, 1].axis('equal')
ax1[1, 1].set_title('Current work, 6 frames')
fig1.show()
