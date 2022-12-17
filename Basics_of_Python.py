#  this single comment
"""

This multi-line comment 

Python is -> Case-Sensitive 

if you want to use a null in python write None so (None => null)

Fundamental Data Types for python

int => 1,10,100,1000

float => 1.0,10.0,100.0,1000.0

bool => True or False

str -> (String) => leatars

dict => dict

set => set

tuple => tuple

list => list

How to save a variable ?
    variable-name = whatever you need to save
    print(variable-name)
    statement = expressions

constant ?
    something you want to change
    for example => PI = 3.14 

classes => Custom classes types

Specialized Data Types:
    Special Packages Not bullet in 
    modules You can use in libraries
    We can think of it as extension


None => nothing 


to know what type of data use type('input')

    print(type(65.20)) => flot
    print(type(65)) => int
    print(type('what kind of data?')) => str


math functions:
    Google it => Python math functions.
    we will use some math functions
    round()
    abs()

To know the binary number for any thing 
  use methon bin() 
  print(bin(5)) => 101

to retreive the the binary number 
    print(int('0b101',2)) => answer is 5

Escape Sequence:
    /n => new line 
    t/ => tap 
    /" => to insert a quote 

Formatted Strings:
    name = 'John Smith'
    age = 21
    print(f'welcome {name} nice name Your age is {age} years old')
    or you can use format()
    print('Hello {0} , Your age is {1}'.format(name,age))
    0 => name , 1 => age
    start count => from zero to whatever 

len() => length 

"""




# To save a variable :
# name = "Fahad "
# age = None
# email = None
# phoneNumber = str(5)
# print(name)

# Let's use if statement

# if (name != None):
#     print(name)
# else:
#     print("name == None")
#     print(phoneNumber)

#let's make a smple loop by using range()
# for i in range(5):
#     print(name,i) 


#let's make a smple loop by using while loop
# def test_():
#     number = 1
#     while number < 10:
#         if (number == 7):
#             print('July')
#             break
#         number += 1
# test_()

# Let's make a functions

# def january():
#     return 'January'
# def february():
#     return 'February'
# def march():
#     return 'march'
# def april():
#     return 'April'
# def may():
#     return 'may'
# def june():
#     return 'June'
# def july():
#     return 'July'
# def august():
#     return 'august'
# def september():
#     return 'September'
# def october():
#     return 'October'
# def november():
#     return 'November' 
# def december():
#     return 'December'

# def last_operation():
#     five = 0
#     while five < 9:
#         if(five == 5):
#             print('yes its 5')
#             break
#         print("its 5 ?",five , "no again")
#         five +=1
# last_operation()
#  lets make an input , this input He will greet you...

#  This function will colculate any number 

# def plus(one,tow):
#     return (one+tow)

# def minus(one,tow):
#     return (one-tow)

# def multiply(one,tow):
#     return (one*tow)

# def divide(one,tow):
#     return (one/tow)

# def culculate():
#     name = input('Enter your name please : ')
#     print('welcome ',name,' i like your name')
#     while True:
#         try:
#             numberOne = float(input('enter the first number: '))
#         except ValueError:
#             print("Enter number only")
#             continue
#         else:
#             break
#     while True:
#         try:
#             numberTwo = float(input('enter the second number: '))
#         except ValueError:
#             print('enter number only')
#         else:
#             break
#     typeOperation = input('enter the type of operation: ')
#     if(typeOperation == '+' ):
#         print(numberOne, typeOperation ,numberTwo,' = ',plus(numberOne,numberTwo))
#     elif typeOperation == '-':
#         print(numberOne, typeOperation ,numberTwo,' = ',minus(numberOne,numberTwo))
#     elif typeOperation == '*' :
#         print(numberOne, typeOperation ,numberTwo,' = ', multiply(numberOne,numberTwo))
#     elif typeOperation == '/' :        
#         print(numberOne, typeOperation ,numberTwo,' = ',divide(numberOne,numberTwo))
#     else:
#         print("error: unknown type => try use one of them ( + , - , * , / )")
# culculate()
#  This function will colculate any number 