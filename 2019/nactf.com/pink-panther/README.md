#### Challenge:

Rahul loves the Pink Panther. He even made this website:

http://pinkpanther.web.2019.nactf.com

I think he hid a message somewhere on the webpage, but I don't know where... can you INSPECT and find the message?

https://www.youtube.com/watch?v=2HMSnfeNf8c

---

#### Solution:

```bash
curl http://pinkpanther.web.2019.nactf.com 2>/dev/null | grep nactf
```

---

<details><summary>FLAG:</summary>

```
nactf{1nsp3ct_b3tter_7han_c10us3au}
```

</details>
