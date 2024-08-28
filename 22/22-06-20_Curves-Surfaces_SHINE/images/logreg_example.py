import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

random_state = 4242

X, y = make_classification(
    n_samples=500,
    n_features=2,
    n_classes=2,
    shuffle=0.1,
    n_informative=1,
    n_redundant=0,
    random_state=random_state,
    n_clusters_per_class=1,
)

fig = plt.figure()
plt.scatter(*X[y == 0].T)
plt.scatter(*X[y == 1].T)
for name, C, c in [("noreg", 1e10, "k"), ("reg", 1e-2, "C2")]:
    clf = LogisticRegression(C=C)
    clf.fit(X, y)

    t = np.array([X.min(axis=0)[0], X.max(axis=0)[0]])
    y_ = -(clf.coef_[0, 0] * t + clf.intercept_[0]) / clf.coef_[0, 1]
    plt.plot(t, y_, f"{c}--")
    plt.ylim(X.min(axis=0)[1] * 0.9, X.max(axis=0)[1] * 1.1)
    fig.savefig(
        f"logreg_{name}.pdf"
    )
