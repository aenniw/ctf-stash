#### Challenge:

Agent, we have discovered a dead drop used by a foreign agency. there was nothing else but a paper with QR code and a piece of written text. Your task is to discover what secret information it contains. Good luck! Strange message found together with Q.R.
`HBSR-CCR2DC16-6X1FBU-NLWFIPTDHBH-FRLVA7G5SC3T18-V-EA2-CHT-YBY0VZ 7TZE-NAUPOL8LG-P6VO6IDMFU6ZNWFX-LIBTOMHFLAZGSYCXDT-18NF-EWAMCHJ- S-O-SJMTBY8YKTE-H-INTFUNLL-3SMG6MVDOI-DCTG18OT-MREALKAC0ZH-B5YPI LTLE-INUFLASXILFI--XV4AXOLIZD4RLTK9O6P6U4FNABHKI7-2AJ6D-F3-UB296` [Q.png](./Q.png ":ignore")

---

#### Solution:

```python
#!/usr/bin/env python

qrCode = '''
XXXXXXXXXXXXXXXX
X_X_X_X_X_X_X_XX
X_X_X_X_X__X___X
X___XX__X_X__XXX
X_X___X_XX_X_X_X
X__X__X__XX__XXX
X_X_XX____X__X_X
X_X__XXX_X_X__XX
X_XXXXXX__XXX__X
X_X_XX_X___XXXXX
X_X__X___X__XX_X
X_XXX__XX___X_XX
X_X__X__X_XXXX_X
X_XX_XXX_X_X_XXX
X______________X
XXXXXXXXXXXXXXXX
'''

message = 'HBSR-CCR2DC16-6X1FBU-NLWFIPTDHBH-FRLVA7G5SC3T18-V-EA2-CHT-YBY0VZ7TZE-NAUPOL8LG-P6VO6IDMFU6ZNWFX-LIBTOMHFLAZGSYCXDT-18NF-EWAMCHJ-S-O-SJMTBY8YKTE-H-INTFUNLL-3SMG6MVDOI-DCTG18OT-MREALKAC0ZH-B5YPILTLE-INUFLASXILFI--XV4AXOLIZD4RLTK9O6P6U4FNABHKI7-2AJ6D-F3-UB296'
msgIndex = 0
flagIndex = 0

for c in qrCode:
    if c == 'X' or c == '_':
        if c == '_':
            if message[msgIndex] == 'C':
                  if flagIndex == 18:
                    print()
                flagIndex = 1
            if flagIndex > 0 and flagIndex < 18:
                print(message[msgIndex],end="")
                flagIndex += 1
        msgIndex += 1
```

---

<details><summary>FLAG:</summary>

```
CT18-EACH-BYTE-NULL-VOID
```

</details>
