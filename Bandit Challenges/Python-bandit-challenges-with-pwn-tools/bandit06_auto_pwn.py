from pwn import *
user = "bandit5"
password = "koReBOKuIDDepwhWk7jZC0RTdopnAYKh"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run("sh")
sh.sendline("cd inhere/;find . -size 1033c ! -executable")
log.success("The correct file to search is === " + sh.recvline().decode("utf-8"))
sh.sendline("cat ./maybehere07/.file2")
log.success("The password for bandit6 is ===" + sh.recvline().decode("utf-8"))
sh.close()
