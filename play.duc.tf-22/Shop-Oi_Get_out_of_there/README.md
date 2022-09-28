#### Challenge:

Someone was able to successfully break into the admin account!

Do you know what the old password was?

Flag format: The password, case insensitive

---

#### Solution:

Filtering for logins with (on the [JSON](../Shop-SetupDisclaimer/DownUnderShop.JSON)):

```bash
grep "shop.downunderctf.com/login?ref=" DownUnderShop.JSON | sort | uniq
```
gives us:

```text
    "url": "shop.downunderctf.com/login?ref=M2RjOTE5ZGUxODZkMWE4ZWU2MmZmZjkyZDgwODM5Zjc6NmQ3YzViM2U3OTZkODMzYjNmZGQ0MGY0Y2U1N2ZhY2Q%3D",
    "url": "shop.downunderctf.com/login?ref=MmFjOWNiN2RjMDJiM2MwMDgzZWI3MDg5OGU1NDliNjM6NmQ3YzViM2U3OTZkODMzYjNmZGQ0MGY0Y2U1N2ZhY2Q%3D",
    "url": "shop.downunderctf.com/login?ref=N2E1ODFhYzRkOGNiM2JmYzU5NmZjZTlhZmIxMTVmZDI6NmQ3YzViM2U3OTZkODMzYjNmZGQ0MGY0Y2U1N2ZhY2Q%3D",
    "url": "shop.downunderctf.com/login?ref=YjUwNmZiMGNhYmI2MGU5ZjExMzJkYWE3MmRmNGQ1Njc6NmQ3YzViM2U3OTZkODMzYjNmZGQ0MGY0Y2U1N2ZhY2Q%3D",
```

Decoding those `base64`s yields:

```text
b506fb0cabb60e9f1132daa72df4d567:6d7c5b3e796d833b3fdd40f4ce57facd
2ac9cb7dc02b3c0083eb70898e549b63:6d7c5b3e796d833b3fdd40f4ce57facd
3dc919de186d1a8ee62fff92d80839f7:6d7c5b3e796d833b3fdd40f4ce57facd
7a581ac4d8cb3bfc596fce9afb115fd2:6d7c5b3e796d833b3fdd40f4ce57facd
```

Realizing the first part is MD5, I put them in [crackstation.net](https://crackstation.net/) and got:

```text
b506fb0cabb60e9f1132daa72df4d567    md5    crackstation
2ac9cb7dc02b3c0083eb70898e549b63    md5    Password1
3dc919de186d1a8ee62fff92d80839f7    Unknown    Not found.
7a581ac4d8cb3bfc596fce9afb115fd2    md5    downunder2
```

Of course, I tried the three passwords that were found and of course they weren't the flag.
So hopping through some other hash cracking sites I found [https://hashes.com/en/decrypt/hash ](https://hashes.com/en/decrypt/hash) yielding:

```text
3dc919de186d1a8ee62fff92d80839f7:ozzieozzieozzie
```

---

<details><summary>FLAG:</summary>

```
ozzieozzieozzie
```

</details>
<br/>
