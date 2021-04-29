from pwn import *
import requests
import re
import html

username = "natas0"
password = "natas0"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas1 password, Hold on! ")
session = requests.session()
web = session.get(url, auth = (username, password)).text
print("The password for natas1 is === " + re.findall("[A-Za-z0-9]{32}", web)[0])
