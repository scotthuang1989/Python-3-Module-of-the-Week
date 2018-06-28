"""
Executors work as context managers, 
running tasks concurrently and waiting for them all to complete. 
When the context manager exits, the shutdown() method of the executor is called.
"""

from concurrent import futures


def task(n):
    print(n)


with futures.ThreadPoolExecutor(max_workers=2) as ex:
    print('main: starting')
    ex.submit(task, 1)
    ex.submit(task, 2)
    ex.submit(task, 3)
    ex.submit(task, 4)

print('main: done')
