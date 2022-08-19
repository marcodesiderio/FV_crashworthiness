import os.path
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
from functions import closest_idx
import mean_acceleration as mean_accel
import seaborn as sns
from read_abaqus_data import data as data_class
from class_acceleration import acceleration
import matplotlib


matplotlib.use('TkAgg')
sns.set()

rootdir_4 = r'C:\Users\Marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0\4frames'
rootdir_5 = r'C:\Users\Marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0\5frames'
rootdir_6 = r'C:\Users\Marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0\6frames'
filename = 'AT3_Floor'



FR4 = data_class(rootdir_4, filename, '.csv', filter_data=True, fc = 60)
FR5 = data_class(rootdir_5, filename, '.csv', filter_data=True, fc = 60)
FR6 = data_class(rootdir_6, filename, '.csv', filter_data=True, fc = 60)

FR4_filtered = FR4.data_filtered
FR5_filtered = FR5.data_filtered
FR6_filtered = FR6.data_filtered

time = FR4.time
ACC4 = acceleration(FR4, '4 frames')
ACC5 = acceleration(FR5, '5 frames')
ACC6 = acceleration(FR6, '6 frames')

# determine DRI
DRI4 = ACC4.DRI
DRI5 = ACC5.DRI
DRI6 = ACC6.DRI

DRI4_mean = DRI4.mean()
DRI5_mean = DRI5.mean()
DRI6_mean = DRI6.mean()

DRI_mean = np.array([DRI4_mean, DRI5_mean, DRI6_mean])
frames = np.array([4, 5, 6]).astype(int)

#determine mean accelerations
mean_accels_4 = ACC4.get_mean_accel(0.11)
mean_accels_5 = ACC5.get_mean_accel(0.11)
mean_accels_6 = ACC6.get_mean_accel(0.11)

mean_accels_4_avg = mean_accels_4.mean()
mean_accels_5_avg = mean_accels_5.mean()
mean_accels_6_avg = mean_accels_6.mean()

mean_accels_avg = np.array([mean_accels_4_avg, mean_accels_5_avg, mean_accels_6_avg])


