import pandas as pd
import numpy as np
import os
import scipy.signal as signal
import matplotlib.pyplot as plt
from abaqus_keyword_parser import key as parse_key
from abaqus_keyword_parser import y_labels, plots_scaling
import seaborn as sns
sns.set()

class data:
    __slots__ = ['rootdir', 'filename', 'df', 'data', 'data_filtered', 'data_label', 'data_type', 'add_label', 'labels',
                 'time', 'filter_data', 'fc', 'data_key', 'fs']

    def __init__(self, rootdir, filename, extension, add_label = '', filter_data = False, fc = 60, fs = 1000):
        self.fc = fc
        self.fs = fs
        self.labels = filename.split('_')
        self.data_key = self.labels[0]
        if len(add_label) > 0:
            self.labels.append(add_label)
        self.data_label = ' '.join(self.labels[1:])
        self.data_type = parse_key[self.data_key]
        self.rootdir = rootdir
        self.filename = filename + extension
        path = os.path.join(rootdir, self.filename)
        df = pd.read_csv(path, delimiter=',')
        slice_rows = df.index[df['Time(s)'] == 'Time(s)']
        if len(slice_rows) > 0:
            n_rows = (df['Time(s)'].shape[0] - slice_rows.shape[0]) // (slice_rows.shape[0] + 1)
            self.time = np.array(df['Time(s)'][:slice_rows[0]]).astype(float)
        else:
            n_rows = (df['Time(s)'].shape[0] - slice_rows.shape[0]) // (slice_rows.shape[0] + 1)
            self.time = np.array(df['Time(s)']).astype(float)
        if filter_data:
            ## create Butterworth filter
            fs = fs  # sampling frequency
            fc = fc  # cut-off frequency
            b_filter, a_filter = signal.butter(5, fc, 'low', fs=fs)
            self.data, self.data_filtered = self.gen_dataset_filtered(df, slice_rows, n_rows, b_filter, a_filter)

        else:
            self.data = self.gen_dataset(df, slice_rows, n_rows)

    def gen_dataset(self, df, slice_rows, n_rows):
        keys = df.keys()
        if len(slice_rows) > 0:
            data = np.zeros((n_rows, slice_rows.shape[0] + 1))
            start = 0
            j = 0
            # slice_rows = np.hstack((slice_rows, n_rows))
            for i in slice_rows:
                data_temp = np.array(df[keys[1]][start:i]).astype(float)
                data[:, j] = data_temp
                start = i + 1
                j += 1
            data_temp = np.array(df[keys[1]][start:]).astype(float)
            data[:, j] = data_temp
        else:
            data = np.array(df[keys[1]]).astype(float)

        return data

    def gen_dataset_filtered(self, df, slice_rows, n_rows, b, a):
        keys = df.keys()
        if len(slice_rows) > 0:
            data = np.zeros((n_rows, slice_rows.shape[0] + 1))
            data_filtered = np.zeros((n_rows, slice_rows.shape[0] + 1))
            start = 0
            j = 0

            for i in slice_rows:
                data_temp = np.array(df[keys[1]][start:i]).astype(float)
                data_filtered_temp = signal.filtfilt(b, a, data_temp)
                data[:, j] = data_temp
                data_filtered[:, j] = data_filtered_temp
                start = i + 1
                j += 1
            data_temp = np.array(df[keys[1]][start:]).astype(float)
            data_filtered_temp = signal.filtfilt(b, a, data_temp)
            data[:, j] = data_temp
            data_filtered[:, j] = data_filtered_temp
        else:
            data = np.array(df[keys[1]]).astype(float)
            data_filtered = signal.filtfilt(b, a, data)
        return data, data_filtered






