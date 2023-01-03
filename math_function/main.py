# import operations
from operations import *
# we can import many different ways to import


name = str(input('Welcome , enter your username : '))
print(f'Hello {name} hope you enjoy...')
value_one = float(input('enter a number : '))
value_two = float(input('enter a number : '))

print(f'{value_one} X {value_two} equal',multiply(value_one,value_two))
print(f'{value_one} ÷ {value_two} equal',divide(value_one,value_two))
print(f'{value_one} + {value_two} equal',add(value_one,value_two))
print(f'{value_one} - {value_two} equal',minus(value_one,value_two))