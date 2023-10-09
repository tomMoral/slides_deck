import numpy as np
import matplotlib.pyplot as plt


sfreq = 50

rng = np.random.RandomState(42)
t = -np.log(rng.rand(20)).cumsum()
tt = (t * sfreq // 1).astype(int)
T_max = int(np.ceil(t.max()))
z = np.zeros(T_max * sfreq)
z[tt] = 1
N = z.cumsum()

plt.stem(t, 4 * np.ones_like(tt), basefmt="C0", label="Events $\{t_k\}$")
plt.hlines(0, 0, T_max, "C0")
plt.plot(np.arange(T_max * sfreq) / sfreq, N, "C1", label="Counting process $N$")
plt.plot(np.arange(T_max + 1), "k--")
plt.yticks([0, 5, 10, 15, 20])
plt.legend()
plt.xlim(0, T_max)

plt.savefig("point_process.pdf")

