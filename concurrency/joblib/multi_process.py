"""
joblib can't leverage Queue to share data between workers.
"""

import numpy as np
import random
from joblib import Parallel, delayed

import multiprocessing as mp

myqueue = mp.Queue()

def worker(testqueue):
    np.hamming(random.randint(1,100000))



with Parallel(n_jobs=2) as parallel:
    accumulator = 0.
    n_iter = 0
    while accumulator < 10:
        results = parallel(delayed(worker)(myqueue) for i in range(50))
        accumulator += sum(results)  # synchronization barrier
        n_iter += 1
print(accumulator, n_iter)