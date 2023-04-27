import numpy as np
import matplotlib.pyplot as plt

np.random.seed(27)
N = 100
alpha = 3
rho = .2
X = np.random.rand(N)
X = np.linspace(0, 1, N)
Z = .8 * np.random.randn(N)
noise = 2*(np.random.rand(N) > rho) - 1
Y = alpha * X + Z
classes = (Z*noise > 0).astype(int)
plt.scatter(X, Y, c=[f"C{c}" for c in classes])
ylim = plt.ylim()

lines = plt.plot(X, alpha*X, 'k')
c0 = plt.fill_between([0, 1], [ylim[0], ylim[0]], [0, alpha], color='C0',
                      alpha=.4)
c1 = plt.fill_between([0, 1], [ylim[1], ylim[1]], [0, alpha], color='C1',
                      alpha=.4)
plt.ylim(ylim)

plt.xticks([])
plt.yticks([])
plt.xlim(-.01, .95)
plt.tight_layout()
plt.savefig("Linear_model")

lines[0].remove()
c0.remove()
c1.remove()

pfx, px, py = 0, 0, 0
nfx, nx, ny = 0, 0, 0
line = [(px, py)]
idx = X.argsort()
last_c = 0
x_off, y_off = .005, .1
for i in idx:
    c = classes[i]
    if c != last_c or i == idx[-1]:
        last_c = c
        if c:
            line += [(pfx-x_off, py - y_off), (px+x_off, py - y_off)]
            pfx, px, py = X[i], X[i], Y[i]
        else:
            line += [(nfx - x_off, ny + y_off), (nx+x_off, ny + y_off)]
            nfx, nx, ny = X[i], X[i], Y[i]
    elif c:
        px, py = X[i], min(py, Y[i])
    else:
        nx, ny = X[i], max(ny, Y[i])

line = np.array(line)[5:].T
plt.plot(line[0], line[1], 'k')

plt.savefig("Overfit")
