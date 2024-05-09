#### Challenge:

Port knocking is boring. Enhance your security through obscurity using sigknock.

`ssh ctf@sigknock.wpictf.xyz` pass: `$1gkn0ck`

---

#### Solution:

- detect all `signals` that binary listens to

```bash
kill -9 $(ps | grep irqknock | awk '{print $1}')
for s in `seq 0 100`; do
    /usr/bin/irqknock &
    echo "$s"
    kill "-$s" $(ps | grep irqknock | awk '{print $1}')
done
```

- send `signals` in correct order

```bash
for s in 2 3 11 13 17; do
    kill "-$s" $(ps | grep irqknock | awk '{print $1}')
done
```

---

<details><summary>FLAG:</summary>

```
WPI{1RQM@St3R}
```

</details>
<br/>
