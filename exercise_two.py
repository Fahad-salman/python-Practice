# Exercise 2 questions => (Counte user password and replace password to ** )  exercise two

userName = input('Enter your name: ')
passWord = input('Enter your password: ')
lengthPassword = len(passWord)
hidePassword = ('*' * lengthPassword)
print(f'welcome {userName} , Your password {hidePassword} is {lengthPassword} letters long .')
