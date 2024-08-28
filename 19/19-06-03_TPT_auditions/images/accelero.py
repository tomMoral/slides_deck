import numpy as np
import matplotlib.pyplot as plt
from db_marche import Database


def plot_signal(X, ax=None, xlim=(250, 1900)):
    X = X - X.mean(axis=0)

    # scale = np.array([[1, 1, 1, np.pi, np.pi, np.pi]])
    # if X[:, 3].std() > 50:
    scale = np.array([[1, 1, 1, 180, 180, 180]])

    X /= scale
    offset = np.arange(6)[None] * 5

    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(X - offset)
    ax.set_xlim(xlim)
    ax.set_ylim((-30, 6))
    ax.set_ylabel("Vitesse angulaire / Acceleration", fontsize=20)
    ax.set_xlabel("Temps [sec]", fontsize=20)

    # ax.set_xticks([xlim[1]])
    # ax.set_xticklabels([f"{xlim[1] / 100:.0f} sec"], fontsize=18)
    ax.set_xticks([])
    ax.set_yticks([])

    return ax


def plot_steps(ax, steps):
    ylim = ax.get_ylim()
    print(ylim)
    steps = np.array(steps)
    ax.vlines(steps.flatten(), *ylim, linestyle='--')
    ax.set_ylim(ylim)
    for step in steps:
        ax.fill_between(step, [ylim[0]] * 2, [ylim[1]] * 2, alpha=.2,
                        color='C0')


if __name__ == "__main__":

    db = Database()
    ex = db.get_data(limit=50, atteinte='T', seed=9)[25]

    ax = plot_signal(ex.data_earth[:6].T)
    plt.tight_layout()
    plt.savefig("accelero")
    plot_steps(ax, ex.steps_annotation[0])
    plt.savefig("accelero_steps")

    # ex = db.get_data(limit=1, atteinte='LER', scoreclinique='<10', seed=42,
    #                  sensor='Xsens')[0]
    # ex = db.get_data(limit=1, atteinte='LCA', scoreclinique='>80', seed=42,
    #                  sensor='Xsens')[0]

    # ax = plot_signal(ex.data_earth[:6].T, xlim=(500, 2100))  # (600, 2760))
    # ax.set_title("Ligaments Croisés Antérieurs", fontsize=32)
    # plt.tight_layout()
    # plt.savefig("accelero_ler")
    # plot_steps(ax, ex.steps_annotation[0])
    # plt.savefig("accelero_ler_steps")

    # Plot 3 steps for the vertical acceleration (to create accelero_dict)
    fig, ax = plt.subplots(figsize=(2, 2), linewidth=3)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_ylim(-5, 5)
    [i.set_linewidth(3) for i in ax.spines.values()]
    fig.patch.set_alpha(0)
    plt.tight_layout()
    for i, s in enumerate([3, 6, 10]):
        start, end = ex.steps_annotation[0][s]
        X = ex.data_earth[2, start - 10:end + 10] - ex.data_earth[2].mean()
        lines = ax.plot(X, 'C2', linewidth=3)
        ax.set_xlim((0, 20 + end - start))

        plt.savefig(f"step{i}")
        lines[0].remove()
    plt.show()
