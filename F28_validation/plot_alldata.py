import energy_dissipation as e
import acceleration as a
import matplotlib.pyplot as plt
import numpy as np

savefig = True

if savefig:
    print('#========== SAVING ALL PLOTS ==========#')


## ====================================== ##
## ======= acceleration plotting ======== ##

fig_dri, ax_dri = plt.subplots()
ax_dri.set_xlabel(r'Position ID')
ax_dri.set_ylabel(r'DRI [-]')
ax_dri.set_title('Dynamic Response Index at accelerometers locations')
ax_dri.minorticks_on()
ax_dri.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
ax_dri.set_ylim(bottom = 0, top = np.hstack([a.DRI4, a.DRI5, a.DRI6]).max() * 1.1)
ax_dri.set_xticks(a.mean_accel.x[::1])
ax_dri.set_xticklabels(a.mean_accel.x.astype(int))

ax_dri.scatter(a.mean_accel.x, a.DRI4, label = '4 Frames Section', s=16)
ax_dri.scatter(a.mean_accel.x, a.DRI5, label = '5 Frames Section', s=16)
ax_dri.scatter(a.mean_accel.x, a.DRI6, label = '6 Frames Section', s=16)

ax_dri.legend()
fig_dri.set_size_inches(8 * 1.125, 6 * 1.125)
fig_dri.tight_layout()

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
    fig1.savefig('mean_accelerations.pdf', dpi = 900, format = 'pdf')

a.ACC4.plot_time_history(savefig=savefig)
a.ACC5.plot_time_history(savefig=savefig)
a.ACC6.plot_time_history(savefig=savefig)

## ====================================== ##
## ========== energy plotting =========== ##

e.plot_pie(e.Xue_fraction, e.E4_f, e.E5_f, e.E6_f, e.pielabel, savefig=savefig)
e.plot_time(e.E4, savefig=savefig)
e.plot_time(e.E5, savefig=savefig)
e.plot_time(e.E6, savefig=savefig)


plt.show()
