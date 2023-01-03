import random

my_list = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8', 'name9']
# help(random.randint)
print(random.randint(1,15))
print(random.choice(my_list))
random.shuffle(my_list)
print(my_list)