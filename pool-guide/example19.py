# SuperFastPython.com
# example of calling map without an iterable
from time import sleep
from multiprocessing import Pool

# custom function executed in another process
def task(value):
    # block for a moment
    sleep(1)
    return 'all done'

# protect the entry point
if __name__ == '__main__':
    # start the process pool
    with Pool() as pool:
        # issue all tasks
        for result in pool.map(task):
            print(result)
