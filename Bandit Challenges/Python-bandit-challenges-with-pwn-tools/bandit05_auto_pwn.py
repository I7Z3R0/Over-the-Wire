from pwn import *
user = "bandit4"
password = "pIwrPrtPN36QITSp3EQaw936yaFoFgAB"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cd inhere/;cat ./-file07")
log.success("The password for bandit5 is ===" + sh.recvline().decode("utf-8"))
sh.close()
