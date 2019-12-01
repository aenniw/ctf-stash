#### Challenge:

Something's blocking my flag from this file... [document.odt](./document.odt ":ignore")

---

#### Solution:

```bash
binwalk -Me  ./document.odt
cat _document.odt.extracted/Basic/Standard/flag.xml
```

---

<details><summary>FLAG:</summary>

```
TUCTF{ST0P_TRUST1NG_M4CR0S_FR0M_4N_UNKN0WN_S0URC3}
```

</details>
<br/>
