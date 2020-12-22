from pwn import *

user = "bandit12"
password = "5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("mktemp -d")
temp = sh.recvline().decode("utf-8")
folder = temp.replace("$", "")
sh.sendline("cp data.txt" + str(folder))
sh.sendline("cd" + str(folder))
sh.sendline("xxd -r data.txt >> data")
sh.sendline("mv data data.gz")
sh.sendline("gunzip data.gz")
sh.sendline("mv data data.bz2")
sh.sendline("bunzip2 data.bz2")
sh.sendline("mv data data.gz")
sh.sendline("gunzip data.gz")
sh.sendline("mv data data.tar")
sh.sendline("tar -xf data.tar")
sh.sendline("mv data5.bin data5.tar")
sh.sendline("tar -xf data5.tar")
sh.sendline("mv data6.bin data6.bz2")
sh.sendline("bunzip2 data6.bz2")
sh.sendline("mv data6 data6.tar")
sh.sendline("tar -xf data6.tar")
sh.sendline("mv data8.bin data8.gz")
sh.sendline("gunzip data8.gz")
sh.sendline("cat data8 | awk '{print$4;}'")
#sh.sendline("ls")
result = sh.recvline().decode("utf-8")
#result = log.success("The password for Bandit13 is === " + sh.recvline().decode("utf-8"))
final = result.replace("$", "")
temp = "".join(final.split())
print("The password for Bandit13 is ===  $" + temp)
sh.close()
