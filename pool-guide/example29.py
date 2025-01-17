# SuperFastPython.com
# example of showing progress in the process pool with separate tasks
from time import sleep
from random import random
from multiprocessing.pool import Pool

# progress indicator for tasks in the process pool
def progress(results):
    print('.', end='', flush=True)

# task executed in a worker process
def task():
    # generate a random value
    value = random()
    # block for a moment
    sleep(value)

# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue many tasks asynchronously to the process pool
        results = [pool.apply_async(task, callback=progress) for _ in range(20)]
        # close the pool
        pool.close()
        # wait for all issued tasks to complete
        pool.join()
    # report all done
    print('\nDone!')
