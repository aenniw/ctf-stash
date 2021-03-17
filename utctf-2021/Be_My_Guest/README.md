#### Challenge:

Can you share some secrets about this box?

`nmap` is allowed for this problem. However, you may only target `misc.utctf.live ports 8881 & 8882`. Thank you.

---

#### Solution:

```console
# nmap -sV -p 8881,8882 misc.utctf.live
Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-13 21:49 CET
Stats: 0:00:07 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Nmap scan report for misc.utctf.live (3.236.87.2)
Host is up (0.19s latency).
rDNS record for 3.236.87.2: ec2-3-236-87-2.compute-1.amazonaws.com

PORT     STATE SERVICE     VERSION
8881/tcp open  netbios-ssn Samba smbd 4.6.2
8882/tcp open  netbios-ssn Samba smbd 4.6.2

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 62.79 seconds
# smbclient -L misc.utctf.live -p 8881 -N

        Sharename       Type      Comment
        ---------       ----      -------
        guest           Disk      Look, but don't touch please.
        IPC$            IPC       IPC Service (Samba Server)
SMB1 disabled -- no workgroup available
```

```bash
mount -t cifs -o guest,port=8881 //misc.utctf.live/guest/ smb/ -v
cat ./smb/flag.txt 
```

---

<details><summary>FLAG:</summary>

```
utflag{gu3st_p4ss_4_3v3ry0n3}
```

</details>
<br/>
