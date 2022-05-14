#### Challenge:

Hi Expert,

the archaeologists believe that domain `thecatchu6jlyqgen3ox74kjcfr5lmwdc7jqj3vmekq6y45dmvo5xmad.onion` could contain interesting information intended for dark minded. Check it out.

Good Luck!

---

#### Solution:

Tor site, we have done something similar in `try2hack.me` Task 4. Just connecting to the onion domain gets us the flag.

```bash
tor &;
socat TCP4-LISTEN:8000,reuseaddr,fork SOCKS4A:127.0.0.1:thecatchu6jlyqgen3ox74kjcfr5lmwdc7jqj3vmekq6y45dmvo5xmad.onion:80,socksport=9050 &
wget 127.0.0.1:8000 -O index.html
```

---

<details><summary>FLAG:</summary>

```
FLAG{uNMI-DKSU-NKmq-7QE0}
```

</details>
<br/>
