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

generalpath = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0'

path4 = os.path.join(generalpath, '4frames')
path5 = os.path.join(generalpath, '5frames')
path6 = os.path.join(generalpath, '6frames')

E4 = energy_data(path4, '4 Frames')
E5 = energy_data(path5, '5 Frames')
E6 = energy_data(path6, '6 Frames')

pielabel = 'Frames and shear clips', 'Skin and stiffeners', 'Cabin floor', 'Struts', 'Cargo floor'
Xue_fraction = np.array([59.08, 13.59, 2.31, 7.96, 16.33])
E4_f = 100 * np.array([E4.frames_f + E4.shear_clips_f, E4.skin_f + E4.stiffeners_f, E4.floor_f, E4.struts_f, 0])
E5_f = 100 * np.array([E5.frames_f + E5.shear_clips_f, E5.skin_f + E5.stiffeners_f, E5.floor_f, E5.struts_f, 0])
E6_f = 100 * np.array([E6.frames_f + E6.shear_clips_f, E6.skin_f + E6.stiffeners_f, E6.floor_f, E6.struts_f, 0])



