# list section 

storCart = [
    'PlayStation 5', # 0
    'Bag', # 1
    'Headset', # 2
    'Tv', # 3
    ]
print(storCart) # will print everything in this list
print(storCart[3]) # Here will print spsefic item in this list

# you can also change the item inside from list 
storCart[0]='PC' # Likes this you change the item you want
print(storCart)

# questions 
# What if i want to copy the list then modify the new list , without change any thing in the first list ? just add ==> [:] <==

newCart = storCart[:]
newCart[1] = 'Xbox one'
print(newCart)


#  multi denominational list we call it matrex 
# example 
matrex=[
    [1,6,3], # 0 
    [7,2,0], # 1 
    [4,8,5], # 2 
]

# to print whatever inside matrex list just add [][] 
print(matrex[0][1]) # here will print 6 because i say matrex go to list number 0 then go to item 1 
print(matrex[0][2]) # here will print 3
print(matrex[2][2]) # here will print 5

basket =[1,2,3,4,5]

# add value to list list.append() , list.insert() , list.extand([])

basket.append(101) # append will add the value in end of list/
print(basket) 
basket.insert(4,103) # insert will add the value into the index you selected 
print(basket) 
basket.extend([888,999,444]) # extend will add the (values) in end of list 
print(basket) 

# remove value from list  , list.pop() , list.remove(need a value) , list.clear() 
basket.pop() # default pop will remove the list index from the list and you can retreive the index you remove , and you can chose the index you want to remove
print(basket) 
basket.remove(3) # remove must have a value = index that you want to remove
print(basket)
basket.clear() # clear will remove everything from the list
print(basket)