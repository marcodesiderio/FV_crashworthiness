import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()


rootdir = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0'
#mean accelerations
df = pd.read_csv('plot-data.csv', delimiter=',')
df['x'] = np.round(df['x'])
x = np.array(df['x'][:12])
a_exp = df[' y'][:12]
upper = df[' y'][12:24]
lower = df[' y'][24:]
