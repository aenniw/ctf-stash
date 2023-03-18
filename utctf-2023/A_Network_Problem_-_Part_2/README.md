#### Challenge:

Update: smb port has been moved to 8445 from 445 on networking-misc-p2

betta.utctf.live has other interesting ports. Lets look at 8445 this time.
By Robert Hill (@Rob H on discord)

`betta.utctf.live:8445`

---

#### Solution:

```bash
smbclient -L betta.utctf.live -N

        Sharename       Type      Comment
        ---------       ----      -------
        WorkShares      Disk      Sharing of work files
        BackUps         Disk      File Backups.
        IPC$            IPC       IPC Service (Samba Server)
SMB1 disabled -- no workgroup available

smbclient //betta.utctf.live/WorkShares/ -U guest% -c "get shares\IT\Itstuff\notetoIT"
cat shares\\IT\\Itstuff\\notetoIT | grep utflag
```

---

<details><summary>FLAG:</summary>

```
utflag{out-of-c0ntrol-access}
```

</details>
<br/>
