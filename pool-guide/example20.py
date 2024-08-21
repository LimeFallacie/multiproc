# SuperFastPython.com
# example of a callback function for apply_async()
from time import sleep
from multiprocessing.pool import Pool

# result callback function
def handler():
    print(f'Callback got: {result}', flush=True)

# custom function executed in another process
def task():
    # block for a moment
    sleep(1)
    return 'all done'

# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks to the process pool
        result = pool.apply_async(task, callback=handler)
        # get the result
        value = result.get()
        print(value)
