# exercise 1 square by using lambda

myList = [5,4,3]
square = list(map(lambda item: item**2,myList))
print(square)

# exercise 2 List sorting and use zip function 

mian_list = [0,4,9,10]
second_list = [2,3,9,-1]
otherList = list(zip(mian_list,second_list))
otherList.sort(key=lambda x: x[1]) # we use lambda here to sort from the second item 
print(otherList)
