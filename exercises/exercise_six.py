# Exercise 6 questions => (check for doublecate value in list then print doublecate value)

words_list =[
    'a','b','c','c','d','e','f','g','h','e','a'
]

words_list.sort()
doublecate = []

for value in words_list: # here we just make a loop for list 
    if words_list.count(value) > 1: # then here we need a condition to check if doublecate or not
        # print (value)
        if value not in doublecate: # after first check , check again if exsist in second list or not
            doublecate.append(value) # add the doublecate value
print(doublecate) 

# Practice more and more for same like this case: !