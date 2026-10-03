#### Challenge:

Ahoy, officer,

 some of the crew started behaving strangely after eating the chef's speciality of the day -  they apparently have hallucinations, because they are talking about sirens wailing,  kraken on starboard, and accussed the chef being reptilian spy. Paramedics are getting crazy, because the chef refuses to reveal what he used to make the food. Your task is to find his secret recipe. It should be easy as the chef knows only security by obscurity and he has registered domain `chef-menu.galley.cns-jv.tcc`. 
May you have fair winds and following seas!

The chef's domain is `chef-menu.galley.cns-jv.tcc`.

---

#### Solution:

This is a web reconnaissance task. The hint "security by obscurity" points at
something hidden in plain sight on the chef's site rather than a real
vulnerability. The trick is that the flag is placed in an HTML element that a
browser never renders, and that element is only present on the plain **HTTP**
response — opening the site in a browser is useless because the server bumps the
connection straight to HTTPS (an HSTS/redirect to `https://`), so I never get to
look at the raw HTTP body visually.

So instead of a browser I fetch the plain HTTP version directly with `curl`,
which happily shows me the raw markup without following the redirect dance:

```bash
curl http://chef-menu.galley.cns-jv.tcc
# the host was reachable only by IP during the event, e.g.:
curl http://10.99.0.32
```

Reading through the returned HTML, there is a paragraph deliberately hidden with
`display: none` — invisible in a browser, but plainly there in the source:

```html
<p style="display: none">The secret ingredient is composed of C6H12O6, C6H8O6, dried mandrake, FLAG{....-....-....-....}, and C20H25N3O. Shake, do not mix.</p>
```

The "ingredients" are a bit of flavour (glucose, ascorbic acid, a mythical root,
and C20H25N3O — the formula for LSD, which explains the crew's hallucinations),
and the flag sits right in the middle of the recipe.

> Note: the challenge host `chef-menu.galley.cns-jv.tcc` is offline now, so I
> could not re-run this live — the above is verified by reasoning from the raw
> HTTP response captured during the event.

---

<details><summary>FLAG:</summary>

```
FLAG{ytZ6-Pewo-iZZP-Q9qz}
```

</details>
<br/>
