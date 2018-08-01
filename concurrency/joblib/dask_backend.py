import dask_ml.joblib  # registers joblib plugin
from dask.distributed import Client

# client = Client(processes=False)             # create local cluster
client = Client("tcp://192.168.0.28:8786")  # or connect to remote cluster

from joblib import Parallel, parallel_backend, delayed

"""
setup dask cluster with SSH:http://dask.pydata.org/en/latest/setup/ssh.html

notes: paramiko, lz4

setup authrization without password:

ssh-keygen -t rsa
cat .ssh/id_rsa.pub | ssh roo@192.168.0.23 'cat >> .ssh/authorized_keys'


"""

import numpy as np
import random

def worker():
    while True:
         np.hamming(random.randint(1,100000))


with parallel_backend('dask'):
    with Parallel(n_jobs=200) as parallel:
        accumulator = 0.
        n_iter = 0
        while accumulator < 1000000:
            results = parallel(delayed(worker)() for i in range(50000))
            accumulator += sum(results)  # synchronization barrier
            n_iter += 1
    print(accumulator, n_iter)