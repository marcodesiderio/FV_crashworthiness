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

FR4 = data_class(rootdir_4, filename, '.csv', filter_data=True)
FR5 = data_class(rootdir_5, filename, '.csv', filter_data=True)
FR6 = data_class(rootdir_6, filename, '.csv', filter_data=True)

FR4_filtered = FR4.data_filtered
FR5_filtered = FR5.data_filtered
FR6_filtered = FR6.data_filtered

time = FR4.time
ACC4 = acceleration(FR4.data, FR4_filtered, FR4.time, '4 frames')
ACC5 = acceleration(FR5.data, FR5_filtered, FR5.time, '5 frames')
ACC6 = acceleration(FR6.data, FR6_filtered, FR6.time, '6 frames')

# determine DRI
DRI4 = ACC4.DRI
DRI5 = ACC5.DRI
DRI6 = ACC6.DRI
#determine mean accelerations
mean_accels_4 = ACC4.get_mean_accel(0.11)
mean_accels_5 = ACC5.get_mean_accel(0.11)
mean_accels_6 = ACC6.get_mean_accel(0.11)


