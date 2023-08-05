#### Challenge:

I've included the flag in as shell command. Can you retrieve it?

I recommend using the [volatility3](https://github.com/volatilityfoundation/volatility3) software for this challenge.

Here is the memory dump: [debian11.core.zst](https://utexas.box.com/s/fehluzyox4bbgfjlz061r2k7k2sek3cw)
This problem also comes with a free profile! [debian11_5.10.0-21.json.zst](https://utexas.box.com/s/g64kezqvkqhm6nw79oovcekn9z1w66q0)
Both of these files are compressed using `zstd`.

This challenge's flag looks like a UUID.

> Note: the volatility challenges do not have a flag format to discourage grepping. They all should be possible without guessing. If you have trouble, remember that you can ask for help.

By Daniel Parks (@danielp on discord)

---

#### Solution:

Pretty standard volatility challenge, but you have to use `volatility3` and put the symbols to its place before running the `linux.bash.Bash` module. The flag is the single bash command present.

```bash
git clone https://github.com/volatilityfoundation/volatility3.git
unzstd ./debian11.core.zst
unzstd ./debian11_5.10.0-21.json.zst
cp ./debian11_5.10.0-21.json ./volatility3/volatility3/symbols
python3 ./volatility3/vol.py isfinfo
python3 ./volatility3/vol.py -f ./debian11.core linux.bash.Bash
```

---

<details><summary>FLAG:</summary>

```
08ffea76-b232-4768-a815-3cc1c467e813
```

</details>
<br/>
