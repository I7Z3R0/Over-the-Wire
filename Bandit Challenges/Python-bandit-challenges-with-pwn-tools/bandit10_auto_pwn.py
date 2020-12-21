from pwn import *
user = "bandit9"
password = "UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("strings data.txt | grep '&====' | awk '{ print $2 }'")
log.success("The password for Bandit10 is " + sh.recvline().decode("utf-8"))
sh.close()

