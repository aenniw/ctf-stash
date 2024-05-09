#### Challenge:

Can you make it through all of the encodings and ciphers? [secret.txt](./secret.txt ":ignore")

---

#### Solution:

The challenge is classical series of encodings. The first is conversion from `binary`, then `base64` and finally `Caesar cipher` rotated by 16 chars. [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)Fork('%5C%5Cn','%5C%5Cn',false)From_Base64('A-Za-z0-9%2B/%3D',true)Fork('%5C%5Cn','%5C%5Cn',false)ROT13(true,true,false,16)) is your friend.

---

<details><summary>FLAG:</summary>

```text
utflag{now_youre_playing_with_crypto}
```

</details>
<br/>
