from pwn import *
user = "bandit20"
password = "GbKksEFF4yrVs6il55v6gwY5aVje5f0j"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("cat /etc/bandit_pass/bandit20 | nc -nlp 3333 &")
sh.sendline("./suconnect 3333")
final = sh.recvlines(3)
end = final[-1]
print("The password for Bandit21 is === " + end.decode("utf-8"))
sh.close()
