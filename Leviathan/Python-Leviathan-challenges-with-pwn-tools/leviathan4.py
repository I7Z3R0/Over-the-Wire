from pwn import *
import re
username = "leviathan4"
password = "vuH0coox6m"
host = "leviathan.labs.overthewire.org"
port = 2223

shell = ssh(username, host, password=password, port=port)
p = shell.run('sh')
p.sendline("cd .trash/")
log.warn(r'Run the command ./bin | tr " " "\n"| while read line; do echo "obase=16;ibase=2;$line" | bc ;done | tr -d "\n" | xxd -p -r')
p.interactive()
#cmd = r'./bin | tr " " "\n"| while read line; do echo "obase=16;ibase=2;$line" | bc ;done'
#sh.sendline(cmd)
#out = sh.recvlines(11)
#flag = 
#print(out)
#sh.close()

#./bin | tr " " "\n"| while read line; do echo "obase=16;ibase=2;$line" | bc ;done | tr -d "\n" | xxd -p -r'
