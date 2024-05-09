#### Challenge:

Nostalgic overload, at least for me. Credit due to Carolina. 

By Jeriah (@jyu on Discord) [game](./game ":ignore")

---

#### Solution:

```bash
docker run --rm -it -v $(pwd):/work -w /work ubuntu:18.04 \
    /bin/bash -c 'apt -qq update && apt install -y -qq swftools && swfstrings game' | \
    grep utflag
```

---

<details><summary>FLAG:</summary>

```
utflag{they_kn0w}
```

</details>
<br/>
