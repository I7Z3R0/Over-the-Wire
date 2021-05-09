from pwn import *
import requests
import re
import html

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"
url = "http://{}.natas.labs.overthewire.org".format(username)

log.progress("Getting the natas9 password, Hold on! ")
session = requests.session()
#web = session.get(url + "/index-source.html", auth = (username, password)).text
web = session.post(url, data = {"secret" : "oubWYf2kBq", "submit": "submit"}, auth = (username, password)).text
#content = html.unescape(web)
#print(content)     # return bin2hex(strrev(base64_encode($secret)))
#print(web)
print("The password for natas9 is === " + re.findall("[A-Za-z0-9]{32}", web)[1])


'''
THIS IS THE SOURCE CODE: 
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>'''


'''
CODE I USED TO REVERSE IT

hex2bin("3d3d516343746d4d6d6c315669563362") = ==QcCtmMml1ViV3b
strrev("==QcCtmMml1ViV3b") = b3ViV1lmMmtCcQ==
base64_decode("b3ViV1lmMmtCcQ==") = oubWYf2kBq

OR

echo base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")))

php online compiler to reverse : https://www.w3schools.com/pHP/phptryit.asp?filename=tryphp_func_string_hex2bin
'''