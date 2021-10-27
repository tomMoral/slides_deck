import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
fig.patch.set_alpha(0)
fig.set_size_inches(12, 6)
t = np.arange(1000) / 1000 * 3
f1 = t
f2 = np.sin(4 * np.pi * t)
plt.plot(t, f1 * 3, t, f2)
plt.xlabel("Time [s]", fontsize="xx-large")
plt.xticks([0, 1, 2, 3])
plt.yticks([])
plt.tight_layout()
plt.tight_layout()
plt.savefig("temporal.png")
