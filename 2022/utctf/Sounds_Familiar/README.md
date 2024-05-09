#### Challenge:

You have one new message. Main menu. To listen to your messages press 1. [super_strange.wav](./super_strange.wav ":ignore")

---

#### Solution:

Playing the provided `WAV` file I realized the sounds are `DTMF`. Using this [site](https://unframework.github.io/dtmf-detect/#/) I decoded the tones to:

```
100888210610071905578878610699109864888508912081681081029071571029810957488812286111817274108102816161
```

The digits seem like ASCII characters if split correctly:

```
100 88 82 106 100 71 90 55 78 87 86 106 99 109 86 48 88 50 89 120 81 68 108 102 90 71 57 102 98 109 57 48 88 122 86 111 81 72 74 108 102 81 61 61
```

[Converting them to characters gives Base64 string which holds the flag.](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)From_Base64('A-Za-z0-9%2B/%3D',true)&input=MTAwIDg4IDgyIDEwNiAxMDAgNzEgOTAgNTUgNzggODcgODYgMTA2IDk5IDEwOSA4NiA0OCA4OCA1MCA4OSAxMjAgODEgNjggMTA4IDEwMiA5MCA3MSA1NyAxMDIgOTggMTA5IDU3IDQ4IDg4IDEyMiA4NiAxMTEgODEgNzIgNzQgMTA4IDEwMiA4MSA2MSA2MQ)

---

<details><summary>FLAG:</summary>

```
utctf{5ecret_f1@9_do_not_5h@re}
```

</details>
<br/>
