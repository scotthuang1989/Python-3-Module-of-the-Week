from concurrent import futures
import threading
import time

"""
Using map() with a Basic Thread Pool¶
The ThreadPoolExecutor manages a set of worker threads, 
passing tasks to them as they become available for more work. 
This example uses map() to concurrently produce a set of results 
from an input iterable. The task uses time.sleep() to pause a different amount of time to demonstrate that, regardless of the order of execution of concurrent tasks, map() always returns the values in order based on the inputs.
"""

def task(n):
    print('{}: sleeping {}'.format(
        threading.current_thread().name,
        n)
    )
    time.sleep(n / 10)
    print('{}: done with {}'.format(
        threading.current_thread().name,
        n)
    )
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
results = ex.map(task, range(5, 0, -1))
print('main: unprocessed results {}'.format(results))
print('main: waiting for real results')
real_results = list(results)
print('main: results: {}'.format(real_results))
