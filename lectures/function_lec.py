list_greeting=[
    'Hi','Hello','Welcome','Hola'
]
def greeting():
    for i in list_greeting:
        print(i)
greeting()


# important questions -> waht is the deffernt between arguments and parameter

# prameters -> when we define the function
def prameters_req(name,age):
    print(f'hello {name} , your age is {age}')

# positional arguments -> are used when we call the function 
name = input('enter your name : ')
age = input('enter your age : ')
prameters_req(name,age) # this the arguments name and age

# keyWord arguments

prameters_req(name=name,age=age)

# we can ser a default value in function
def say_hello(greeting='hello'):
    print(greeting)

say_hello() # if is none value will take the default value