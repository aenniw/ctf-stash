#### Challenge:


---

#### Solution:

```bash
for c in $(strings list.pcap | grep -i command=echo | sed 's/command=echo+%22\(.*\)base64.*/\1/'); do
    echo -n $(echo $c | base64 -d 2>/dev/null | awk '{print $6}'| tr -d '"')
done; echo;
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{b4s3_64_isnt_that_g00d}
```

</details>
<br/>
