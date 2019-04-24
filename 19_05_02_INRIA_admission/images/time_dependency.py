import numpy as np
import matplotlib.pyplot as plt


np.random.seed(4242)
T = 1000
nnz = 4
K = 3
i0 = np.random.choice(np.arange(int(T/ 150)), nnz, replace=False) * 150
i0.sort()

Z = np.zeros((T, K))
for i in i0:
    for k in range(K):
        i1 = i + k * 40 * (30 - 40*np.random.rand())
        Z[i +k*100+10, k] = 1 + .2*np.random.randn()


offset = np.ones(shape=Z.shape) * np.arange(3)[None]
fig = plt.figure(figsize=(10, 5.73))

ax = fig.subplots()
ax.set_facecolor("#0F0F0F00")

plt.plot(Z-offset)
plt.yticks([], [])
plt.xticks([], [])
plt.xlim(0, 1000)

plt.ylabel(r"$Z$", fontsize=42, rotation=0, labelpad=25,
           verticalalignment='center')
plt.tight_layout()
plt.savefig('time_dependency')
