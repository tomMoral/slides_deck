import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
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
fig, axes = plt.subplots(nrows=2, ncols=7, figsize=(9, 4))
ax = plt.subplot2grid((2, 7), (0, 0), colspan=7)
color = 'C0'
ax.plot(X.T, color=color)
ax.set_xlim(0, 1750)
ax.set_xticks([], [])
ax.set_yticks([], [])
ax.set_ylabel(r"$x^n$", fontsize=26, rotation=0, labelpad=20,
              verticalalignment='center',
              bbox={'edgecolor': color, 'facecolor': 'none', 'linewidth': 2})

######################
color = 'C2'
ax = plt.subplot2grid((2, 7), (1, 2), colspan=5)
ax.plot(z[:1, 0].T, color=color)
z1 = ax.set_ylabel(r"$* z_1^n$", fontsize=26, rotation=0, labelpad=20,
                   verticalalignment='center', bbox={
                       'edgecolor': color, 'facecolor': 'none', 'linewidth': 2}
                   )
patch = z1.get_bbox_patch()
patch.set_height(2)
patch.set_y(-.2)
z1.set_bbox(dict(height=1.4, width=1.4))
print(patch)

ax.set_xlim(0, 1750)
ax.set_xticks([], [])
ax.set_yticks([], [])

#######################
color = 'C1'
ax = plt.subplot2grid((2, 7), (1, 0), colspan=2)
ax.plot(ds.T, color=color)
ax.set_ylabel(r"$d_1$", fontsize=26, rotation=0, labelpad=20,
              verticalalignment='center',
              bbox={'edgecolor': color, 'facecolor': 'none', 'linewidth': 2})
ax.set_xlim(0, 400)
ax.set_xticks([], [])
ax.set_yticks([], [])

######################
plt.tight_layout()
fig.savefig('intro_csc.pdf')
plt.show()
