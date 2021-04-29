from pwn import *
import requests
import re
import html

username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas2 password, Hold on! ")
session = requests.session()
web = session.get(url, auth = (username, password)).text
print("The password for natas2 is === " + re.findall("[A-Za-z0-9]{32}", web)[1])
