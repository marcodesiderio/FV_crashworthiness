import numpy as np
from numpy.linalg import inv
import os
import pandas as pd

class energy_data:
    __slots__ = ['KE', 'floor', 'skin', 'stiffeners', 'struts', 'frames', 'shear_clips', 'KE_max', 'beams', 'longbeams', 'time',
                 'floor_f', 'skin_f', 'stiffeners_f', 'struts_f', 'frames_f', 'shear_clips_f', 'label']

    def __init__(self, path, label):
        ALLKE_filename = 'ALLKE_Global.csv'
        ALLPD_frames_filename = 'ALLPD_Frames.csv'
        ALLPD_shear_clips_filename = 'ALLPD_Shear_clips.csv'
        ALLPD_skin_filename = 'ALLPD_Skin.csv'
        ALLPD_stiffeners_filename = 'ALLPD_Stiffeners.csv'
        ALLPD_struts_filename = 'ALLPD_Floor_struts.csv'
        ALLPD_beams_filename = 'ALLPD_floor_beams.csv'
        ALLPD_longbeams_filename = 'ALLPD_floor_long_beams.csv'

        path_global = os.path.join(path, ALLKE_filename)
        path_frames = os.path.join(path, ALLPD_frames_filename)
        path_shear_clips = os.path.join(path, ALLPD_shear_clips_filename)
        path_skin = os.path.join(path, ALLPD_skin_filename)
        path_stiffeners = os.path.join(path, ALLPD_stiffeners_filename)
        path_struts = os.path.join(path, ALLPD_struts_filename)
        path_beams = os.path.join(path, ALLPD_beams_filename)
        path_longbeams = os.path.join(path, ALLPD_longbeams_filename)

        ALLKE = pd.read_csv(path_global, delimiter=',')
        self.frames = np.array(pd.read_csv(path_frames, delimiter=',')['Energy(J)'])
        self.shear_clips = np.array(pd.read_csv(path_shear_clips, delimiter=',')['Energy(J)']).astype(float)
        self.skin = np.array(pd.read_csv(path_skin, delimiter=',')['Energy(J)']).astype(float)
        self.stiffeners = np.array(pd.read_csv(path_stiffeners, delimiter=',')['Energy(J)']).astype(float)
        self.struts = np.array(pd.read_csv(path_struts, delimiter=',')['Energy(J)']).astype(float)
        self.beams = np.array(pd.read_csv(path_beams, delimiter=',')['Energy(J)']).astype(float)
        self.longbeams = np.array(pd.read_csv(path_longbeams, delimiter=',')['Energy(J)']).astype(float)

        self.floor = self.beams + self.longbeams
        self.KE = np.array(ALLKE['Energy(J)']).astype(float)
        self.KE_max = self.KE[0]
        self.time = ALLKE['Time(s)']

        tot = self.frames[-1] + self.shear_clips[-1] + self.skin[-1] + self.stiffeners[-1] + self.struts[-1] + self.floor[-1]
        self.frames_f = self.frames[-1] / tot
        self.shear_clips_f = self.shear_clips[-1] / tot
        self.skin_f = self.skin[-1] / tot
        self.stiffeners_f = self.stiffeners[-1] / tot
        self.struts_f = self.struts[-1] / tot
        self.floor_f = self.floor[-1] / tot

        self.label = label




