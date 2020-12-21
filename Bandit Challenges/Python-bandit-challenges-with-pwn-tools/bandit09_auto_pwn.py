from pwn import *
user = "bandit8"
password = "cvX2JJa4CFALtqS87jk27qwqGhBM9plV"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
#sh.sendline("pwd")
#log.success(sh.recvline().decode("utf-8"))
sh.sendline("cat data.txt | sort | uniq -c | grep -v '10' | awk '{print $2;}'")
log.success("The password for Bandit9 is ===" + sh.recvline().decode("utf-8"))
sh.close()

