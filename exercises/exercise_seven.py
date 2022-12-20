# Exercise 7 questions => (Take list of numbers then print highest even number )

def highest_even(get_list):
    list_evens=[] # This list for even numbers 
    for items in get_list: 
        if items % 2 == 0:
            if items not in list_evens: # To check there is no duplicate value
                list_evens.append(items) # Add even numbers to list
    highest_even = max(list_evens) # Take max number == highest number
    print(f'highest even nuber is {highest_even}') # Here we go this the answer 

highest_even([5,6,100,7,9,8,10,20,80])