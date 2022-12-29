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
print(myList3)