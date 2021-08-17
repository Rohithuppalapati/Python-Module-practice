# importing hashlib(generates hashcodes for pwds) and requests(ping a url and get response code)

import hashlib
import requests


# Writing function for URL that needs to be checked get response code and password given which needs to be verified

def request_url(to_check):
    url = 'https://api.pwnedpasswords.com/range/' + to_check
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'please check url that you have given it is throwing {response.status_code} error')
    return response


# Writing function to check count of how many times password was hacked

def password_leaks_count(hashes, hash_to_check):
    hash_checker = (lines.split(':') for lines in hashes.text.splitlines())
    for hash,count in hash_checker:
        if hash == hash_to_check:
            return count
    return 0


# Writing function to check pawned password(also convert password to hash code in hexadecimal)

def pawned_password_checker(password):
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first_5char, tail = sha1password[:5], sha1password[5:]
    resp = request_url(first_5char)
    return password_leaks_count(resp, tail)

# writing main function to execute pawned_password_checker function

def main(args):
    for password in args:
        count = pawned_password_checker(password)
        if count:
            print(f'your {password} has been hacked {count} times please change it ')
        else:
            print('password not found carry on ......')


# calling main func to run program

if __name__ == '__main__':
    list1 = ['rohith1414', 'happy123']
    main(list1)
