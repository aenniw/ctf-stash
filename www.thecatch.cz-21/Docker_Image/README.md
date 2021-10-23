#### Challenge:

Hi Expert,

some leads indicates presence of interesting information in seized docker image, examine it and find what you can. 

Download the image `docker pull ghcr.io/aenniw/ctfs/python3test:latest`

Good Luck!

---

#### Solution:

- inspecting the image with [dive](https://github.com/wagoodman/dive) reveals that `/usr/sbin/init` was multiple times added and removed

```bash
docker pull ghcr.io/aenniw/ctfs/python3test:latest
docker save ghcr.io/aenniw/ctfs/python3test:latest -o image.tar
tar -xvf ./image.tar
tar -xvf ./3ffb8e574d1d978b34723bc3a2314833b5bf6b32547509e860a20f387eb0d716/layer.tar 
wget 'https://www.fontsupply.com//fonts/cour.ttf' -O cour.ttf
python3 ./usr/sbin/init -f flag

```

---

<details><summary>FLAG:</summary>

```
FLAG{DDmL-mK70-P5Kx-sfrc}
```

</details>
<br/>
