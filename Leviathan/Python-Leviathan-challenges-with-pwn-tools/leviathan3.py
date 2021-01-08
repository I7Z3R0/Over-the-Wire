from pwn import *
import re
username = "leviathan3"
password = "Ahdiemoo1j"
host = "leviathan.labs.overthewire.org"
port = 2223

shell = ssh(username, host, password=password, port=port)
p = shell.run('sh')
p.sendline('(echo snlprintf;cat) | ./level3')
p.recvline()
p.sendline("cat /etc/leviathan_pass/leviathan4")
log.success("The password for leviathan4 is === " + p.recvline().decode("utf-8"))
#log.warn("RUN THE COMMAND 'cat /etc/leviathan_pass/leviathan3'")
#sh.interactive()

p.close()
