# exercise 3 questions-> check the email is it email or not 
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
user_email = input('Enter your email address : ')

res = pattern.search(user_email)
# print(res)

if res == None:
    print('Please enter your email address correctly')
else:
    print(res)

# password checker

pat = re.compile(r'[A-Za-z0-9$%#@!?]{8,}')
password = input('Enter your password : ')
chek = pat.fullmatch(password)

if chek == None:
    print('password invalid')
else:
    print(chek)  
    
    