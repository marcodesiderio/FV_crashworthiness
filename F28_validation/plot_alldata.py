import pandas as pd

import energy_dissipation as e
import acceleration as a
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from tkinter import *
import seaborn as sns

def set_value(value):
    global savefig
    savefig = value
def exit(exit_val):
    global running
    running = exit_val


savefig = None
running = True

gui = Tk(className= 'Save plots as PDF?')
gui.geometry("300x190+600+300")
pixelVirtual = PhotoImage(width=1, height=1)

Button(gui, text='Save all plots',command=lambda *args: set_value(True), bg='#9BFF75', fg='black', image=pixelVirtual, width=200, height=38, compound="c").pack()
Button(gui, text='Do not save',command=lambda *args: set_value(False), bg='#FF8E75', fg='black', image=pixelVirtual, width=200, height=38, compound="c") .pack()
Button(gui, text='Terminate program',command=lambda *args: exit(False), bg='#000000', fg='white', image=pixelVirtual, width=200, height=38, compound="c") .pack()
Button(gui, text='Accept and continue',command=gui.destroy, image=pixelVirtual, width=200, height=38, compound="c").pack()

mainloop()
if not running:
    sys.exit()
if savefig == None:
    print('No savefig selection. Exiting...')
    sys.exit()


savepath = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0\figures'
# savepath = r''


if savefig:
    print('#========== SAVING ALL PLOTS ==========#')
    print('Saving directory:')
    if savepath =='':
        print('The saving directory is the current working directory.')
    else:
        print(savepath)


## ====================================== ##
## ======= acceleration plotting ======== ##

fig_dri, ax_dri = plt.subplots()
ax_dri.set_xlabel(r'Number of frames')
ax_dri.set_ylabel(r'DRI (average) [-]')
ax_dri.set_title('Average DRI vs number of frames of tested section')
ax_dri.minorticks_on()
ax_dri.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
ax_dri.set_ylim(bottom = 0, top = np.hstack([a.DRI4, a.DRI5, a.DRI6]).max() * 1.1)
ax_dri.set_xticks(a.frames)
ax_dri.set_xticklabels(a.frames)
data = [a.DRI4, a.DRI5, a.DRI6]
ax_dri.plot(a.frames, a.DRI_mean, marker = 'o', markersize = 6, label='Average value')
ax_dri.boxplot(data, positions = [4,5,6])
ax_dri.scatter(a.frames[0] * np.ones_like(a.DRI4), a.DRI5, label = '4 Frames Section', s=16)
ax_dri.scatter(a.frames[1] * np.ones_like(a.DRI5), a.DRI5, label = '5 Frames Section', s=16)
ax_dri.scatter(a.frames[2] * np.ones_like(a.DRI6), a.DRI6, label = '6 Frames Section', s=16)

ax_dri.legend()
fig_dri.set_size_inches(8 * 1.125, 6 * 1.125)
fig_dri.tight_layout()
if savefig:
    savestr = 'DRIs.pdf'
    savestr = os.path.join(savepath, savestr)
    fig_dri.savefig(savestr, dpi = 900, format = 'pdf')

fig0, ax0 = plt.subplots()

ax0.set_xlabel(r'Number of Frames')
ax0.set_ylabel(r'$g$ [-]')
ax0.set_title('Mean accelerations vs number of frames')
ax0.minorticks_on()
ax0.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
ax0.set_ylim(bottom = 0, top = np.hstack([a.mean_accels_4, a.mean_accels_5, a.mean_accels_6]).max() * 1.1)
ax0.set_xticks(a.frames)
ax0.set_xticklabels(a.frames)

data = [a.mean_accels_4, a.mean_accels_5, a.mean_accels_6]
ax0.plot(a.frames, a.mean_accels_avg, marker = 'o', markersize = 6, label = 'Average value')
ax0.boxplot(data, positions = [4,5,6])
ax0.scatter(a.frames[0] * np.ones_like(a.mean_accels_4), a.mean_accels_4, label = '4 Frames Section', s=16)
ax0.scatter(a.frames[1] * np.ones_like(a.mean_accels_5), a.mean_accels_5, label = '5 Frames Section', s=16)
ax0.scatter(a.frames[2] * np.ones_like(a.mean_accels_6), a.mean_accels_6, label = '6 Frames Section', s=16)
ax0.legend()

fig0.set_size_inches(8 * 1.125, 6 * 1.125)
fig0.tight_layout()
if savefig:
    savestr = 'Average_accelerations.pdf'
    savestr = os.path.join(savepath, savestr)
    fig0.savefig(savestr, dpi = 900, format = 'pdf')


fig1, ax1 = plt.subplots()
ax1.set_xlabel(r'Position ID')
ax1.set_ylabel(r'$g$ [-]')
ax1.set_title('Mean accelerations')
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
ax1.set_ylim(bottom = 0, top = np.hstack([a.mean_accel.upper, a.mean_accels_4, a.mean_accels_5, a.mean_accels_6]).max() * 1.1)
ax1.set_xticks(a.mean_accel.x[::1])
ax1.set_xticklabels(a.mean_accel.x.astype(int))

ax1.plot(a.mean_accel.x, a.mean_accel.upper, label = 'Upper bound', color = 'k', marker = 'o',markersize=6)
ax1.plot(a.mean_accel.x, a.mean_accel.lower, label = 'Lower bound', color = 'k', marker = 'x',markersize=6)
ax1.scatter(a.mean_accel.x, a.mean_accel.a_exp, s = 15, label = 'NASA Drop Test')
ax1.scatter(a.mean_accel.x, a.mean_accels_4, s=15, label = 'Current work, 4 frames')
ax1.scatter(a.mean_accel.x, a.mean_accels_5, s=15, label = 'Current work, 5 frames')
ax1.scatter(a.mean_accel.x, a.mean_accels_6, s=15, label = 'Current work, 6 frames')
ax1.legend()

fig1.set_size_inches(8 * 1.125, 6 * 1.125)
fig1.tight_layout()
if savefig:
    savestr = 'mean_accelerations.pdf'
    savestr = os.path.join(savepath, savestr)
    fig1.savefig(savestr, dpi = 900, format = 'pdf')

a.ACC4.plot_time_history(savefig=savefig, savepath=savepath)
a.ACC5.plot_time_history(savefig=savefig, savepath=savepath)
a.ACC6.plot_time_history(savefig=savefig, savepath=savepath)

a.ACC4.plot_FFT(savefig=savefig, savepath=savepath)
a.ACC5.plot_FFT(savefig=savefig, savepath=savepath)
a.ACC6.plot_FFT(savefig=savefig, savepath=savepath)

## ====================================== ##
## ========== energy plotting =========== ##

e.plot_pie(e.Xue_fraction, e.E4_f, e.E5_f, e.E6_f, e.pielabel, savefig=savefig, savepath=savepath)
e.plot_time(e.E4, savefig=savefig, savepath=savepath)
e.plot_time(e.E5, savefig=savefig, savepath=savepath)
e.plot_time(e.E6, savefig=savefig, savepath=savepath)


plt.show()
