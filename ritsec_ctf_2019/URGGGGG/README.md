#### Challenge:

One of our operatives sent us this packet capture but we aren't quite sure what to make of it, what can you find? [URGGGGGG.pcapng](./URGGGGGG.pcapng ":ignore")

---

#### Solution:

```bash
tshark -r ./URGGGGGG.pcapng -Y "((usb.transfer_type == 0x01) && !(usb.capdata == 00:00:00:00:00:00:00:00))" -T fields -e usb.capdata > keystrokes.txt
```

- Keyboard HID translation table [usb_hid_keys.h](https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2)

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
    0x33: ";:", 0x34: "'\"",  0x36: ",<",  0x37: ".>"
}

row = 0
lines = [""]
prev_key_code = None
for packet in open("keystrokes.txt", "r").readlines():
    packet = packet.replace(':', '')

    ctrl_pressed = int(packet[:2], 16) in [0x01, 0x10]
    shift_pressed = int(packet[:2], 16) in [0x02, 0x20]
    key_code = int(packet[4:6], 16)

    if key_code == prev_key_code:
        continue
    prev_key_code = key_code

    if key_code in [0x51, 0x28]:
        if len(lines) <= row + 1:
            lines.append("")
        row += 1
    elif key_code == 0x52:
        row -= 1
    elif key_code == 0x2a:
        lines[row] += "\b"
    elif key_code == 0x4c:
        lines[row] += "d̼"
    elif key_code == 0x4f:
        lines[row] += "»"
    elif key_code == 0x50:
        lines[row] += "«"
    elif key_code in usb_codes:
        key = usb_codes[key_code][1] if shift_pressed else usb_codes[key_code][0]
        if not ctrl_pressed:
            lines[row] += key
        elif key in "cC":
            lines[row] += 'c̼'
        elif key in "vV":
            lines[row] += 'v̼'

print("\n".join(lines).replace("«»", ""))

```

---

<details><summary>FLAG:</summary>

```
RITSEC{wH0_s@id_n3tw0rk1nG_wAs_tH3_oNlY_pAck3t_TyP3}
```

</details>
<br/>
