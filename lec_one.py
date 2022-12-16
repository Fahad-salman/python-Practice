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

slice string

randomText = 'Here You can print any word from here let/'s look How we do this'
    so start from zero to whatever in your statement
    print(randomText[0])
    The number you insert , python will search in Your statement
    here 0 == H in your statement
    print(randomText[9])
    here 9 == c in your statement
    [start] => will take one value 
    [start:stop] => will take first value until second you enterd
    [start:stop:stepover] => will take first value until second you enterd stepover like skip
    print(randomText[0:8:2])


    questions one:
        what will happen for this code?
        print(randomText[2:])
        answer => will print from later 2 util the end.


    questions two:
        what will happen for this code?
        print(randomText[:5])
        answer => will print from later 0 util the the value we insert.


    questions three:
        what will happen for this code?
        print(randomText[::2])
        answer => will print as a default .

    if you enter negative number will start from the end

    [::-1] will print reverse (from end to start) 

len() => length 


"""
# Exercise

currentYear = 2022
while True:
    try:
        birthYear = float(input('What year were you born ? '))
    except ValueError:
            print('Use number please')   
    else:
        break
age = currentYear-birthYear
print(f'Your age is {age} years old')

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