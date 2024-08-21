# SuperFastPython.com
# example of an exception raised in the worker initializer function
from time import sleep
from multiprocessing.pool import Pool

# function for initializing the worker process
def init():
    # raise an exception
    raise Exception('Something bad happened!')

# task executed in a worker process
def task():
    # block for a moment
    sleep(1)

# protect the entry point
if __name__ == '__main__':
    # create a process pool
    with Pool(initializer=init) as pool:
        # issue a task
        pool.apply(task)
