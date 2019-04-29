import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from alphacsc.utils.convolution import construct_X

import matplotlib as mpl

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble'] = [r"\usepackage{amsbsy}"]


######################
fig = plt.figure(figsize=(9, 4))
axes = []
for i in range(2):
    axes.append(plt.subplot2grid((2, 7), (i, 0), colspan=7, fig=fig))


def plot_z(ax, z, xlim, ylim):

    ax.plot(np.minimum(z[0, 0], ylim[1] * .8), color='C2')
    ax.set_ylabel(r"$z_1^n$", fontsize=26, rotation=0, labelpad=20,
                  verticalalignment='center')

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xticks([], [])
    ax.set_yticks([], [])


def final(X, ds, z, xlim, ylim):
    ax = plt.subplot2grid((2, 7), (0, 0), colspan=7, fig=fig)
    ax.plot(X.T, color='C0')
    ax.set_xlim(xlim)
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
    plot_z(ax, z, xlim, ylim)

    plt.tight_layout()


def update(t, X, ds, z, xlim, ylim):

    t0 = int(t * 30)
    ax = axes[0]
    ax.cla()
    ax.plot(X.T, color='C0')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xticks([], [])
    ax.set_yticks([], [])
    ax.set_ylabel(r"$x^n$", fontsize=26, rotation=0, labelpad=20,
                  verticalalignment='center')

    ######################
    ax = axes[1]
    ax.cla()
    d = ds[0] / np.linalg.norm(ds[0], ord=2)
    ax.plot(np.convolve(z[0, 0, :t0], d), color='C0')
    ax.plot(range(t0, t0 + ds.shape[1]), ds.T, color='C1')
    plot_z(ax, z, xlim, ylim)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser('')
    parser.add_argument('--gif', action="store_true",
                        help='')
    parser.add_argument('--prez', action="store_true",
                        help='')
    parser.add_argument('--walk', action="store_true",
                        help='')
    args = parser.parse_args()

    if args.walk:
        from db_marche import Database
        db = Database()
        ex = db.get_data(limit=50, atteinte='T', seed=9)[25]

        X_start = ex.steps_annotation[0][2][0] - 20
        X_end = ex.steps_annotation[0][4][1] + 20
        X = ex.data_earth[2, X_start:X_end] - ex.data_earth[2].mean()

        d_start, d_end = ex.steps_annotation[0][3]
        ds = ex.data_earth[2, d_start - 5:d_end + 5] - ex.data_earth[2].mean()
        ds = ds[None]

        d = ds[0] / np.linalg.norm(ds[0], ord=2)
        z = np.r_[np.correlate(X, d), np.zeros(100)]
        mask = np.zeros_like(z)
        mask[1:-1] = (z[1:-1] > z[2:])*(z[1:-1] > z[:-2])
        z = z * ((z * mask) > .9 * z.max())[None, None]

        xlim = (0, X_end - X_start)
        ylim = (-5, 5)
    else:
        n_times = 3000
        n_times_atom = 400
        n_atoms = 1
        n_trials = 1
        n_times_valid = n_times - n_times_atom + 1

        z = np.array([
            sparse.random(n_atoms, n_times_valid,
                          density=5. / n_atoms / n_times_valid,
                          random_state=274).toarray() for _ in range(n_trials)
        ])

        z = np.swapaxes(z, 0, 1)
        z[z != 0] = np.maximum(z[z != 0], 0.5)

        t = np.arange(n_times_atom) / 50.
        ds = np.c_[np.hanning(n_times_atom) *
                   np.sin(t * 1.5 + np.cos(t * 1.5))].T

        X = construct_X(z, ds)
        xlim = (0, 1750)
        ylim = (-.9, 1)

    fargs = (X, ds, z, xlim, ylim)
    t0 = (xlim[1] - ds.shape[1]) // 2

    if args.gif:
        anim = FuncAnimation(fig, update, frames=range(1, 45), interval=150,
                             fargs=fargs)

        ######################
        plt.tight_layout()
        anim.save('intro_csc.gif', dpi=150, writer='imagemagick')
        plt.show()

    if args.prez:

        for i, nnz in enumerate(z.nonzero()[2][:3]):
            update((nnz + .7) / 30, *fargs)
            plt.tight_layout()
            fig.savefig(f"intro_csc_{2 + i}")

        # Only display the dictionary
        ax = axes[1]
        ax.cla()
        ax.plot(range(t0, t0 + ds.shape[1]), ds.T, color='C1')

        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_xticks([], [])
        ax.set_yticks([], [])
        ax.set_ylabel(r"$d_1$", fontsize=26, rotation=0, labelpad=20,
                      verticalalignment='center')
        plt.savefig("intro_csc_1")
        plt.tight_layout()

        ax.remove()
        plt.savefig("intro_csc_0")

        final(*fargs)
        fig.savefig("intro_csc_5")

    plt.show()
