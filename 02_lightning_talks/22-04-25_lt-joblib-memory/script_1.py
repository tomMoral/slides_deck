import time
import numpy as np


from joblib import Memory
mem = Memory(location="__cache__")


@mem.cache(ignore=['verbose'])
def run_one(sigma=0.1, verbose=True):
    time.sleep(10)
    if verbose:
        print("Hello MIND!")
    return sigma * np.random.randn(10)


from joblib import Parallel, delayed

results = Parallel(n_jobs=2)(
    delayed(run_one)(sigma=sigma)
    for sigma in np.linspace(0, 1, 100)
)
