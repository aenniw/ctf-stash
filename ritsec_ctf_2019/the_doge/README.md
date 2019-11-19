#### Challenge:

Steganography is the practice of concealing messages or information within other nonsecret data and images. The doge holds the information you want, feed the doge a treat to get the hidden message. [the_doge.jpg](./the_doge.jpg ":ignore")

---

#### Solution:

```bash
steghide extract -p treat -sf ./the_doge.jpg -xf -
```

---

<details><summary>FLAG:</summary>

```
RITSEC{hAppY_l1L_doG3}
```

</details>
<br/>
