# SuperFastPython.com
# example of waiting for all tasks in a batch to finish
from time import sleep
from multiprocessing.pool import Pool

# task executed in a worker process
def task(identifier):
    # block for a moment
    sleep(0.5)
    # report done
    print(f'Task {identifier} done', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks into the process pool
        result = pool.map_async(task, range(10))
        # wait for tasks to complete
        result.wait()
        # report all tasks done
        print('All tasks are done', flush=True)
    # process pool is closed automatically
