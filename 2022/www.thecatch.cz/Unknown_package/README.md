#### Challenge:

Hi, promising candidate,

the cleaning drones have taken pictures of some abandoned unknown package in our backup depot. The AI claims that the analyzed item is in no way a package, instead it repeats "cat - animal - dangerous - avoid".

Get as much as possible information about the package.

Download [taken pictures](./unknown_package.zip ":ignore") (MD5 checksum `c6f700e1217c0b17b7d3a35081c9fabe`).

May the Packet be with you!

---

#### Solution:

- crop the bar codes via any `img` tool and scan the codes, one of them reveals the flag. [bar-1.png](./bar-1.png ":ignore")

```bash
zbarimg ./bar-1.png
```

---

<details><summary>FLAG:</summary>

```
FLAG{Oics-NF3B-vUOC-pUMt}
```

</details>
<br/>
