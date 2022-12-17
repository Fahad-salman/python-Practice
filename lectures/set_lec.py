# set it's unordered collection of unique opjects
# in set there is no doublecate everything has to be unique 

my_set = { 'a', 'b', 'c', 'd', 'e', 'f','f','a'}
print(my_set)

# methods for set

number_set = {1,2,3,4,4,5,6,7}
second_number_set = {2,5,6,7,8,9,10,10,11,12,13}

# issubset method,
# is there a duplicate value from the first set and second set if yes will return True , if No will return False 
print(number_set.issubset(second_number_set))

# Does a first set contain everything from the second set? if yes will return True , if No will return False
print(number_set.issuperset(second_number_set),'<<<')


# intersection method
print(number_set.intersection(second_number_set))
#  short line 
print(number_set & second_number_set)

# union method , will create a new set without duplicate values
print(number_set.union(second_number_set))
# short line for union
print(number_set | second_number_set)

# isdisjoint method , do they have the same value if yes will return false , if no will return true
print(number_set.isdisjoint(second_number_set))

# difference method it will show you the difference between them
print(number_set.difference(second_number_set))
print(second_number_set.difference(number_set))

# discard will remove the value from the set
my_set.discard('f') # must be the same as in the set 
print(my_set)

# difference_update will remove duplicate value from the first set and second set
number_set.difference_update(second_number_set)
print(number_set)
