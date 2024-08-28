import matplotlib.pyplot as plt
from db_marche import Database


db = Database()
ex = db.get_data(limit=10, atteinte='T', seed=42)[0]

fig = plt.figure()
fig.patch.set_alpha(0)
fig.set_size_inches(12, 6)
s = 100
for i in range(6):
    if i == 3:
        s /= 60
    plt.plot(s * ex.D[i, ex.seg_annotation[0]:ex.seg_annotation[3]] - 850 * i)
plt.xticks([])
plt.yticks([])
plt.xlabel("Time [s]")
plt.ylabel("Acceleration/Angular Velocity")
plt.tight_layout()
plt.savefig("../../communications/misc/17_10_prez-edmh/images/accelero.pdf",
            dpi=150)

plt.show()
