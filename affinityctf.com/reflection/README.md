#### Challenge:

[task.gif](./task.gif ":ignore")

---

#### Solution:

```bash
binwalk -Me task.gif
strings ./_task.gif.extracted/* | grep AFF
```

---

<details><summary>FLAG:</summary>

```
AFFCTF{m@k3s_y0u__th0nk}
```

</details>
