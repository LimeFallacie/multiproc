# SuperFastPython.com
# example of handling an exception raised within a task
from time import sleep
from multiprocessing.pool import Pool

# task executed in a worker process
def task():
    # block for a moment
    sleep(1)
    try:
        raise Exception('Something bad happened!')
    except Exception:
        return 'Unable to get the result'
    return 'Never gets here'

# protect the entry point
if __name__ == '__main__':
    # create a process pool
    with Pool() as pool:
        # issue a task
        result = pool.apply_async(task)
        # get the result
        value = result.get()
        # report the result
        print(value)
