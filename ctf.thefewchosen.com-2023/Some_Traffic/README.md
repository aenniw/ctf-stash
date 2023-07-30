#### Challenge:

Our SOC analysts said that in the last few days, some of our employees started to upload a lot of photos on random sites. Check it out.

Flag Format: TFCCTF{...}.

*Disclaimer (forensics+stegano)*

[sus.pcapng](./sus.pcapng ":ignore")

---

#### Solution:

Opening the PCAP file in `wireshark` and looking around we can see there are `3 PNGs` sent to some evildomain. Because I'm lazy, and also because exporting HTTP objects via `wireshark` didn't work, I run `foremost -T -i sus.pcapng` which extracted 2 of the PNGs, but there was nothing special about them.

The 3rd PNG was probably not extracted by foremost, because there were some requests in between the chunks, so I saved the HTTP stream containing the 3rd PNG as raw bytes (`right-click -> Follow -> HTTP Stream` -> Show data as `Raw` -> `Save as...`).

Running foremost again on the raw output file gives the 3rd PNG. On it are 2 raceflags in the background and `3 green matrix-like columns` of 1 pixel width. This indicates data encoded in the image, so I run the `stegsolve` on it and data extract revealed the flag in
the `green plane` extracted by `column`.

---

<details><summary>FLAG:</summary>

```
TFCCTF{H1dd3n_d4t4_1n_p1x3ls_i5n't_f4n_4nd_e4sy_ to_f1nd!}
```

</details>
<br/>
