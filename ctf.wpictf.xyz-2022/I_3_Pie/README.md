#### Challenge:

I dropped my pie in the laundry machine and it got all spun around :(

Flag:
`lxm{wsuwaxbweqiutekwvtl}`

Creator: emalcxe!

---

#### Solution:

This gave me a bit of a head ache, I realized quite quickly that this is `Vigenere's` cipher with the key `pie` because entering it in [CyberChef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('pie')&input=bHhte3dzdXdheGJ3ZXFpdXRla3d2dGx9) correctly deciphered the `wpi` flag prefix, but the content of the flag was still mangled.

The problem was the `{` of the flag. The CyberChef's implementation correctly ignored it, as it isn't in its alphabet, but it didn't use the letter of the key on it. I bypassed it by replacing the `{` and `}` with `X` and then reverting them in the decrypted flag - see [CyberChef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('pie')&input=bHhtWHdzdXdheGJ3ZXFpdXRla3d2dGxYCg). Another possible solution would be to specify the key repetitions manualy and skipping the `{`'s position like this - `pieiepiepiepiepiepiepi`, which gives - [CyberChef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('pieiepiepiepiepiepiepi')&input=bHhte3dzdXdheGJ3ZXFpdXRla3d2dGx9Cg).

---

<details><summary>FLAG:</summary>

```
wpi{oofowitspieflavored}
```

</details>
<br/>
