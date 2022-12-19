# Iterable 

user ={
    'name':'Ronaldo',
    'age':36,
    'isFotball_player':True,
}

for item in user.items():
    # we can unpacking the tuple
    keyy , valuee = item
    print(keyy ,'=>',valuee,'<items>')


    # short hand to do this replace item to (key any name , value)
for key , value in user.items():
    # we can unpacking the tuple
    # key , value = item
    print(key ,'=>',value,'<Short hand>')


for item in user.keys():
    print(item,'<key>')

for item in user.values():
    print(item,'<value>')


# fon in range

for _ in range(4):
    print(list(range(4)))

# smple exercise 
for i,index in enumerate(list(range(61))):
    if index == 50:
        print(f"index = {index} ")
    else:
        print("else") 

# while loop 
num = 0
while num < 8:
    num += 1
    # continue # will let you start from the beginning
    print(num)
    # break 
    # pass # as a placeholder 