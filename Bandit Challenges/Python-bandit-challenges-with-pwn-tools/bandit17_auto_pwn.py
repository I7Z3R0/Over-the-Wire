from pwn import *

user = "bandit17"
password = "xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("diff -s passwords.new passwords.old | grep '<' | awk '{print$2}'")
log.success("The password for Bandit18 is === " + sh.recvline().decode("utf-8"))
sh.close()
