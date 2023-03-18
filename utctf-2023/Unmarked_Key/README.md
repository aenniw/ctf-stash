#### Challenge:

The flag submission server's been down for a month. I SSHed in and it turns out the filesystem's completely gone - it won't let you run any commands.

I know there's open SSH access on port 1134 (and conveniently, there's a bridge on the same port on guppy.utctf.live). I also know it's supposed to have an HTTPS server running on port 443, but of course that's not running. I don't recall the actual domain name, but I managed to salvage both the private key and the certificate, so I think you can get it from those.

...what do you mean, "the other half of the certificate?" You're talking about the private key, right? No?

Oh shoot, the filesystem corruption was worse than I thought.

By Jonathan (JBYoshi#5551 on Discord) [privkey.pem](./privkey.pem ":ignore"), [cert-part.pem](./cert-part.pem ":ignore")

---

#### Solution:

```bash
```

---

<details><summary>FLAG:</summary>

```
utflag{dd_if_dev_random_of_dev_sda}
```

</details>
<br/>
