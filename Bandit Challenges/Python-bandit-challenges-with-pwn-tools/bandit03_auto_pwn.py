from pwn import *
user = "bandit2"
password = "CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password= password, port=port)
sh = shell.run('sh')
cmd = "cat spaces\ in\ this\ filename"
sh.sendline(cmd)
log.success("The password for bandit3 is ==== " + sh.recvline().decode("utf-8"))
sh.close()
