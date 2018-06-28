"""
The ProcessPoolExecutor works in the same way as ThreadPoolExecutor,
but uses processes instead of threads. This allows CPU-intensive operations 
to use a separate CPU and not be blocked by the CPython interpreter’s global
interpreter lock.
"""

from concurrent import futures
import os


def task(n):
    return (n, os.getpid())


ex = futures.ProcessPoolExecutor(max_workers=2)
results = ex.map(task, range(5, 0, -1))
for n, pid in results:
    print('ran task {} in process {}'.format(n, pid))

"""
If something happens to one of the worker processes to cause it to exit unexpectedly, 
the ProcessPoolExecutor is considered “broken” and will no longer schedule tasks.
"""

from concurrent import futures
import os
import signal


with futures.ProcessPoolExecutor(max_workers=2) as ex:
    print('getting the pid for one worker')
    f1 = ex.submit(os.getpid)
    pid1 = f1.result()

    print('killing process {}'.format(pid1))
    os.kill(pid1, signal.SIGHUP)

    print('submitting another task')
    f2 = ex.submit(os.getpid)
    try:
        pid2 = f2.result()
    except futures.process.BrokenProcessPool as e:
        print('could not start new tasks: {}'.format(e))
