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




# ALLPD_frames_fraction = np.max(ALLPD_frames) / ALLKE_max
# ALLPD_shear_clips_fraction = np.max(ALLPD_shear_clips) / ALLKE_max
# ALLPD_skin_fraction = np.max(ALLPD_skin) / ALLKE_max
# ALLPD_stiffeners_fraction = np.max(ALLPD_stiffeners) / ALLKE_max
# ALLPD_struts_fraction = np.max(ALLPD_struts) / ALLKE_max
# ALLPD_beams_fraction  = np.max(ALLPD_beams) / ALLKE_max
# ALLPD_longbeams_fraction = np.max(ALLPD_longbeams) / ALLKE_max
#
# pielabel = 'Frames and Shear clips', 'Skin and Stiffeners', 'Cabin Floor', 'Struts', 'Cargo Floor'
# Xue_fraction = np.array([59.08, 13.59, 2.31, 7.96, 16.33])
# current_fraction = 100 * np.array([ALLPD_frames_fraction + ALLPD_shear_clips_fraction, ALLPD_skin_fraction + ALLPD_stiffeners_fraction, ALLPD_longbeams_fraction + ALLPD_beams_fraction, ALLPD_struts_fraction, 0])
#
#
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
# fig1, ax1 = plt.subplots(1,2)
# explode = (0,0,0,0,0)
# ax1[0].pie(Xue_fraction, labels = pielabel, explode = explode, autopct='%1.1f%%')
# ax1[0].axis('equal')
# ax1[0].set_title('Xue et al.')
#
# ax1[1].pie(current_fraction, labels = pielabel, explode = explode, autopct='%1.1f%%')
# ax1[1].axis('equal')
# ax1[1].set_title('Current work, ' + case_label)
#
# plt.show()


