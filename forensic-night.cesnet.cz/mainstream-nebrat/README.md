#### Challenge:

`Použijme léty prověřené technologie!` ... by žádný hipster nikdy neřekl.

Dokážete najít chybku, kterou hipmajster udělal v aplikaci http://forensic-night.cesnet.cz/mainstreamisout ?

---

#### Solution:

https://git-scm.com/docs/gitrevisions

```bash
curl 'https://forensic-night.cesnet.cz/mainstreamisout/?list=master~18' 2>/dev/null | grep 'flag'
```

---

<details><summary>FLAG:</summary>

```
flag{Linus_Torvalds-5047}
```

</details>
