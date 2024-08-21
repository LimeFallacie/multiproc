# SuperFastPython.com
# example of calling submit with a function call
from time import sleep
from multiprocessing import Pool

# custom function executed in another process
def task():
    # block for a moment
    sleep(1)
    return 'all done'

# protect the entry point
if __name__ == '__main__':
    # start the process pool
    with Pool() as pool:
        # issue the task
        result = pool.apply_async(task())
        # get the result
        value = result.get()
        print(value)
