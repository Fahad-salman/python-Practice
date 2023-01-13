import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    print('=========================================================')
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, check api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_cheak):
    hashes = (line.split(':')for line in hashes.text.splitlines())
    for h,count  in hashes:
        if h == hash_to_cheak:
            return count
    return 0

def pwend_api_check(password):
    shai1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char,tall = shai1password[:5],shai1password[5:]
    response = request_api_data(first5_char)
    print(f'({first5_char}) , ({tall})')
    return get_password_leaks_count(response,tall)

def main(args):
    for password in args:
        count = pwend_api_check(password)
        if count:
            print(f'({password}) was found ({count}) times... \n you should change your password')
        else:
            print(f'{password} was not found . ')
    return '========================================================='


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))