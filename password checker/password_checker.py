# importing required packages as requests(deals with url response) and hashlib(to generate hash codes for passwords)

import requests
import hashlib

# function to hit url and check for status code
def request_url(to_check):
    url='https://api.pwnedpasswords.com/range/' + to_check
    response=requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'please check the url its throwing {response.status_code} and enter again')
    return response

# code to check pawned pwd by giving hash codes to check for pawned stats
def password_leaks_count(hashes,hash_to_check):
    hashes= (lines.split(':') for lines in hashes.text.splitlines())
    for h,count in hashes:
        print(h,count)

# code to convert input pwd to hashcode and check for pawning
def pawned_api_check(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest()
    first_5_char,tail=sha1password[:5],sha1password[5:]
    resp=request_url(first_5_char)
    print(resp)
    return password_leaks_count(resp,tail)


pawned_api_check('123')
