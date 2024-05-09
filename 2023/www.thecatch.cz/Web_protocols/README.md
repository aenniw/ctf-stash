#### Challenge:

Ahoy, officer, 

almost all interfaces of the ship's systems are web-based, so we will focus the exercise on the relevant protocols. Your task is to identify all webs on given server, communicate with them properly and assembly the control string from responses.  

May you have fair winds and following seas!

The webs are running on server `web-protocols.cns-jv.tcc`.

---

#### Solution:

```bash
nmap -p0-65535 web-protocols.cns-jv.tcc

{
    echo "GET / HTTP/0.9" | nc web-protocols.cns-jv.tcc 5009 | sed "s/.*SESSION=//" | sed 's/;.*//' | head -n 3 | tail -n 1 | tr -d '\n';
    curl  http://web-protocols.cns-jv.tcc:5011 -v  2>&1 | grep SESSION | sed "s/.*SESSION=//" | sed 's/;.*//' | tr -d '\n';
    curl  http://web-protocols.cns-jv.tcc:5020 -v  2>&1 | grep SESSION | sed "s/.*SESSION=//" | sed 's/;.*//' | tr -d '\n';
} | base64 -d
```

---

<details><summary>FLAG:</summary>

```
FLAG{krLt-rvbq-abIR-433A}
```

</details>
<br/>
