import numpy as np
import matplotlib.pyplot as plt
from db_marche import Database


db = Database()
ex = db.get_data(limit=1, atteinte='T', seed=42)[0]

fig = plt.figure()
fig.patch.set_alpha(0)
fig.set_size_inches(12, 6)
# s = 100
# for i in range(6):
#     if i == 3:
#         s /= 60
#     plt.plot(s * ex.D[i, ex.seg_annotation[0]:ex.seg_annotation[3]] - 850 * i)
X = ex.DAZ.T[350:]
t = np.arange(len(X)) / 100
plt.plot(t, X)
plt.xlim(0, t[-1])
plt.ylim(-7, 7)
# plt.xticks([])
# plt.yticks([])
plt.xlabel("Time [s]", fontsize="xx-large")
plt.ylabel("Acceleration [m/s$^2$]", fontsize="xx-large")
plt.tight_layout()
plt.savefig("accelero.pdf", dpi=150)

plt.show()
