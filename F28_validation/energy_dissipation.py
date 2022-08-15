# import standard libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#import custom files

import abaqus_keyword_parser as parse


test = 'ALLKE'
outcome = parse.key[test]

rootdir = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0_energies'

ALLKE_filename = 'ALLKE_Global_Model.csv'
ALLPD_frames_filename = 'ALLPD_Frames.csv'
ALLPD_shear_clips_filename = 'ALLPD_Shear_clips.csv'
ALLPD_skin_filename = 'ALLPD_Skin.csv'
ALLPD_stiffeners_filename = 'ALLPD_Stiffeners.csv'
ALLPD_struts_filename = 'ALLPD_Struts.csv'
ALLPD_beams_filename = 'ALLPD_floor_beams.csv'
ALLPD_longbeams_filename = 'ALLPD_floor_long_beams.csv'

ALLKE = pd.read_csv(os.path.join(rootdir, ALLKE_filename), delimiter=',').iloc[: , :-1]
ALLPD_frames = pd.read_csv(os.path.join(rootdir, ALLPD_frames_filename), delimiter=',').iloc[: , :-1]['Energy(J)']
ALLPD_shear_clips = pd.read_csv(os.path.join(rootdir, ALLPD_shear_clips_filename), delimiter=',').iloc[: , :-1]['Energy(J)']
ALLPD_skin = pd.read_csv(os.path.join(rootdir, ALLPD_skin_filename), delimiter=',').iloc[: , :-1]['Energy(J)']
ALLPD_stiffeners = pd.read_csv(os.path.join(rootdir, ALLPD_stiffeners_filename), delimiter=',').iloc[: , :-1]['Energy(J)']
ALLPD_struts = pd.read_csv(os.path.join(rootdir, ALLPD_struts_filename), delimiter=',').iloc[: , :-1]['Energy(J)']
ALLPD_beams = pd.read_csv(os.path.join(rootdir, ALLPD_beams_filename), delimiter=',').iloc[: , :-1]['Energy(J)']
ALLPD_longbeams = pd.read_csv(os.path.join(rootdir, ALLPD_longbeams_filename), delimiter=',').iloc[: , :-1]['Energy(J)']

time = ALLKE['Time(s)']
ALLKE = ALLKE['Energy(J)']
ALLKE_max = ALLKE[0]

ALLPD_frames_fraction = np.max(ALLPD_frames) / ALLKE_max
ALLPD_shear_clips_fraction = np.max(ALLPD_shear_clips) / ALLKE_max
ALLPD_skin_fraction = np.max(ALLPD_skin) / ALLKE_max
ALLPD_stiffeners_fraction = np.max(ALLPD_stiffeners) / ALLKE_max
ALLPD_struts_fraction = np.max(ALLPD_struts) / ALLKE_max
ALLPD_beams_fraction  = np.max(ALLPD_beams) / ALLKE_max
ALLPD_longbeams_fraction = np.max(ALLPD_longbeams) / ALLKE_max

pielabel = 'Frames and Shear slips', 'Skin and Stiffeners', 'Cabin Floor', 'Struts', 'Cargo Floor'
Xue_fraction = np.array([59.08, 13.59, 2.31, 7.96, 16.33])
current_fraction = 100 * np.array([ALLPD_frames_fraction + ALLPD_shear_clips_fraction, ALLPD_skin_fraction + ALLPD_stiffeners_fraction, ALLPD_longbeams_fraction + ALLPD_beams_fraction, ALLPD_struts_fraction, 0])


fig, ax = plt.subplots()
ax.set_xlabel(r'Time [ms]')
ax.set_ylabel(r'$E$ [kJ]')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

ax.plot(time * 1e3, ALLKE / 1e3, label = 'Kinetic Energy', linestyle = '--')
ax.plot(time * 1e3, ALLPD_frames / 1e3, label = 'Frames Plastic Energy')
ax.plot(time * 1e3, ALLPD_shear_clips / 1e3, label = 'Shear Clips Plastic Energy')
ax.plot(time * 1e3, ALLPD_skin / 1e3, label = 'Skin Plastic Energy')
ax.plot(time * 1e3, ALLPD_stiffeners / 1e3, label = 'Stiffeners Plastic Energy')
ax.plot(time * 1e3, ALLPD_struts / 1e3, label = 'Struts Plastic Energy')
ax.plot(time * 1e3, ALLPD_beams / 1e3, label = 'Floor Beams Plastic Energy')
ax.plot(time * 1e3, ALLPD_longbeams / 1e3, label = 'Floor Long. Beams Plastic Energy')
ax.legend()

fig1, ax1 = plt.subplots(1,2)
explode = (0,0,0,0,0)
ax1[0].pie(Xue_fraction, labels = pielabel, explode = explode, autopct='%1.1f%%')
ax1[0].axis('equal')
ax1[0].set_title('Xue et al.')

ax1[1].pie(current_fraction, labels = pielabel, explode = explode, autopct='%1.1f%%')
ax1[1].axis('equal')
ax1[1].set_title('Current work')

plt.show()


