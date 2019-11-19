#### Challenge:

Rev up your GPUs... `nc ctfchallenges.ritsec.club 8080` Flag format `RS{ }`

---

#### Solution:

```python
#!/bin/python3

# subprocess.run(['john --wordlist=/usr/share/john/password.lst --format=sha512crypt /root/Desktop/passwd '], shell=True)

import random
import string
def randomString(stringLength=8):
    """Generate a random string of fixed length """
    letters= string.ascii_lowercase
    return ''.join(random.sample(letters,stringLength))

from pwn import *


try:
    s = remote('ctfchallenges.ritsec.club', 8080)

    print('skip', s.recvline())
    print('skip', s.recvline())

    mmsg = s.recv().decode("utf-8")
    mmsg_split = mmsg.split( )
    wordlists =[]
    wordlists.append(mmsg_split[11][:-1])
    wordlists.append(mmsg_split[12])
    wordlists.append(mmsg_split[14])
    print(wordlists)

    while True:
        new_hash = s.recvline(True).decode("utf-8").strip()
        print(new_hash)

        hash_id = randomString(8)
        f=open("hash_"+hash_id+".txt","w+")
        f.write(new_hash)
        f.close()


        for wordlist in wordlists:

            print("###########################################################")
            print("# Trying wordlist: ")
            print("#" + wordlist)
            print("# FOR HASH: ")
            print("# "+ new_hash)
            print("###########################################################")
            command="~/projects/JohnTheRipper/run/john --wordlist=./Passwords/Common-Credentials/"+wordlist+" hash_"+hash_id+".txt --verbosity=1 1>john.out 2>john.err"

            john_result = subprocess.run([command], shell=True, stdout=subprocess.PIPE)

            command2="~/projects/JohnTheRipper/run/john --show hash_"+hash_id+".txt"
            password = subprocess.run([command2], shell=True, stdout=subprocess.PIPE)
            print(password)
            if (str(password).find('0 left') != -1):
                print("====== FOUND ======")
                password_final = str(password)[(str(password).find('?')+2):str(password).find("1 pass")][:-4]
                print(password_final)
                s.sendline(password_final)
                break;

        print('skip', s.recvline(True).decode("utf-8"))
except Exception as e:
    raise
except ValueError as e:
    print(mmsg)
finally:
    s.close()

```

---

<details><summary>FLAG:</summary>

```
RS{H@$HM31FY0UCAN}
```

</details>
<br/>
