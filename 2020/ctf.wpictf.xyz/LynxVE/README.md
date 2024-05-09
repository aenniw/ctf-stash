#### Challenge:

`ssh ctf@lynxve.wpictf.xyz` pass: `lynxVE`

---

#### Solution:

- lynx browser navigate to `//etc/passwd` via `SHIFT + G`

```bash
root:x:0:0::/root:/bin/bash
bin:x:1:1::/:/usr/bin/nologin
daemon:x:2:2::/:/usr/bin/nologin
mail:x:8:12::/var/spool/mail:/usr/bin/nologin
ftp:x:14:11::/srv/ftp:/usr/bin/nologin
http:x:33:33::/srv/http:/usr/bin/nologin
nobody:x:65534:65534:Nobody:/:/usr/bin/nologin
dbus:x:81:81:System Message Bus:/:/usr/bin/nologin
systemd-journal-remote:x:982:982:systemd Journal Remote:/:/usr/bin/nologin
systemd-network:x:981:981:systemd Network Management:/:/usr/bin/nologin
systemd-resolve:x:980:980:systemd Resolver:/:/usr/bin/nologin
systemd-timesync:x:979:979:systemd Time Synchronization:/:/usr/bin/nologin
systemd-coredump:x:978:978:systemd Core Dumper:/:/usr/bin/nologin
uuidd:x:68:68::/:/usr/bin/nologin
ctf:x:1000:1000::/home/ctf:/bin/sh
```

- then go to `//home/ctf/flag`

---

<details><summary>FLAG:</summary>

```
WPI{lynX_13_Gr8or_Th@n_Chr0m1Um}
```

</details>
<br/>
