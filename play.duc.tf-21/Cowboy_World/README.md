#### Challenge:

I heard this is the coolest site for cowboys and can you find a way in? [web-cowboy-world](https://web-cowboy-world-54f063db.chal-2021.duc.tf/)

---

#### Solution:

We are given a site with login form. After checking the `robots.txt` we found that the username we should use is `sadcowboy`. After trying out different passwords we noticed that using passwords containing apostrophy `'` returned `Internal Server Error` instead of `Incorrect username or password`. From that we got an idea to check for SQL injection. Usings `' or ''='` as password logged us in and we got the flag.

---

<details><summary>FLAG:</summary>

```
DUCTF{haww_yeeee_downunderctf?}
```

</details>
<br/>
