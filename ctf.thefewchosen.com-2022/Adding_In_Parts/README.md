#### Challenge:

I stored my data in multiple files for extra security. But they all got corrupted somehow.

NOTE: The flag IS in TFCCTF{...} format. No need to add that part yourself. Beware of flag-like strings

[add_parts.zip](./add_parts.zip ":ignore")

---

#### Solution:

We are given `ZIP` archive containing 22 `ZIP` archives with names `0.zip` upto `21.zip`. Each of these ZIPs contain only one file with `single character` in it. Printing the chars in order of the filenames reveals string which isn't the flag. While we were extracting the individual `ZIPs`, we got warning about the `CRC` checksum of the extracted file being different from the one recorded in `ZIP`. Since the files hold only one character, we can bruteforce their original contents by cracking the CRC hashes from the `ZIP` files to get the flag.

```python
import string
import zlib

zip_crcs=[
  {'id': '00', 'val': "be047a60"},
  {'id': '01', 'val': "4dbd0b28"},
  {'id': '02', 'val': "3dd7ffa7"},
  {'id': '03', 'val': "3dd7ffa7"},
  {'id': '04', 'val': "be047a60"},
  {'id': '05', 'val': "4dbd0b28"},
  {'id': '06', 'val': "15d54739"},
  {'id': '07', 'val': "06b9df6f"},
  {'id': '08', 'val': "916b06e7"},
  {'id': '09', 'val': "6dd28e9b"},
  {'id': '10', 'val': "06b9df6f"},
  {'id': '11', 'val': "0862575d"},
  {'id': '12', 'val': "1b0ecf0b"},
  {'id': '13', 'val': "f26d6a3e"},
  {'id': '14', 'val': "e101f268"},
  {'id': '15', 'val': "1ad5be0d"},
  {'id': '16', 'val': "29d6a3e8"},
  {'id': '17', 'val': "01d41b76"},
  {'id': '18', 'val': "f4dbdf21"},
  {'id': '19', 'val': "0f0f9344"},
  {'id': '20', 'val': "98dd4acc"},
  {'id': '21', 'val': "fcb6e20c"},
]

for k in zip_crcs:
    for char in list(string.printable):
        if int(hex(zlib.crc32(char.encode('ascii')) & 0xffffffff), 16) == int("0x"+k["val"], 16):
            print(char, end="")
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{ch3cksum2_g0od}
```

</details>
<br/>
