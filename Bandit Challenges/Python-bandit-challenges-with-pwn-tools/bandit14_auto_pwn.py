from pwn import *
import re

user = "bandit14"
password = "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("nc localhost 30000")
sh.sendline("4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e")
total = sh.recvlines(2)
result = total[-1]
print("The password for bandit15 is === " + result.decode("utf-8"))
sh.close()
