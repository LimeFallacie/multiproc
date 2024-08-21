# SuperFastPython.com
# example of handling an exception raised within a task in the caller
from time import sleep
from multiprocessing.pool import Pool

# task executed in a worker process
def task():
    # block for a moment
    sleep(1)
    # fail with an exception
    raise Exception('Something bad happened!')
    # unreachable return value
    return 'Never gets here'

# protect the entry point
if __name__ == '__main__':
    # create a process pool
    with Pool() as pool:
        # issue a task
        result = pool.apply_async(task)
        # get the result
        try:
            value = result.get()
            # report the result
            print(value)
        except Exception:
            print('Unable to get the result')
