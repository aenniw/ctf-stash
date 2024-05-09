#### Challenge:

Bruh, do you even read books, lol? Then solve this: `++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++++++++++++.<++++++++++++++++++++++++.<++++++++++++++++++++++.-------.++++++.--.+++.>>.<.<-.--------.+++++++.+++++..------.>>.<.<+.-----.++++++++++.++.----.-.>>.<<---------.++++++++++++.----.-.--.+++++++++++++.-------------.` [file1.txt](./file1.txt ":ignore") [file2.txt](./file2.txt ":ignore") [desc.txt](./desc.txt ":ignore")

---

#### Solution:

```bash
cat ./file2.txt | head -n 1
cat ./file2.txt | sed 's/!/!\n\nx = 0, y = 0, rule = B3\/S23\n/g'
```

Import and check candidates in https://copy.sh/life/

![life.png](./life.png ":ignore")

```bash
echo 'YmFiZWw=' | base64 -d     # google to https://libraryofbabel.info
bf ./desc.txt                   # x^4-314x^3+2771x^2-7954x+7320=0 x=2, x=3, x=4, x=305
echo "https://libraryofbabel.info/book.cgi?$(cat ./file1.txt | xxd -r -p)-w2-s3-v04:305"
```

---

<details><summary>FLAG:</summary>

```
d4ark{daymsonureadbooksbiglol}c0de
```

</details>