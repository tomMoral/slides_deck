import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from alphacsc.utils.convolution import construct_X

import matplotlib as mpl

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble'] = [r"\usepackage{amsbsy}"]


n_times = 3000
n_times_atom = 400
n_atoms = 1
n_trials = 1
n_times_valid = n_times - n_times_atom + 1

z = np.array([
    sparse.random(n_atoms, n_times_valid, density=5. / n_atoms / n_times_valid,
                  random_state=274).toarray() for _ in range(n_trials)
])

z = np.swapaxes(z, 0, 1)
z[z != 0] = np.maximum(z[z != 0], 0.5)

t = np.arange(n_times_atom) / 50.
ds = np.c_[np.hanning(n_times_atom) * np.sin(t * 1.5 + np.cos(t * 1.5))].T

X = construct_X(z, ds)

######################
fig = plt.figure(figsize=(9, 4))
axes = []
for i in range(2):
    axes.append(plt.subplot2grid((2, 7), (i, 0), colspan=7, fig=fig))


def final():
    ylim = (-.9, 1)
    ax = plt.subplot2grid((2, 7), (0, 0), colspan=7, fig=fig)
    ax.plot(X.T, color='C0')
    # ax.plot(X.T[:t0 + 400], color='C0')
    ax.set_xlim(0, 1750)
    ax.set_ylim(ylim)
    ax.set_xticks([], [])
    ax.set_yticks([], [])
    ax.set_ylabel(r"$x^n$", fontsize=26, rotation=0, labelpad=20,
                  verticalalignment='center')

    ax = plt.subplot2grid((2, 7), (1, 5), colspan=2, fig=fig)
    ax.plot(ds.T, color='C1')
    ax.set_ylabel(r"$*d_1$", fontsize=26, rotation=0, labelpad=20,
                  verticalalignment='center')
    ax.set_xlim(0, ds.shape[1])
    ax.set_ylim(ylim)
    ax.set_xticks([], [])
    ax.set_yticks([], [])

    ax = plt.subplot2grid((2, 7), (1, 0), colspan=5, fig=fig)
    ax.plot(z[0, 0], color='C2')
    ax.set_ylabel(r"$z_1^n$", fontsize=26, rotation=0, labelpad=20,
                  verticalalignment='center')

    ax.set_xlim(0, 1750)
    ax.set_ylim(ylim)
    ax.set_xticks([], [])
    ax.set_yticks([], [])

    plt.tight_layout()


def update(t):

    ylim = (-.9, 1)
    t0 = int(t * 30)
    ax = axes[0]
    ax.cla()
    ax.plot(X.T, color='C0')
    # ax.plot(X.T[:t0 + 400], color='C0')
    ax.set_xlim(0, 1750)
    ax.set_ylim(ylim)
    ax.set_xticks([], [])
    ax.set_yticks([], [])
    ax.set_ylabel(r"$x^n$", fontsize=26, rotation=0, labelpad=20,
                  verticalalignment='center')

    ######################
    ax = axes[1]
    ax.cla()
    ax.plot(np.convolve(z[0, 0, :t0], ds[0]), color='C0')
    ax.plot(z[0, 0], color='C2')
    ax.plot(range(t0, t0 + ds.shape[1]), ds.T, color='C1')
    ax.set_ylabel(r"$z_1^n$", fontsize=26, rotation=0, labelpad=20,
                  verticalalignment='center')

    ax.set_xlim(0, 1750)
    ax.set_ylim(ylim)
    ax.set_xticks([], [])
    ax.set_yticks([], [])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser('')
    parser.add_argument('--gif', action="store_true",
                        help='')
    parser.add_argument('--prez', action="store_true",
                        help='')
    args = parser.parse_args()

    if args.gif:
        anim = FuncAnimation(fig, update, frames=range(1, 45), interval=150)

        ######################
        plt.tight_layout()
        anim.save('intro_csc.gif', dpi=150, writer='imagemagick')
        plt.show()

    if args.prez:

        update(216.5 / 30)
        plt.tight_layout()
        fig.savefig("intro_csc_2")

        update(782 / 30)
        fig.savefig("intro_csc_3")

        update(1100 / 30)
        fig.savefig("intro_csc_4")

        # Only display the dictionary
        ax = axes[1]
        ax.cla()
        t0 = 500
        ax.plot(range(t0, t0 + ds.shape[1]), ds.T, color='C1')

        ax.set_xlim(0, 1750)
        ax.set_ylim((-.9, 1))
        ax.set_xticks([], [])
        ax.set_yticks([], [])
        ax.set_ylabel(r"$d_1$", fontsize=26, rotation=0, labelpad=20,
                      verticalalignment='center')
        plt.savefig("intro_csc_1")

        ax.remove()
        plt.savefig("intro_csc_0")

        final()
        fig.savefig("intro_csc_5")
