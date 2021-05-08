#### Challenge:

Our Lubuntu server has been breached! We recieved an alert about it communicating with malicious servers and we saw a SIGNIFICANT increase in CPU usage. We SSHed in and saw that changes had been made to the / directory. We need to know how this attacker got in (so we can keep him out in the future) and what he was using our server for...

uname: "victem" (ya, we kinda jinxed ourselves with that name) pw: "correct-horse-battery-staple"

Download: https://drive.google.com/file/d/16sV8pXSrG22KL4zJ9VrpZTcZAs_N9XYw/view

---

#### Solution:

We are presented with OVA virtual machine image. After logging into it with given credentials, I checked the root folder as the description said. There I was able to find `potfile` with the root password (`toor`). With this I logged in as root and checked the `history`. It lead to repository https://gitlab.com/thehacker1/payload. After running the payload from the repository without lines `sleep $W` and `rm encrypted.csv`, we get `encrypted.csv` which contains the flag.

---

<details><summary>FLAG:</summary>

```
WPI{open-ports-will-be-abused}
```

</details>
<br/>
