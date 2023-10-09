import numpy as np
import matplotlib.pyplot as plt


def prob_gauss(mu, sigma, xlim):
    t = np.linspace(*xlim, 10000)
    p = np.exp(-.5*((t - mu) / sigma)**2) / (np.sqrt(2*np.pi)*sigma)
    return t, p


if __name__ == '__main__':

    xlim = (-2, 4)
    mu0 = 0
    mu1 = 1
    for n in [10, 50, 200]:
        fig = plt.figure()
        sigma = 5 / np.sqrt(n)
        t1, p1 = prob_gauss(mu1, sigma, xlim)
        t0, p0 = prob_gauss(mu0, sigma, xlim)

        plt.plot(t0, p0)
        plt.plot(t1, p1)

        idx = (np.cumsum(p0) > .95*np.sum(p0)).argmax()
        pval = t0[idx]

        ylim = plt.ylim()
        plt.vlines(pval, *ylim, linestyle='--')
        plt.ylim(ylim)

        plt.fill_between(t0[idx:], p1[idx:], color='r')
        plt.fill_between(t0[idx:], p0[idx:], color='g')
        plt.text(pval - 1, .01, "p-value", fontsize=16, color='g')
        plt.text(min(pval + 1, 3.2), .5 * p0.max(), "power", fontsize=16,
                 color='r')

        if n == 50:
            plt.text(-2, .35, "$p(y|H0)$", fontsize=16)
            plt.text(2.5, .35, "$p(y|H1)$", fontsize=16)

        plt.title(f"n_samples = {n}", fontsize=28)
        plt.tight_layout()

        plt.savefig(f"sample_size_{n}")
    plt.show()
