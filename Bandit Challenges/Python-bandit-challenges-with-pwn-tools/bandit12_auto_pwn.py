from pwn import *
user = "bandit11"
password = "IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cat data.txt")
log.success("We need to use the rot13 of this string ===" + sh.recvline().decode("utf-8"))
log.info("The password for Bandit12 is === $ 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu")
sh.close()

