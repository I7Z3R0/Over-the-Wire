from pwn import *
user = "bandit21"
password = "gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr"
host = "bandit.labs.overthewire.org"
port = 2220

shell = ssh(user, host, password=password, port=port)
sh = shell.run('sh')
log.info("searching for the cron job in /etc/cron.d/cronjob_bandit22")
sh.sendline("cat /etc/cron.d/cronjob_bandit22")
sh.recvline()
sh.recvline()
log.info("Checking the script which is being run every minute")
sh.sendline("cat /usr/bin/cronjob_bandit22.sh")
sh.recvline()
sh.recvline()
sh.recvline()
log.info("Found that the password is being copied to folder /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv every minute")
sh.sendline("cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv")
log.success("The password for Bandit22 is === " + sh.recvline().decode("utf-8"))
sh.close()
