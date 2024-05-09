#### Challenge:

Ogres are like files -- they have layers! [shrek.jpg](./shrek.jpg ":ignore")

---

#### Solution:

```bash
binwalk shrek.jpg
dd if=shrek.jpg of=payload bs=1 skip=275566
file x payload
7z x payload
binwalk -Me  flag.tar.gz
grep -R  TUCTF _flag.tar.gz.extracted/
```

---

<details><summary>FLAG:</summary>

```
TUCTF{F1L3S4R3L1K30N10NSTH3YH4V3L4Y3RS}
```

</details>
<br/>
