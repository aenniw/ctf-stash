#### Challenge:

TheEmperor created an HTML form where he was trying to show that he can store his password there without any risk thanks to his faithful guards that will prevent anyone from getting access to the flag.

For simplicity reason, he knows that obfuscating so much the code would decrease its performance. That's why he only remained on his guards and for another simplicity reason, he didn't want to put a compact code (the code is beautified) since the objective is to test how powerful are his guards.

Now, bypass TheEmperor's guards and get a full access to the empire with his mighty flag. 

`web3.q21.ctfsecurinets.com`

---

#### Solution:

- download the `javascript` source files from web page and dissect `validateform` function for flag [script.js](./script.js ":ignore")

```javascript
    var success = !![];
    for (var index = -0x1037 + 0x29 + 0x100e; index < flag[_0x5f5794(0xa1)]; index++) {
        if (_0x5546f5[_0x5f5794(0xad)] !== _0x5546f5[_0x5f5794(0xad)]) {
            var _0x41c282 = function_2;
            var _0x359702 = function_1;
            var _0x1c6b37 = new _0x4aebe7(_0x359702(0x18a));
            var _0x5e8359 = new _0x275431(kBQUsu[_0x359702(0xee)], 'i');
            var _0x17968b = kBQUsu[_0x359702(0x104)](_0x5ebb60, kBQUsu[_0x41c282(0x181, 'c68O')]);
            if (!_0x1c6b37[_0x359702(0xbd)](kBQUsu[_0x41c282(0xc0, 'Lzxu')](_0x17968b, kBQUsu[_0x41c282(0xa0, '7G[7')])) || !_0x5e8359[_0x41c282(0x170, '#NgI')](_0x17968b + kBQUsu[_0x359702(0x167)])) {
                kBQUsu[_0x41c282(0xab, '7G[7')](_0x17968b, '0');
            } else {
                kBQUsu[_0x359702(0xa6)](_0x34b632);
            }
        } else {
            process.stdout.write(flag[index][index]);
        }
    }
    console.log()
    process.exit(1)
    if (success)
        _0x5546f5[_0x5f5794(0xaf)](console.log, _0x5546f5[_0x487fdb(0x157, '#NgI')]);
    return ![];
```

```bash
node script.js
```

---

<details><summary>FLAG:</summary>

```
Securinets{TheEmeror_grant_you_s4f3ty_in_th3_Empire}
```

</details>
<br/>
