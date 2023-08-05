#### Challenge:

I have been snooping on the [conversations](./admiral_shark.pcapng ":ignore") of my elusive enemies. See if you can help me gather the information I need to defeat them once and for all.

---

#### Solution:

Looking at the traffic, we see TCP communication and fuzzied binary data. Trying `binwalk` on the `pcapfile`, it shows that there is a `zip` file somewhere in the communication. Carve it out and grep for flag:

```bash
binwalk -Me admiral_shark.pcapng
grep -r actf _admiral_shark.pcapng.extracted
```

---

<details><summary>FLAG:</summary>

```
actf{wireshark_in_space}
```

</details>
<br/>
