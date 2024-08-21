# SuperFastPython.com
# example of the imap_unordered and use as completed usage pattern
from time import sleep
from random import random
from multiprocessing import Pool

# task to execute in a new process
def task(value):
    # generate a random value
    random_value = random()
    # block for moment
    sleep(random_value)
    # return result
    return (value, random_value)

# protect the entry point
if __name__ == '__main__':
    # create the process pool
    with Pool() as pool:
        # issue tasks and process results
        for result in pool.imap_unordered(task, range(10)):
            print(f'>got {result}')
