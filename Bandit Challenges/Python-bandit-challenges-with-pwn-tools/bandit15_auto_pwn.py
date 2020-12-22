from pwn import *
import re

user = "bandit15"
password = "BfMYroe26WYalil77FoDi9qh59eK5xNr"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -ign_eof | tail")
#total = sh.recv()
total = sh.recvlines(14)
result = re.findall("[a-zA-Z0-9]{32}", str(total))
print("The password for Bandit16 is ===" + result[-1])
sh.close()
