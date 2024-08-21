# SuperFastPython.com
# exception in one of many tasks issued to the process pool synchronously
from time import sleep
from multiprocessing.pool import Pool

# task executed in a worker process
def task(value):
    # block for a moment
    sleep(1)
    # check for failure case
    if value == 2:
        raise Exception('Something bad happened!')
    # report a value
    return value

# protect the entry point
if __name__ == '__main__':
    # create a process pool
    with Pool() as pool:
        # issues tasks to the process pool
        for result in pool.map(task, range(5)):
            print(result)
