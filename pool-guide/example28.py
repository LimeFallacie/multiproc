# SuperFastPython.com
# example of issuing a follow-up task automatically with a result callback
from random import random
from time import sleep
from multiprocessing.pool import Pool

# handle results of the task (in the main process)
def result_callback(result_iterator):
    # unpack result
    for i,v in result_iterator:
        # check result
        if v > 0.5:
            # issue a follow-up task
            _ = pool.apply_async(task2, args=(i, v))

# task executed in a worker process
def task2(identifier, result):
    # generate a random number
    value = random()
    # block for a moment
    sleep(value)
    # report result
    print(f'>>{identifier} with {result}, generated {value}', flush=True)
    # return result
    return (identifier, result, value)

# task executed in a worker process
def task1(identifier):
    # generate a random number
    value = random()
    # block for a moment
    sleep(value)
    # report result
    print(f'>{identifier} generated {value}', flush=True)
    # return result
    return (identifier, value)

# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks asynchronously to the process pool
        result = pool.map_async(task1, range(10), callback=result_callback)
        # wait for issued tasks to complete
        result.wait()
        # close the pool
        pool.close()
        # wait for all issued tasks to complete
        pool.join()
    # all done
    print('All done.')
