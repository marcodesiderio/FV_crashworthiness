import energy_dissipation as e
import acceleration as a
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from tkinter import *

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


savepath = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\ovalization_study\figures'
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
ax_dri.set_ylim(bottom = 0, top = np.hstack([a.DRI000, a.DRI015, a.DRI030]).max() * 1.1)
ax_dri.set_xticks(a.frames)
ax_dri.set_xticklabels(a.frames)
data = [a.DRI000, a.DRI015, a.DRI030, a.DRI045]
ax_dri.plot(a.frames, a.DRI_mean, marker = 'o', markersize = 6, label='Average value')
ax_dri.boxplot(data, positions = [0, 0.15, 0.30, 0.45])
ax_dri.scatter(a.frames[0] * np.ones_like(a.DRI000), a.DRI000, label = 'e = 0.0', s=16)
ax_dri.scatter(a.frames[1] * np.ones_like(a.DRI015), a.DRI015, label = 'e = 0.15', s=16)
ax_dri.scatter(a.frames[2] * np.ones_like(a.DRI030), a.DRI030, label = 'e = 0.30', s=16)
ax_dri.scatter(a.frames[3] * np.ones_like(a.DRI045), a.DRI045, label = 'e = 0.45', s=16)

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
ax0.set_ylim(bottom = 0, top = np.hstack([a.mean_accels_000, a.mean_accels_015, a.mean_accels_030]).max() * 1.1)
ax0.set_xticks(a.frames)
ax0.set_xticklabels(a.frames)
data = [a.mean_accels_000, a.mean_accels_015, a.mean_accels_030, a.mean_accels_045]
ax0.boxplot(data, positions = [0, 0.15, 0.30, 0.45])
ax0.plot(a.frames, a.mean_accels_avg, marker = 'o', markersize = 6, label = 'Average value')
ax0.scatter(a.frames[0] * np.ones_like(a.mean_accels_000), a.mean_accels_000, label = '0', s=16)
ax0.scatter(a.frames[1] * np.ones_like(a.mean_accels_015), a.mean_accels_015, label = '15', s=16)
ax0.scatter(a.frames[2] * np.ones_like(a.mean_accels_030), a.mean_accels_030, label = '30', s=16)
ax0.scatter(a.frames[3] * np.ones_like(a.mean_accels_045), a.mean_accels_030, label = '45', s=16)
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
ax1.set_ylim(bottom = 0, top = np.hstack([a.mean_accel.upper, a.mean_accels_000, a.mean_accels_015, a.mean_accels_030]).max() * 1.1)
ax1.set_xticks(a.mean_accel.x[::1])
ax1.set_xticklabels(a.mean_accel.x.astype(int))

ax1.scatter(a.mean_accel.x, a.mean_accels_000, s=15, label = 'e = 0.0')
ax1.scatter(a.mean_accel.x, a.mean_accels_015, s=15, label = 'e = 0.15')
ax1.scatter(a.mean_accel.x, a.mean_accels_030, s=15, label = 'e = 0.30')
ax1.scatter(a.mean_accel.x, a.mean_accels_045, s=15, label = 'e = 0.45')
ax1.legend()

fig1.set_size_inches(8 * 1.125, 6 * 1.125)
fig1.tight_layout()
if savefig:
    savestr = 'mean_accelerations.pdf'
    savestr = os.path.join(savepath, savestr)
    fig1.savefig(savestr, dpi = 900, format = 'pdf')

a.ACC000.plot_time_history(savefig=savefig, savepath=savepath)
a.ACC015.plot_time_history(savefig=savefig, savepath=savepath)
a.ACC030.plot_time_history(savefig=savefig, savepath=savepath)
a.ACC045.plot_time_history(savefig=savefig, savepath=savepath)

a.ACC000.plot_FFT(savefig=savefig, savepath=savepath)
a.ACC015.plot_FFT(savefig=savefig, savepath=savepath)
a.ACC030.plot_FFT(savefig=savefig, savepath=savepath)
a.ACC045.plot_FFT(savefig=savefig, savepath=savepath)

## ====================================== ##
## ========== energy plotting =========== ##

e.plot_pie(e.E000_f, e.E015_f, e.E030_f, e.E045_f, e.E060_f, e.E070_f, e.pielabel, savefig=savefig, savepath=savepath)
e.plot_time(e.E000, savefig=savefig, savepath=savepath)
e.plot_time(e.E015, savefig=savefig, savepath=savepath)
e.plot_time(e.E030, savefig=savefig, savepath=savepath)
e.plot_time(e.E045, savefig=savefig, savepath=savepath)
e.plot_time(e.E060, savefig=savefig, savepath=savepath)
e.plot_time(e.E070, savefig=savefig, savepath=savepath)



plt.show()
