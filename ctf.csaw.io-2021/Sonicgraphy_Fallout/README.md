#### Challenge:

A hacker named Blue_Blur was recently arrested and is accused of hiding some evidence. The evidence was reported to have been hidden in the hacker's OC Sonic comic. See if you can find any hidden files. Reportedly, it was a 'video' of some sort. On the other hand, the comics are pretty good. Enjoy! :)

Credit goes to Deebs/Fini-mun for the artwork of the comics. [Fallout-New_Mobius.png](./Fallout-New_Mobius.png ":ignore")

---

#### Solution:

- `stego-toolkit` reveals that one of the files `Page 7.png` contains additional data appended to `PNG`
```bash
docker run -it --rm -v "$(pwd)":/data  -w /data dominicbreuker/stego-toolkit check_png.sh ./Page 7.png
```
- after extracting if we see that its `ISO Media, MP4 v2 [ISO 14496-14]` file containing the flag

![sonic.png](./sonic.png ":ignore")

---

<details><summary>FLAG:</summary>

```
flag{R011in6_@r0und_@_7h3_$p33d_0f_50und}
```

</details>
<br/>
