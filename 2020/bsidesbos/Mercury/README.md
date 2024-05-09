#### Challenge:

This ZIP file is hanging out with the stars in the Milky Way! Can you find the flag? [mercury.zip](./mercury.zip ":ignore")

---

#### Solution:

We are provided with the zip containing `.hg` folder which is mercurial's equivalent for `.git` folder.

```bash
unzip mercury.zip
cd mercury
hg grep --diff flag | grep flag
```

---

<details><summary>FLAG:</summary>

```
flag{version_control_for_the_solar_system}
```

</details>
<br/>
