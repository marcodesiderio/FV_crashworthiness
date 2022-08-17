import matplotlib.pyplot as plt
import os

def plot_pie(Xue_fraction, E4_f, E5_f, E6_f, pielabel, savefig = False, savepath = ''):

    fig, ax = plt.subplots(2,2)
    explode = (0,0,0,0,0)
    ax[0, 0].pie(Xue_fraction, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[0, 0].axis('equal')
    ax[0, 0].set_title('Xue et al.')

    ax[0, 1].pie(E4_f, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[0, 1].axis('equal')
    ax[0, 1].set_title('Current work, 4 frames')

    ax[1, 0].pie(E5_f, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[1, 0].axis('equal')
    ax[1, 0].set_title('Current work, 5 frames')

    ax[1, 1].pie(E6_f, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[1, 1].axis('equal')
    ax[1, 1].set_title('Current work, 6 frames')
    fig.set_size_inches(8 * 1.5, 6 * 1.25)
    # fig.tight_layout()
    fig.suptitle('Energy absorption fraction; distribution by component')
    if savefig:
        savestr = 'E_by_component_fractions.pdf'
        savestr = os.path.join(savepath, savestr)
        fig.savefig(savestr, dpi=900, format='pdf')


def plot_time(E, savefig = False, savepath = ''):

    fig, ax = plt.subplots()
    ax.set_xlabel(r'Time [ms]')
    ax.set_ylabel(r'$E$ [kJ]')
    ax.set_title(E.label + ' fuselage section')
    ax.minorticks_on()
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    ax.plot(E.time * 1e3, E.KE / 1e3, label = 'Kinetic Energy', linestyle = '--')
    ax.plot(E.time * 1e3, E.frames / 1e3, label = 'Frames Plastic Energy')
    ax.plot(E.time * 1e3, E.shear_clips / 1e3, label = 'Shear Clips Plastic Energy')
    ax.plot(E.time * 1e3, E.skin / 1e3, label = 'Skin Plastic Energy')
    ax.plot(E.time * 1e3, E.stiffeners / 1e3, label = 'Stiffeners Plastic Energy')
    ax.plot(E.time * 1e3, E.struts / 1e3, label = 'Struts Plastic Energy')
    ax.plot(E.time * 1e3, E.beams / 1e3, label = 'Floor Beams Plastic Energy')
    ax.plot(E.time * 1e3, E.longbeams / 1e3, label = 'Floor Long. Beams Plastic Energy')
    ax.legend()
    fig.set_size_inches(8 * 1.125, 6 * 1.125)
    fig.tight_layout()

    if savefig:
        savestr = 'E_abs_by_component_' + E.label.replace(' ', '') + '.pdf'
        savestr = os.path.join(savepath, savestr)
        fig.savefig(savestr, dpi=900, format='pdf')
