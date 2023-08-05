#### Challenge:

The flag submission server's been down for a month. I SSHed in and it turns out the filesystem's completely gone - it won't let you run any commands.

I know there's open SSH access on port 1134 (and conveniently, there's a bridge on the same port on guppy.utctf.live). I also know it's supposed to have an HTTPS server running on port 443, but of course that's not running. I don't recall the actual domain name, but I managed to salvage both the private key and the certificate, so I think you can get it from those.

...what do you mean, "the other half of the certificate?" You're talking about the private key, right? No?

Oh shoot, the filesystem corruption was worse than I thought.

By Jonathan (JBYoshi#5551 on Discord) [privkey.pem](./privkey.pem ":ignore"), [cert-part.pem](./cert-part.pem ":ignore")

---

#### Solution:

As we get just part of the certificate the goal is to get the full one and forward the remote traffic to local server. Thankfully we can download it, if we know the `hostname` of the original server at `crt.sh`.

- first we need to figure out the `hostname`. This could be done via service [https://search.censys.io/](https://search.censys.io/) where we can lookup certificates based on their public keys.

```bash
openssl rsa -in privkey.pem -modulus -noout
```

- with this we can build our search query `parsed.subject_key_info.rsa.modulus: EC4CB9EA9999980C83AFD1F6D59FDFD013600DD018E882AF2DF7CBD992B92A832B909E55D42FF4D1BCF466AFA6DA7EF8E26DBED65AF0E656D483EF940305316309D252D62612AB9EC43C4163438C74685B5A8C8B1BC7BC6664009DB3BFE2058E3F78973BA55C9AFD1FEBA5278ADB476534D39BA1BBB93928E1BA88126F154B5911FDDFFF0367F737CCC3E54493D56AE73422172752F209C96C0B2FFD6571DE163E5AA14FF69F2978381A46999B9A443A9182E53F2D8AB0D0231C911C3C9A7A824E24E34A130EA81D6CADC4F0860063CF50008E21BD3157976B7E4D5C8A2E4CA10AC97D867C86D160A12D953A5F6DAC4E1C6F79A948906629187D1D52C7761CC7` [search.censys.io](https://search.censys.io/search?resource=certificates&q=parsed.subject_key_info.rsa.modulus%3A+EC4CB9EA9999980C83AFD1F6D59FDFD013600DD018E882AF2DF7CBD992B92A832B909E55D42FF4D1BCF466AFA6DA7EF8E26DBED65AF0E656D483EF940305316309D252D62612AB9EC43C4163438C74685B5A8C8B1BC7BC6664009DB3BFE2058E3F78973BA55C9AFD1FEBA5278ADB476534D39BA1BBB93928E1BA88126F154B5911FDDFFF0367F737CCC3E54493D56AE73422172752F209C96C0B2FFD6571DE163E5AA14FF69F2978381A46999B9A443A9182E53F2D8AB0D0231C911C3C9A7A824E24E34A130EA81D6CADC4F0860063CF50008E21BD3157976B7E4D5C8A2E4CA10AC97D867C86D160A12D953A5F6DAC4E1C6F79A948906629187D1D52C7761CC7) that reveals that the `hostname` is `u-please-t-hack-c-this-t-site-f-2023.mooo.com`, unfortunately, certificate here is revoked, so we can't use it.
- here comes into play another service - [crt.sh](https://crt.sh/?q=u-please-t-hack-c-this-t-site-f-2023.mooo.com+), where we can lookup and download old certificates based on `hostname` and just by validating against the part that we have, we have the winner [8743563548](https://crt.sh/?id=8743563548).

- setup remote port forwarding `ssh -p 1134 guppy.utctf.live -R 34.201.13.237:443:localhost:8080`
- start local server that will log the traffic

```js
const https = require("https");
const fs = require("fs");

const express = require("express");

const app = express();

https
    .createServer(
        {
            key: fs.readFileSync("privkey.pem"),
            cert: fs.readFileSync("cert.pem"),
        },
        app
    )
    .listen(8080, () => {
        console.log("server is runing at port 8080");
    });

app.get('*', (req, res) => {
    console.log(req.originalUrl, req.body)
})
```

- sadly we run into issue `TLS error detected: Error (UNABLE_TO_VERIFY_LEAF_SIGNATURE): unable to verify the first certificate` as the `cert.pem` is not full-chain but that can be quickly fixed by [tools.keycdn.com](https://tools.keycdn.com/certificate-chain)

```console
server is runing at port 8080
/submit?flag=utflag{dd_if_dev_random_of_dev_sda} undefined
/submit?flag=utflag{dd_if_dev_random_of_dev_sda} undefined
/submit?flag=utflag{dd_if_dev_random_of_dev_sda} undefined
/submit?flag=utflag{dd_if_dev_random_of_dev_sda} undefined
/submit?flag=utflag{dd_if_dev_random_of_dev_sda} undefined
```

---

<details><summary>FLAG:</summary>

```
utflag{dd_if_dev_random_of_dev_sda}
```

</details>
<br/>
