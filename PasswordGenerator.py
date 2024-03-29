import random
import string

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','?']

def generate_password():
    while True:
        try:
            pwd_longer = int(input('How long do you want your password to be? '))
            if pwd_longer == 0:
                print('Password length must be greater than 0.')
                continue
        except ValueError :
            print('Please enter a number.')
        else:
            break            
    pwd_list = [random.choice(chars) for i in range(pwd_longer)]
    print('Here is your password:',''.join(pwd_list))
    
generate_password()

# ---------------------------------------------------------------- 

def generate_password_v2(lng):
    """Generates a random password with the given length"""
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(lng))
    return password

psd = int(input('Enter leangt password : '))
password = generate_password_v2(psd)
print("Generated password:", password)
