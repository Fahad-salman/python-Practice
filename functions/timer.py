from time import time

def preformance(func):
    def warpper(*args, **kwargs):
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        print(f'took {time_end-time_start} milliseconds')
        return result
    return warpper


@preformance
def long_time():
    for i in range(10000000):
        i*5
long_time() 