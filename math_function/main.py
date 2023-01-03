import operations



name = str(input('Welcome , enter your username : '))
print(f'Hello {name} hope you enjoy...')
value_one = float(input('enter a number : '))
value_two = float(input('enter a number : '))

print(f'{value_one} X {value_two} equal',operations.multiply(value_one,value_two))
print(f'{value_one} ÷ {value_two} equal',operations.divide(value_one,value_two))
print(f'{value_one} + {value_two} equal',operations.add(value_one,value_two))
print(f'{value_one} - {value_two} equal',operations.minus(value_one,value_two))