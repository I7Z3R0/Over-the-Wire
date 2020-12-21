from pwn import *
user = "bandit10"
password = "truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cat data.txt | base64 -d | awk '{print $4;}'")
log.success("The password for Bandit11 is === " + sh.recvline().decode("utf-8"))
sh.close()

