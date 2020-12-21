from pwn import *
user = "bandit7"
password = "HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cat data.txt | grep millionth | cut -f 2")
log.success("The password for Bandit8 is === " + sh.recvline().decode("utf-8"))
sh.close()
