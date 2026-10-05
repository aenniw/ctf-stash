#### Challenge:

Hi Associate Researcher,

The National Research and Education Network (NREN) has many experts, such as is Dr. Simon Dvorak, Chair of the Committee for Strategic QWERTY Decommissioning, member of 17 working groups, editor of 42 draft documents, and self-proclaimed "Home Row Evangelist".

Yesterday, Dr. Dvorak briefly visited a shared workstation in the NREN office. Without looking at the keyboard, he quickly typed an important document, saved it, and left for following National QWERTY Transition Initiative meeting.

Unfortunately, the resulting document appears to be complete nonsense. Your task is to recover the correct document.

Stay curious!

Download the [dr_dvoraks_document.zip](./dr_dvoraks_document.zip ":ignore").\
(SHA256 checksum: `1b10f088e53772993ed6b628e9cb4f2846f848d203a4f94248ae90baeaa83fed`)

Hints:
- The workstation was configured with the standard QWERTY layout.
- Mr. Dvorak produced the document at an astonishing speed while several of Dvorak enthusiasts chanted in support "One layout! One home row! Dvorak Simplified!".

---

#### Solution:

The archive contains a single `dr_dvoraks_document.txt` full of gibberish:

```
Hdao isppdaufd;w ;frrsokdo;w alh kjs;d ,js aod ;kgpp f;glu X<DOKTw
...
Ks sfo ld, ;frrsokdo;w G ;atZ kjd csfoldt ,gpp nd ijappdluglue Yogdlh; mat xfd;kgsl tsfo ijsgid;e Yamgpt mdmndo; mat odyf;d ks ;,gkij patsfk;e :kat ;kosluw kjglv ansfk YPAU_NIcM'6:rS'J>rG'L13N+e ...
```

Dr. Dvorak touch-typed with **Dvorak Simplified Keyboard** muscle memory on a machine set to **QWERTY**.
Every character in the file is therefore the QWERTY key sitting at the physical position where the intended Dvorak character is.
Reversing it is a simple per-key substitution (QWERTY character -> Dvorak character on the same key, including shifted symbols; the number row is identical):

```python
#!/usr/bin/env python3
# Typed with Dvorak muscle memory on a QWERTY machine: map QWERTY key -> Dvorak char at same position.
import sys
qwerty = "-=qwertyuiop[]asdfghjkl;'zxcvbnm,./" + '_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'
dvorak = "[]',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz" + '{}"<>PYFGCRL?+AOEUIDHTNS_:QJKXBMWVZ'
t = str.maketrans(qwerty, dvorak)
data = open(sys.argv[1], encoding="utf-8", errors="replace").read() if len(sys.argv) > 1 else sys.stdin.read()
sys.stdout.write(data.translate(t))
```

```bash
unzip dr_dvoraks_document.zip
python3 decode.py dr_dvoraks_document.txt | grep -oE 'FLAG\{[^}]*\}'
```

The decoded document is a speech of the new Coordinator of the National QWERTY Transition Initiative:

```
Dear colleagues, supporters, and those who are still using QWERTY,
...
Stay strong, think about FLAG{BCjM-6SpO-HVpI-N13B}. Every great change begins with a remapping file.
...
```

(The raw flag `YPAU_NIcM'6:rS'J>rG'L13N+` maps `_`->`{`, `'`->`-`, `+`->`}`.)

---

<details><summary>FLAG:</summary>

```
FLAG{BCjM-6SpO-HVpI-N13B}
```

</details>
<br/>
