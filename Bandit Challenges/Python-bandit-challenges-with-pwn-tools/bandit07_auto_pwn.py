from pwn import *
user = "bandit6"
password = "DXjZPULLxYr17uwoI01bNLQbtFemEgo7"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("find / -user bandit7 -group bandit6 -size 33c 2>/dev/null")
log.success("The correct file is == " + sh.recvline().decode("utf-8"))
sh.sendline("cat /var/lib/dpkg/info/bandit7.password")
log.success("The password for Bandit7 is === " + sh.recvline().decode("utf-8"))
sh.close()
