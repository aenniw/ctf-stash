#### Challenge:

Ahoy, deck cadet,

there are rumors that on the ship web server is not just the official presentation. Your task is to disprove or confirm these rumors.

May you have fair winds and following seas! 

Ship web server is available at <a href="http://www.cns-jv.tcc" target="_blank">http:&#47;&#47;www.cns-jv.tcc</a>.

---

#### Solution:

- inspecting the certificate reveals that it has multiple hostnames leading us into intro altering `host` header.  

```
documentation.cns-jv.tcc
home.cns-jv.tcc
pirates.cns-jv.tcc
structure.cns-jv.tcc
```


```bash
curl -k https://www.cns-jv.tcc -H "host: pirates.cns-jv.tcc" 2>/dev/null | grep '>ver\.' | sed 's/.*ver. //' | sed 's/<\/small>.*//' | base64 -d
curl -k https://www.cns-jv.tcc -H "host: structure.cns-jv.tcc" 2>/dev/null | grep '>ver\.' | sed 's/.*ver. //' | sed 's/<\/small>.*//' | base64 -d
curl -k https://www.cns-jv.tcc/style.css -H "host: documentation.cns-jv.tcc" 2>/dev/null | sed 's/.*ver. //' | sed 's/".*//' | base64 -d 
curl -k https://www.cns-jv.tcc/?user=suzan -H "host: home.cns-jv.tcc" 2>/dev/null | grep '>ver\.' | sed 's/.*ver. //' | sed 's/<\/small>.*//' | base64 -d 

```

---

<details><summary>FLAG:</summary>

```
FLAG{ejii-plmQ-Q53C-gMwc}
```

</details>
<br/>
