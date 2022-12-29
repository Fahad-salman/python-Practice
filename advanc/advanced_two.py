# Comprehensions 

listOne = []
for i in 'Hello World!':
    listOne.append(i)
# print(listOne)

# or we can just do it in one line 

myList = [char for char in 'Hello World']
# print(myList)

# very simple  
# let's do more examples
# question -> insert value into list fron 0 to 100

myList1 = [num for num in range(0,101)]
# print(myList1)

# do like previous example but multiply by 2

myList2 =[num*2 for num in range(0,101)]
# print(myList2)

# question -> do like previous but only print even number

myList3 =[num*2 for num in range(0,101) if num % 2 == 0]
# print(myList3)

# also we can do it with set and dictionary

mySet = {num*2 for num in range(0,101) if num % 2 != 0}
# print(mySet)

otherDict ={
    'a': 1,
    'b': 2 ,
    'c': 3 ,
}
myDict = {key:value**2 for key,value in otherDict.items() if value % 2 != 0}
# print(myDict)

myDict2 ={num: num**2 for num in [1,2,3,4]}
# print(myDict2)