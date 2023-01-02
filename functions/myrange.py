from time import time

def preformance(func):
    def warpper(*args, **kwargs):
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        print(f'took {time_end-time_start} milliseconds')
        return result
    return warpper

class Myrange():
    counter = 0
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if Myrange.counter < self.end:
            num = Myrange.counter
            Myrange.counter +=1
            return num
        raise StopIteration

@preformance
def fun():
    count = Myrange(0,10000)
    for i in count:
        print(i)

fun()

# @preformance
# def loop():
#     for i in range(0,10000):
#         print(i)
# loop()