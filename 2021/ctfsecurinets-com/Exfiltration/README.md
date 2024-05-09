#### Challenge:

2 spies were suspected to be involved in stoling secret data.

According to the logs, the data was stolen when the first comment in the following tweet was published: 
`https://twitter.com/_TheEmperors_/status/1373321585180966915` [comment.png](./comment.png ":ignore")

After this incident, all the necessary actions were taken in place to remediate the breach.

Hint: There is an important comment in this tweet apart the main tweet.

---

#### Solution:

```console
zsteg -a ./comment.png 
[?] 477840 bytes of extra data after zlib stream
extradata:0         .. file: Audio file with ID3 version 2.3.0, contains: MPEG ADTS, layer III, v1,  96 kbps, 44.1 kHz, JntStereo
    00000000: 49 44 33 03 00 00 00 00  2e 7b 54 59 45 52 00 00  |ID3......{TYER..|
    00000010: 00 0d 00 00 01 ff fe 32  00 30 00 32 00 31 00 00  |.......2.0.2.1..|
    00000020: 00 54 44 41 54 00 00 00  0d 00 00 01 ff fe 31 00  |.TDAT.........1.|
    00000030: 38 00 30 00 33 00 00 00  54 49 4d 45 00 00 00 0d  |8.0.3...TIME....|
    00000040: 00 00 01 ff fe 32 00 31  00 30 00 30 00 00 00 50  |.....2.1.0.0...P|
    00000050: 52 49 56 00 00 0f 2c 00  00 58 4d 50 00 3c 3f 78  |RIV...,..XMP.<?x|
    00000060: 70 61 63 6b 65 74 20 62  65 67 69 6e 3d 22 ef bb  |packet begin="..|
    00000070: bf 22 20 69 64 3d 22 57  35 4d 30 4d 70 43 65 68  |." id="W5M0MpCeh|
    00000080: 69 48 7a 72 65 53 7a 4e  54 63 7a 6b 63 39 64 22  |iHzreSzNTczkc9d"|
    00000090: 3f 3e 0a 3c 78 3a 78 6d  70 6d 65 74 61 20 78 6d  |?>.<x:xmpmeta xm|
    000000a0: 6c 6e 73 3a 78 3d 22 61  64 6f 62 65 3a 6e 73 3a  |lns:x="adobe:ns:|
    000000b0: 6d 65 74 61 2f 22 20 78  3a 78 6d 70 74 6b 3d 22  |meta/" x:xmptk="|
    000000c0: 41 64 6f 62 65 20 58 4d  50 20 43 6f 72 65 20 35  |Adobe XMP Core 5|
    000000d0: 2e 33 2d 63 30 31 31 20  36 36 2e 31 34 35 36 36  |.3-c011 66.14566|
    000000e0: 31 2c 20 32 30 31 32 2f  30 32 2f 30 36 2d 31 34  |1, 2012/02/06-14|
    000000f0: 3a 35 36 3a 32 37 20 20  20 20 20 20 20 20 22 3e  |:56:27        ">|
```

```bash
dd if=comment.png of=message.mp3 bs=1 skip=855938
```

---

<details><summary>FLAG:</summary>

```
Securinets{never_gonna_give_you_up_never_gonna_let_you_down_5739}
```

</details>
<br/>
