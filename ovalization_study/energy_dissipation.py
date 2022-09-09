# import standard libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from class_energy import energy_data
from energy_plotting import plot_pie, plot_time
matplotlib.use('TkAgg')
sns.set()

#import custom files

import abaqus_keyword_parser as parse

generalpath = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\ovalization_study'

path000 = os.path.join(generalpath, 'e=000')
path015 = os.path.join(generalpath, 'e=015')
path030 = os.path.join(generalpath, 'e=030')
path045 = os.path.join(generalpath, 'e=045')
path060 = os.path.join(generalpath, 'e=060')
path070 = os.path.join(generalpath, 'e=070')

E000 = energy_data(path000, 'e = 0.0')
E015 = energy_data(path015, 'e = 0.15')
E030 = energy_data(path030, 'e = 0.30')
E045 = energy_data(path045, 'e = 0.45')
E060 = energy_data(path060, 'e = 0.60')
E070 = energy_data(path070, 'e = 0.70')

pielabel = 'Frames and shear clips', 'Skin and stiffeners', 'Cabin floor', 'Struts'
Xue_fraction = np.array([59.08, 13.59, 2.31, 7.96, 16.33])
E000_f = 100 * np.array([E000.frames_f + E000.shear_clips_f, E000.skin_f + E000.stiffeners_f, E000.floor_f, E000.struts_f])
E015_f = 100 * np.array([E015.frames_f + E015.shear_clips_f, E015.skin_f + E015.stiffeners_f, E015.floor_f, E015.struts_f])
E030_f = 100 * np.array([E030.frames_f + E030.shear_clips_f, E030.skin_f + E030.stiffeners_f, E030.floor_f, E030.struts_f])
E045_f = 100 * np.array([E045.frames_f + E045.shear_clips_f, E045.skin_f + E045.stiffeners_f, E045.floor_f, E045.struts_f])
E060_f = 100 * np.array([E060.frames_f + E060.shear_clips_f, E060.skin_f + E060.stiffeners_f, E060.floor_f, E060.struts_f])
E070_f = 100 * np.array([E070.frames_f + E070.shear_clips_f, E070.skin_f + E070.stiffeners_f, E070.floor_f, E070.struts_f])



