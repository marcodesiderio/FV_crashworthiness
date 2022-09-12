import matplotlib.pyplot as plt
import os

def plot_pie(E00, E01, E02, E10, E11, E12, pielabel, savefig = False, savepath = ''):

    fig, ax = plt.subplots(2,3)
    explode = (0,0,0,0)
    ax[0, 0].pie(E00, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[0, 0].axis('equal')
    ax[0, 0].set_title('e = 0.0')

    ax[0, 1].pie(E01, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[0, 1].axis('equal')
    ax[0, 1].set_title('e = 0.15')

    ax[0, 2].pie(E02, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[0, 2].axis('equal')
    ax[0, 2].set_title('e = 0.30')

    ax[1, 0].pie(E10, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[1, 0].axis('equal')
    ax[1, 0].set_title('e = 0.45')

    ax[1, 1].pie(E11, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[1, 1].axis('equal')
    ax[1, 1].set_title('e = 0.60')

    ax[1, 2].pie(E12, labels = pielabel, explode = explode, autopct='%1.1f%%')
    ax[1, 2].axis('equal')
    ax[1, 2].set_title('e = 0.70')

    fig.set_size_inches(8 * 1.5, 6 * 1.25)
    # fig.tight_layout()
    fig.suptitle('Energy absorption fraction; distribution by component.')
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

def plot_keg_time(E1, E2, E3, E4, E5, E6, savefig = False, savepath = ''):
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Time [ms]')
    ax.set_ylabel(r'$E$ [kJ]')
    ax.set_title('ALLKE vs. time')
    ax.minorticks_on()
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    ax.plot(E1.time * 1e3, E1.KE / 1e3, label=E1.label)
    ax.plot(E2.time * 1e3, E2.KE / 1e3, label=E2.label)
    ax.plot(E3.time * 1e3, E3.KE / 1e3, label=E3.label)
    ax.plot(E4.time * 1e3, E4.KE / 1e3, label=E4.label)
    ax.plot(E5.time * 1e3, E5.KE / 1e3, label=E5.label)
    ax.plot(E6.time * 1e3, E6.KE / 1e3, label=E6.label)

    ax.legend()
    fig.set_size_inches(8 * 1.125, 6 * 1.125)
    fig.tight_layout()

    if savefig:
        savestr = 'ALLKE_vs_time' + '.pdf'
        savestr = os.path.join(savepath, savestr)
        fig.savefig(savestr, dpi=900, format='pdf')

def plot_FrSc_time(E1, E2, E3, E4, E5, E6, savefig = False, savepath = ''):
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Time [ms]')
    ax.set_ylabel(r'$E$ [kJ]')
    ax.set_title('ALLPD frames and shear clips vs. time')
    ax.minorticks_on()
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    ax.plot(E1.time * 1e3, E1.frames / 1e3 + E1.shear_clips / 1e3, label=E1.label)
    ax.plot(E2.time * 1e3, E2.frames / 1e3 + E2.shear_clips / 1e3, label=E2.label)
    ax.plot(E3.time * 1e3, E3.frames / 1e3 + E3.shear_clips / 1e3, label=E3.label)
    ax.plot(E4.time * 1e3, E4.frames / 1e3 + E4.shear_clips / 1e3, label=E4.label)
    ax.plot(E5.time * 1e3, E5.frames / 1e3 + E5.shear_clips / 1e3, label=E5.label)
    ax.plot(E6.time * 1e3, E6.frames / 1e3 + E6.shear_clips / 1e3, label=E6.label)

    ax.legend()
    fig.set_size_inches(8 * 1.125, 6 * 1.125)
    fig.tight_layout()

    if savefig:
        savestr = 'ALLPD_FrSc_vs_time' + '.pdf'
        savestr = os.path.join(savepath, savestr)
        fig.savefig(savestr, dpi=900, format='pdf')


def plot_floor_time(E1, E2, E3, E4, E5, E6, savefig=False, savepath=''):
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Time [ms]')
    ax.set_ylabel(r'$E$ [kJ]')
    ax.set_title('ALLPD floor beams vs. time')
    ax.minorticks_on()
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    ax.plot(E1.time * 1e3, E1.floor / 1e3, label=E1.label)
    ax.plot(E2.time * 1e3, E2.floor / 1e3, label=E2.label)
    ax.plot(E3.time * 1e3, E3.floor / 1e3, label=E3.label)
    ax.plot(E4.time * 1e3, E4.floor / 1e3, label=E4.label)
    ax.plot(E5.time * 1e3, E5.floor / 1e3, label=E5.label)
    ax.plot(E6.time * 1e3, E6.floor / 1e3, label=E6.label)

    ax.legend()
    fig.set_size_inches(8 * 1.125, 6 * 1.125)
    fig.tight_layout()

    if savefig:
        savestr = 'ALLPD_floor_vs_time' + '.pdf'
        savestr = os.path.join(savepath, savestr)
        fig.savefig(savestr, dpi=900, format='pdf')

def plot_struts_time(E1, E2, E3, E4, E5, E6, savefig=False, savepath=''):
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Time [ms]')
    ax.set_ylabel(r'$E$ [kJ]')
    ax.set_title('ALLPD floor struts vs. time')
    ax.minorticks_on()
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    ax.plot(E1.time * 1e3, E1.struts / 1e3, label=E1.label)
    ax.plot(E2.time * 1e3, E2.struts / 1e3, label=E2.label)
    ax.plot(E3.time * 1e3, E3.struts / 1e3, label=E3.label)
    ax.plot(E4.time * 1e3, E4.struts / 1e3, label=E4.label)
    ax.plot(E5.time * 1e3, E5.struts / 1e3, label=E5.label)
    ax.plot(E6.time * 1e3, E6.struts / 1e3, label=E6.label)

    ax.legend()
    fig.set_size_inches(8 * 1.125, 6 * 1.125)
    fig.tight_layout()

    if savefig:
        savestr = 'ALLPD_struts_vs_time' + '.pdf'
        savestr = os.path.join(savepath, savestr)
        fig.savefig(savestr, dpi=900, format='pdf')

def plot_stiff_skin_time(E1, E2, E3, E4, E5, E6, savefig=False, savepath=''):
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Time [ms]')
    ax.set_ylabel(r'$E$ [kJ]')
    ax.set_title('ALLPD skin and stiffeners vs. time')
    ax.minorticks_on()
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    ax.plot(E1.time * 1e3, E1.skin / 1e3 + E1.stiffeners / 1e3, label=E1.label)
    ax.plot(E2.time * 1e3, E2.skin / 1e3 + E2.stiffeners / 1e3, label=E2.label)
    ax.plot(E3.time * 1e3, E3.skin / 1e3 + E3.stiffeners / 1e3, label=E3.label)
    ax.plot(E4.time * 1e3, E4.skin / 1e3 + E4.stiffeners / 1e3, label=E4.label)
    ax.plot(E5.time * 1e3, E5.skin / 1e3 + E5.stiffeners / 1e3, label=E5.label)
    ax.plot(E6.time * 1e3, E6.skin / 1e3 + E6.stiffeners / 1e3, label=E6.label)

    ax.legend()
    fig.set_size_inches(8 * 1.125, 6 * 1.125)
    fig.tight_layout()

    if savefig:
        savestr = 'ALLPD_stiffskin_vs_time' + '.pdf'
        savestr = os.path.join(savepath, savestr)
        fig.savefig(savestr, dpi=900, format='pdf')