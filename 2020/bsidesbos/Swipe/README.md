#### Challenge:

Whoops, I accidentally right-swiped on something I didn't mean to. Now I have this weird file? <br><br> <b>Open the <code>Deployment</code> tab to start this challenge.</b>

---

#### Solution:

```bash
cp swipe /tmp/swipe/.flag.png.swp
vim /tmp/swipe/flag.png # recover file
dd if=/tmp/swipe/flag.png of=flag.png bs=1 skip=889
zbarimg flag.png
```

---

<details><summary>FLAG:</summary>

```
flag{swipe_right_on_vim_swap_soisoisoisoisoi}
```

</details>
<br/>
