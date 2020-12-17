from pwn import *
user = "bandit3"
password = "UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cd inhere/;cat .hidden")
log.success("The password for Bandit4 is ===" + sh.recvline().decode("utf-8"))
sh.close()

