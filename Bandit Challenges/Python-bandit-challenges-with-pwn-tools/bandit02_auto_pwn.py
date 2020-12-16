from pwn import *
user = "bandit1"
password = "boJ9jbbUNNfktd78OOpsqOltutMc3MY1"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cat ./-")
log.success("The password for bandit2 is === " + sh.recvline().decode("utf-8"))
sh.close()
