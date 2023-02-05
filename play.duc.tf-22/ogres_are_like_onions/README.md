#### Challenge:

if you see this you have to post in `#memes` thems the rules

```
docker run -tp 8000:8000 downunderctf/onions
```

[hint](https://youtu.be/uFRHP02PruE)

---

#### Solution:

```bash
docker save downunderctf/onions -o onion.tar
tar -xvf onion.tar
tar -xvf ./506946d44c8939efe882d5fd59797d22f2fe84adb7e2b7af066ca1563c11d464/layer.tar 
eog app/memes/flag.jpg
```

---

<details><summary>FLAG:</summary>

```
DUCTF{P33L_B4CK_TH3_L4Y3RS}
```

</details>
<br/>
