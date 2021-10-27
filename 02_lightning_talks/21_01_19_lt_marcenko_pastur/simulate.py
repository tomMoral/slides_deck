import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# activate latex text rendering
rc('text', usetex=True)


if __name__ == "__main__":

    sig = 1
    n_hist = 3
    max_iter = 5000

    list_m = np.logspace(2, 3, n_hist, dtype=int)

    vals, e_min, e_max = {}, {}, {}
    for alpha in [0.25, 1, 4]:
        vals[alpha], e_min[alpha], e_max[alpha] = {}, {}, {}

        # Simulate distributions
        for m in list_m:
            n = int(m / alpha)

            vals[alpha][m], e_min[alpha][m], e_max[alpha][m] = [], [], []
            for i in range(max_iter):
                print(f'iteration m={m}, n={n}: {i / max_iter:6.1%}\r',
                      end='', flush=True)
                X = sig * np.random.randn(m, n)
                Y = X.dot(X.T) / n
                e, _ = np.linalg.eigh(Y)

                vals[alpha][m].extend(e)
                e_min[alpha][m].append(min(e[abs(e) > 1e-10]))
                e_max[alpha][m].append(max(e))
            print(f'iteration m={m}, n={n}: {"done":6}')

        # Setup plot
        fig = plt.figure()
        spec = plt.GridSpec(
            ncols=2, nrows=3, height_ratios=(0.1, 0.45, 0.45),
            figure=fig
        )
        ax_full = fig.add_subplot(spec[1, :])
        ax_min = fig.add_subplot(spec[2, 0])
        ax_max = fig.add_subplot(spec[2, 1])

        # Marchenko-Pastur constants and density
        l_min = (sig * (1 - np.sqrt(alpha))) ** 2
        l_max = (sig * (1 + np.sqrt(alpha))) ** 2
        t = np.linspace(l_min, l_max, 1000)
        nu = np.sqrt((l_max - t) * (t - l_min)) / (2 * np.pi * alpha * t)

        # Plot histograms
        bins = 100
        bins_min, bins_max = bins, bins
        for c, m in enumerate(list_m):
            ax_full.hist(
                vals[alpha][m], bins=bins, color=f'C{c}',
                alpha=0.5, density=True
            )
            _, bins_min, _ = ax_min.hist(
                np.array(e_min[alpha][m]) - l_min, bins=bins_min,
                alpha=0.5, density=True
            )
            _, bins_max, _ = ax_max.hist(
                np.array(e_max[alpha][m]) - l_max, bins=bins_max,
                alpha=0.5, density=True
            )

        # Plot density function
        ax_full.plot(t, nu, color='k')
        ax_full.set_title(r"Eigenvalues $\lambda$")
        if alpha == 4:
            ax_full.set_ylim(0, .3)

        # Plot theoretical values
        for ax, title in [(ax_min, r'$\lambda_{min} - \lambda_-$'),
                          (ax_max, r'$\lambda_{max} - \lambda_+$')]:
            ylim = np.array(ax.get_ylim())
            ax.vlines(0, *ylim, color='k', ls='--')
            ax.set_ylim(ylim)
            ax.set_title(title)

        ax_legend = fig.add_subplot(spec[0, :])
        leg = ax_legend.legend(
            [plt.Rectangle((0, 0), 1, 1, color=f'C{c}', alpha=0.5)
             for c in range(len(list_m))],
            [f'{n}' for n in list_m], loc='center',
            bbox_to_anchor=(0, 0, 1, 1), ncol=len(list_m),
            title=r'\textbf{\underline{Sample size $n$}}'
        )
        leg._legend_box.align = "left"
        ax_legend.set_axis_off()

        plt.tight_layout()
        plt.savefig(f'marchenko_pastur_alpha={alpha}.pdf', dpi=300)
        plt.pause(0)
    plt.show()
