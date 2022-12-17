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

# ===================

newBasket = [
    'phone',
    'Tv',
    'Water',
    'Bag',
]

# index can take three vale and will tell you where is it in the list,
# first vale thing that you want to find into the list ,
# second vale start from index you intered ,
# third value stop on the index you intered
print(newBasket.index('Tv'))

# if locking for any word from the list , you can use (in)
# and will tell if the word you locking for is on the list will return True , if not found it will return False 
# (" bty not only in list ")
print('Tv' in newBasket)

# you can count the word in the list by using List.count
print(newBasket.count('Water'))

# you can sort your lists by using List.sort() or sorted(listName)
# list.reverse()

#you can copy the list by using List.copy()

# you can gnareate a list by using range()
print(list(range(101)))

# join will insert your text into the current text
text = '*'
editText = text.join(['Hello','im','Fahad'],)
print(editText)
# or you can write like this
article = ' '.join(['<Hello','im','Fahad>'])
print(article)

# list unpacking 

a,b,c,*other = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(b)
print(c)
# what if we want print the rest of them type *other
print(other)