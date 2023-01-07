# exercise 3 questions-> check the email is it email or not 
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
user_email = 'Fahad-Salman@gcom'

res = pattern.search(user_email)
# print(res)

if res == None:
    print('Please enter your email address correctly')
else:
    print(res)