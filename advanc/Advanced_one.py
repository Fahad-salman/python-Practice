from functools import reduce

# functions

def line():
    print('=======================================')

def mltiply_by2(number):
    return number*2

def get_odd_number(number):
    return number % 2 != 0

def accumulateor(acc,number):
    print(acc,number)
    return acc + number

# map function
firstList = [1,2,3,4]
line()
print(list(map(get_odd_number,firstList)),'map()') # will not change the other 
print(firstList)

line()
# filter function

print(list(filter(get_odd_number,firstList)),'filter()') # will not change the other 
line()
# zip function

otherList = [20,15,70]
theirList = [80,30,90]
print(list(zip(firstList,otherList,theirList)),'zip()') # will not change the other 
line()
# reduce function
print(reduce(accumulateor,firstList,-100),'reduce()') # will not change the other 
