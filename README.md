# CTF-Stash

## CTF Toolkits

[CTF-tools.md](./CTF-tools.md ":include")

## CTF dumping

```bash
./ctf-dump.py   # User-Agent/Cookie needs to be updated based on CTF
```

External tools [CTFdScraper](https://github.com/ichinano/CTFdScraper) [CTFDump](https://github.com/realgam3/CTFDump)

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

## Credits

- [aenniw](https://ctftime.org/user/65413)
- [spacecowboy](https://ctftime.org/user/65412)
