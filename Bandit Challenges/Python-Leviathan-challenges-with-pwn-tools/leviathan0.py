from pwn import *
import re

username = "leviathan0"
password = "leviathan0"
host = "leviathan.labs.overthewire.org"
port = 2223

shell = ssh(username, host, password=password, port=port)
p = shell.run('sh')
p.sendline("cd .backup/")
p.sendline("cat bookmarks.html | grep password")
final = p.recvline().decode("utf-8")
flag = re.findall("[A-Za-z0-9]{10}", final)
print("The password for leviathan1 is === " + flag[3])
p.close()
