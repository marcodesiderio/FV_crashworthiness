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

rootdir_000 = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\ovalization_study\e=000'
rootdir_015 = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\ovalization_study\e=015'
rootdir_030 = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\ovalization_study\e=030'
rootdir_045 = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\ovalization_study\e=045'
rootdir_060 = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\ovalization_study\e=060'
rootdir_070 = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\ovalization_study\e=070'
filename = 'AT3_Floor'



FR000 = data_class(rootdir_000, filename, '.csv', filter_data=True, fc = 60)
FR015 = data_class(rootdir_015, filename, '.csv', filter_data=True, fc = 60)
FR030 = data_class(rootdir_030, filename, '.csv', filter_data=True, fc = 60)
FR045 = data_class(rootdir_045, filename, '.csv', filter_data=True, fc = 60)
# FR060 = data_class(rootdir_060, filename, '.csv', filter_data=True, fc = 60)
# FR070 = data_class(rootdir_070, filename, '.csv', filter_data=True, fc = 60)


FR000_filtered = FR000.data_filtered
FR015_filtered = FR015.data_filtered
FR030_filtered = FR030.data_filtered
FR045_filtered = FR045.data_filtered
# FR060_filtered = FR060.data_filtered
# FR070_filtered = FR070.data_filtered


time = FR000.time
ACC000 = acceleration(FR000, 'e = 0.0')
ACC015 = acceleration(FR015, 'e = 0.15')
ACC030 = acceleration(FR030, 'e = 0.30')
ACC045 = acceleration(FR045, 'e = 0.45')
# ACC060 = acceleration(FR060, 'e = 0.60')
# ACC070 = acceleration(FR070, 'e = 0.70')


# determine DRI
DRI000 = ACC000.DRI
DRI015 = ACC015.DRI
DRI030 = ACC030.DRI
DRI045 = ACC045.DRI
# DRI060 = ACC060.DRI
# DRI070 = ACC070.DRI

DRI000_mean = DRI000.mean()
DRI015_mean = DRI015.mean()
DRI030_mean = DRI030.mean()
DRI045_mean = DRI045.mean()
# DRI060_mean = DRI060.mean()
# DRI070_mean = DRI070.mean()

DRI_mean = np.array([DRI000_mean, DRI015_mean, DRI030_mean, DRI045_mean])
frames = np.array([0.0, 0.15, 0.30, 0.45])

#determine mean accelerations
mean_accels_000 = ACC000.get_mean_accel(0.11)
mean_accels_015 = ACC015.get_mean_accel(0.11)
mean_accels_030 = ACC030.get_mean_accel(0.11)
mean_accels_045 = ACC045.get_mean_accel(0.11)
# mean_accels_060 = ACC060.get_mean_accel(0.11)
# mean_accels_070 = ACC070.get_mean_accel(0.11)

mean_accels_000_avg = mean_accels_000.mean()
mean_accels_015_avg = mean_accels_015.mean()
mean_accels_030_avg = mean_accels_030.mean()
mean_accels_045_avg = mean_accels_045.mean()
# mean_accels_060_avg = mean_accels_060.mean()
# mean_accels_070_avg = mean_accels_070.mean()

mean_accels_avg = np.array([mean_accels_000_avg, mean_accels_015_avg, mean_accels_030_avg, mean_accels_030_avg])


