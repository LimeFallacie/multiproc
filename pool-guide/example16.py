# SuperFastPython.com
# example of not having a check for the main top-level environment
from time import sleep
from multiprocessing import Pool

# custom task that will sleep for a variable amount of time
def task(value):
    # block for a moment
    sleep(1)
    return value

# start the process pool
with Pool() as pool:
    # submit all tasks
    for result in pool.map(task, range(5)):
        print(result)
