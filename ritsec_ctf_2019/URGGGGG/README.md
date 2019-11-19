#### Challenge:

One of our operatives sent us this packet capture but we aren't quite sure what to make of it, what can you find? [URGGGGGG.pcapng](./URGGGGGG.pcapng ":ignore")

---

#### Solution:

```python
#!/usr/bin/python3

usb_codes = {
    0x04: "aA", 0x05: "bB", 0x06: "cC", 0x07: "dD", 0x08: "eE", 0x09: "fF",
    0x0A: "gG", 0x0B: "hH", 0x0C: "iI", 0x0D: "jJ", 0x0E: "kK", 0x0F: "lL",
    0x10: "mM", 0x11: "nN", 0x12: "oO", 0x13: "pP", 0x14: "qQ", 0x15: "rR",
    0x16: "sS", 0x17: "tT", 0x18: "uU", 0x19: "vV", 0x1A: "wW", 0x1B: "xX",
    0x1C: "yY", 0x1D: "zZ", 0x1E: "1!", 0x1F: "2@", 0x20: "3#", 0x21: "4$",
    0x22: "5%", 0x23: "6^", 0x24: "7&", 0x25: "8*", 0x26: "9(", 0x27: "0)",
    0x2C: "  ", 0x2D: "-_", 0x2E: "=+", 0x2F: "[{", 0x30: "]}",  0x32: "#~",
    0x33: ";:", 0x34: "'\"",  0x36: ",<",  0x37: ".>",
}


def remove_at(i, s):
    return s[:i] + s[i+1:]


def insert_at(i, s, v):
    return s[:i-1] + v + s[i-1:]


row = 0
col = 0
lines = [""]
last_key_code = ''
for x in open("keystrokes.txt", "r").readlines():
    code = int(x[6:8], 16)
    if code == last_key_code:
        continue

    if code == 0x4f:
        col += 1
    elif code == 0x50:
        col -= 1
    elif code == 0x51:
        row -= 1
    elif code == 0x52:
        row += 1
        if len(lines) == row:
            lines.append(' ' * col)
    elif code == 0x4c:
        lines[row] = remove_at(col+1, lines[row])
        col -= 1
    elif code == 0x2a:
        lines[row] = remove_at(col, lines[row])
        col -= 1
    elif code == 0x28:
        row += 1
        col = 0
        lines.insert(row, "")
    elif code not in usb_codes:
        continue
    elif int(x[0:2], 16) == 2:
        lines[row] += usb_codes[code][1]
        col += 1
    else:
        lines[row] += usb_codes[code][0]
        col += 1
    last_key_code = code

for l in lines:
    print(l)

```

---

<details><summary>FLAG:</summary>

```
RITSEC{wH0_s@id_n3tw0rk1nG_wAs_tH3_oNlY_pAck3t_TyP3}
```

</details>
<br/>
