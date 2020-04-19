#### Challenge:

The flag could be any one of us! He could be in this very room... He could be you! He could be me! He could even be... [Hint](https://www.youtube.com/watch?v=RSRd7MAaxeQ)

---

#### Solution:

```bash
for i in {1..23}; do
    curl -Ss "https://ctf.wpictf.xyz/teams?page=${i}" | grep "WPI{"
done
```

---

<details><summary>FLAG:</summary>

```
WPI{the_best_teams_make_the_flags}
```

</details>
<br/>
