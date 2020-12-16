from pwn import *
user = "bandit0"
password = "bandit0"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port )
sh = shell.run('sh')
sh.sendline("cat readme")
log.success("The password for the bandit1 is =====" + sh.recvline().decode("utf-8"))
sh.close()
