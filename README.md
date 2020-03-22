# CTF-Stash

## CTF Events

- ### [try2hack.me](./try2hack.me/README.md)
- ### [tryhackme.com](./tryhackme.com/README.md)
- ### [catch the qubit](./catch-the-qubit/README.md)
- ### thecatch.cz - 2018
  - [Practice Challenges](./www.thecatch.cz-18/round-0/README.md)
  - [Round - 1](./www.thecatch.cz-18/round-1/README.md)
  - [Round - 2 (leaked)](./www.thecatch.cz-18/round-2-leaked/README.md)
  - [Round - 2](./www.thecatch.cz-18/round-2/README.md)
- ### [thecatch.cz - 2019](./www.thecatch.cz-19/README.md)
- ### [hackcon.online](./hackcon.online/README.md)
- ### [forensic-night.cesnet.cz](./forensic-night.cesnet.cz/README.md)
- ### [ctf.dragonsector.pl](./ctf.dragonsector.pl/README.md)
- ### [affinityctf.com](./affinityctf.com/README.md)
- ### [nactf.com](./nactf.com/README.md)
- ### [challenges.reply.com](./challenges.reply.com/README.md)
- ### [ctf.ritsec.club](./ritsec_ctf_2019/README.md)
- ### [venividivici.iitdh.ac.in](./venividivici.iitdh.ac.in/README.md)
- ### [aeroctf.com](./aero-ctf-2020/README.md)
- ### [utctf.live](./utctf-2020/README.md)
- ### [tuctf.com](./tuctf.com/README.md)
- ### [ctfsecurinets.com](./ctfsecurinets-com-2020/README.md)

## CTF dumping

```bash
./ctf-dump.py   # User-Agent/Cookie needs to be updated based on CTF
```

External tools [CTFdScraper](https://github.com/ichinano/CTFdScraper) [CTFDump](https://github.com/realgam3/CTFDump)

## CTF Toolkits

- [CyberChef](https://gchq.github.io/CyberChef/)
- [StegOnline](https://georgeom.net/StegOnline/upload)
- [unicode_steganography](https://330k.github.io/misc_tools/unicode_steganography.html)
- [Volatility - Docker](https://hub.docker.com/r/blacktop/volatility)
  - `docker run --rm -v $(pwd):/data:ro blacktop/volatility -f silentbanker.vmem pslist`
  - plugins:
    - https://raw.githubusercontent.com/dfirfpi/hotoloti/master/volatility/mimikatz.py
    - https://raw.githubusercontent.com/superponible/volatility-plugins/master/sqlite_help.py
    - https://raw.githubusercontent.com/superponible/volatility-plugins/master/chromehistory.py
    - https://raw.githubusercontent.com/superponible/volatility-plugins/master/firefoxhistory.py

## Resources

- Curated list of Unix binaries [GTFOBins](https://gtfobins.github.io/)
- USB pcap how-to [LFC-Forensics](https://bitvijays.github.io/LFC-Forensics.html)
- Stegano cheatsheet [steganography-101](https://pequalsnp-team.github.io/cheatsheet/steganography-101)

## FAQ

- serving local processes via ncat
  - `ncat --listen --keep-open --sh-exec ./main.py 7777`

## Building locally

To work locally with this project, you'll have to follow the steps below:

1. Fork, clone or download this project
1. Install Docsify `npm install docsify-cli -g`
1. Preview your project: `docsify serve`
