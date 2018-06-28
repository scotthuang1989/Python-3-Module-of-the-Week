"""
test if share state is possible
"""

from concurrent import futures
from multiprocessing import Manager

share_list =[]

def task(n):
    print(n)
    share_list.append(n)


with futures.ThreadPoolExecutor(max_workers=2) as ex:
    print('main: starting')
    ex.submit(task, 1)
    ex.submit(task, 2)
    ex.submit(task, 3)
    ex.submit(task, 4)

print('thread test: done')
print(share_list)

# must use Manager as proxy
manager = Manager()
share_list_process =  manager.list([])


def task_p(n, t_list):
    t_list.append(n)
    return n


with futures.ProcessPoolExecutor(max_workers=2) as ex:
    print('main: starting')
    ex.submit(task_p, 5, share_list_process)
    ex.submit(task_p, 6, share_list_process)
    ex.submit(task_p, 7, share_list_process)
    ex.submit(task_p, 8, share_list_process)

print('process test: done')
print(share_list_process)
