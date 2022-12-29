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
print(list(zip(firstList,otherList)),'zip()') # will not change the other 
line()
# reduce function
print(reduce(accumulateor,firstList,2),'reduce()') # will not change the other 
line()
# lembda expression
# step -> lembda pram: action we want to take , yourlist[] 
print(list(map(lambda item: item/2,firstList)),'lambda map') 
print(list(filter(lambda item: item+1,firstList)),'lambda filter') 
print(list(filter(lambda item: item % 2 != 0,firstList)),'lambda') 
print(reduce(lambda acc,item: acc+item,firstList),'reduce' ),
line()