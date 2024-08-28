import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
sns.set_style("darkgrid")

fig = plt.figure(figsize=(8, 6))
fig.patch.set_alpha(0)
ax = plt.subplot(111)
# ax.set_aspect("equal")

theta = 30
w, h = (10, 2)
xy = (0, 0)

y_lim = np.array([-11, 11])
x_lim = 4 * y_lim / 3

# Set ticks and draw axis
ticks = np.arange(-21, 21, 3)
plt.xticks(ticks, [])
plt.yticks(ticks, [])
plt.hlines(0, *x_lim)
plt.vlines(0, *y_lim)

# Set limits for the plot
plt.xlim(x_lim)
plt.ylim(y_lim)

# Draw the original quadratic form
for w, h in [(30, 6), (25, 5), (20, 4)]:
    ell = Ellipse(xy=xy, width=w, height=h,
                  angle=theta, color='black')
    ell.set_facecolor('none')
    ax.add_artist(ell)

# Save the first figure
plt.tight_layout()
plt.savefig("ell1.pdf", dpi=150)

# Add the isotropic approximation
circ = Ellipse(xy=xy, width=4, height=4, angle=0, color="red", linewidth=2)
circ.set_facecolor('none')
ax.add_artist(circ)

# Save the second figure
plt.savefig("ell2.pdf", dpi=150)

vline = plt.vlines(0, 0, 2.3, linewidth=5, color='g')
hline = plt.hlines(0, 0, 3.75, linewidth=5, color='g')

# Save the fourth figure
plt.savefig("ell4.pdf", dpi=150)

# Clean up unneeded features
vline.remove()
hline.remove()
circ.remove()

# Remove the circle and add the non isotropic approx + deformed axis
ell = Ellipse(xy=xy,
              width=8, height=3,
              angle=theta / 3, color='blue', linewidth=2)
ell.set_facecolor('none')
ax.add_artist(ell)
plt.plot(np.cos(np.pi * theta / 540) * x_lim,
         np.sin(np.pi * theta / 540) * y_lim,
         "g--")
plt.plot(np.sin(np.pi * theta / 540) * 2 * x_lim,
         -np.cos(np.pi * theta / 540) * 2 * y_lim,
         "g--")

# Save third figure
plt.savefig("ell3.pdf", dpi=150)
plt.show()
