from random import randint
import os
import string


# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
# experimental_password = input("Enter your password: ")

# password =''
# while(password != experimental_password):
#     password =''
#     for i in range(len(experimental_password)):
#         guess_password = chars[randint(0,17)]
#         password = str(guess_password)+str(password)
#         print(password)
#         print('Checking password , please wait... : ')
#         os.system('clear')
# print(f'probably this is the password : {password}')


userPass = input("\nEnter your password:")

chars =list(string.ascii_lowercase)

guessPass = ""

while (guessPass != userPass):
    guessPass = ""
    for letter in range(len(userPass)):
        guessLetter = chars[randint(0, 25)]
        guessPass = str(guessLetter) + str(guessPass) 
    print('Checking password  please wait... : ',end=' ')
    print(guessPass)
    os.system('clear')

print("password is: ", guessPass)
