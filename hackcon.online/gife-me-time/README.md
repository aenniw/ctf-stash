#### Challenge:

A renowned hacker, John, has hidden all the credentials of his [website](http://68.183.158.95/GIFe_me_time/) as he decided to pause his work. Can you find the credentials before he secures his website?

PS: Maybe what you find first is not always the answer :)

---

#### Solution:

In browser inspect network on http://68.183.158.95/GIFe_me_time/

```bash
wget http://68.183.158.95/GIFe_me_time/images/demo/username.gif
convert -coalesce username.gif username-%05d.pgm # count flags on pictures -> 71 49 70 115 95 52 114 51 95 63 46 95 99 46 46 106
for c in 71 49 70 115 95 52 114 51 95 63 46 95 99 46 46 106; do  echo $c | awk '{printf("%c",$1)}'; done; echo # G1Fs_4r3_?._c..j

wget http://68.183.158.95/GIFe_me_time/images/demo/password.gif
convert -coalesce password.gif password-%05d.pgm
zbarimg ./password-* | grep 'd4rk' # QR-Code:here's the actual one: d4rk{qrc0d3s_4r3_fun_t00_r1ght}
```

---

<details><summary>FLAG:</summary>

```
d4rk{J0hN_1s_n0t_4_g00d_h4ck3r}c0de
```

</details>
