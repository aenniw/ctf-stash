#### Challenge:

I think someone downloaded something from an http site. Luckily I caught the traffic. I'm super curious about what it was. Let's go hunt! (doo, doo, doo, doo, doo, doo)


[baby_shark1.pcap](./baby_shark1.pcap ":ignore")

---

#### Solution:

We are provided with `PCAP` file. Even without the hint in the challenge name, I'd open it in `Wireshark` to see HTTP request for `flag.png`.
Then its just clicking:

```
File -> Export Objects -> HTTP... -> (Select the one with flag.png) -> Save
```

---

<details><summary>FLAG:</summary>

```
utflag{eye_c_what_u_c}
```

</details>
<br/>
