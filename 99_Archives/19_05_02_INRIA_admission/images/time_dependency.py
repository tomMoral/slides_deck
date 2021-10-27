import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


np.random.seed(4242)
T = 1000
nnz = 4
K = 3
i0 = np.random.choice(np.arange(int(T / 150)), nnz, replace=False) * 150
i0.sort()

Z = np.zeros((T, K))
for i in i0:
    for k in range(K):
        # i1 = i + k * 40 * (30 - 40*np.random.rand())
        Z[i + k * 50 + 50, k] = 1 + .2*np.random.randn()


offset = np.ones(shape=Z.shape) * np.arange(K)[None]
fig = plt.figure(figsize=(10, 5.73))

ax = fig.subplots()
ax.set_facecolor("#0F0F0F00")

plt.plot(Z - offset, linewidth=2)
plt.yticks([], [])
plt.xticks([], [])
plt.xlim(0, 1000)
ylim = plt.ylim()

plt.ylabel(r"Activations", fontsize=36, labelpad=5)
plt.xlabel(r"Temps", fontsize=36, labelpad=5)
plt.tight_layout()
plt.savefig('time_dependency')


style = "Simple,tail_width=0.5,head_width=8,head_length=8"
kw = dict(arrowstyle=style, color="k")

nnz0 = Z[:, 0].nonzero()[0]
nnz1 = Z[:, 1].nonzero()[0]
nnz2 = Z[:, 2].nonzero()[0]

for x0, x1, x2 in zip(nnz0, nnz1, nnz2):
    a0 = patches.FancyArrowPatch((x0, -0.1), (x1 - 5, -.9),
                                 connectionstyle="arc3,rad=.3", **kw)
    a1 = patches.FancyArrowPatch((x1, -1.1), (x2 - 5, -1.9),
                                 connectionstyle="arc3,rad=.3", **kw)
    ax.add_patch(a0)
    ax.add_patch(a1)

plt.savefig('time_dependency_arrow')


fig = plt.figure(figsize=(10, 5.73))
ax = fig.subplots()
ax.set_facecolor("#0F0F0F00")

for k in range(K):
    z = Z[:, 1] * (.8 + .3 * np.random.randn(T))
    plt.plot(z - offset[:, k], linewidth=2)

for i1 in nnz1:
    x_bounds = [i1 - 20, i1 + 20]
    y_bounds = [ylim[0] + .1, ylim[1] - .1]
    plt.fill_between(x_bounds, [y_bounds[0]] * 2, [y_bounds[1]] * 2,
                     color='k', alpha=.1)
    plt.vlines(x_bounds, *y_bounds)
    plt.hlines(y_bounds, *x_bounds)
plt.ylim(ylim)
plt.yticks([], [])
plt.xticks([], [])
plt.xlim(0, 1000)

plt.ylabel(r"Activations", fontsize=36, labelpad=5)
plt.xlabel(r"Temps", fontsize=36, labelpad=5)
plt.tight_layout()
plt.savefig('time_dependency_simultaneous')

plt.show()
