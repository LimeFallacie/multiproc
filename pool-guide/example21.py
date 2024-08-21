# SuperFastPython.com
# example of an argument that does not pickle
from time import sleep
from multiprocessing import Pool

# custom function executed in another process
def task(file):
    # write to the file
    file.write('hi there')
    return 'all done'

# protect the entry point
if __name__ == '__main__':
    # open the file
    with open('tmp.txt', 'w') as file:
        # start the process pool
        with Pool() as pool:
            # issue the task
            result = pool.apply_async(task, file)
            # get the result
            value = result.get()
            print(value)
