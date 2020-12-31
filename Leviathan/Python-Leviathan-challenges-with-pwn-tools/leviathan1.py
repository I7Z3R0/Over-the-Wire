from pwn import *

username = "leviathan1"
password = "rioGegei8m"
host = "leviathan.labs.overthewire.org"
port = 2223

shell = ssh(username, host, password=password, port=port)
p = shell.run('sh')
p.sendline("(echo sex;cat) | ./check")
p.sendline("cat /etc/leviathan_pass/leviathan2")
log.success("The password for leviathan2 is === " + p.recvline().decode("utf-8"))
p.close()
