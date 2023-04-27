import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
sns.set_style("darkgrid")

fig = plt.figure()
fig.patch.set_alpha(0)
fig.set_size_inches(6, 6)
ax = plt.subplot(111)
ax.set_aspect("equal")

theta = 30
w, h = (10, 2)
xy = (0, 0)

t_lim = np.array([-10, 13])

for w, h in [(15, 3), (10, 2), (5, 1)]:
    ell = Ellipse(xy=xy, width=w, height=h,
                  angle=theta, color='black')
    ell.set_facecolor('none')
    ax.add_artist(ell)
t = np.linspace(-10, 10, 9)
plt.xticks(t, [])
plt.yticks(t, [])
plt.hlines(0, t_lim[0], t_lim[1])
plt.vlines(0, t_lim[0], t_lim[1])
plt.xlim(t_lim)
plt.ylim(t_lim)
plt.tight_layout()
plt.savefig("ell1.png", dpi=150)
circ = Ellipse(xy=xy, width=15, height=15, angle=0, color="red")
circ.set_facecolor('none')
ax.add_artist(circ)
plt.savefig("ell2.png", dpi=150)
circ.remove()
ell = Ellipse(xy=xy,
              width=19, height=8,
              angle=theta / 3, color='blue')
ell.set_facecolor('none')
ax.add_artist(ell)
t = t_lim
plt.plot(np.cos(np.pi * theta / 540) * t, np.sin(np.pi * theta / 540) * t, "g--")
plt.plot(np.sin(np.pi * theta / 540) * 2 * t,
         -np.cos(np.pi * theta / 540) * 2 * t,
         "g--")
plt.savefig("ell3.png", dpi=150)
plt.show()

