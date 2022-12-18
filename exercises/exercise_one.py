# Exercise 1 questions => (Counte user age) 

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