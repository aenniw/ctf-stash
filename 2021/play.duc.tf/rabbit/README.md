#### Challenge:

Can you find Babushka's missing vodka? It's buried pretty deep, like 1000 steps, deep. [flag.txt](./flag.txt ":ignore")

---

#### Solution:

```bash
#/bin/bash

mkdir tmp
cp flag.txt ./tmp/
cd tmp

changed=true
while $changed == "true"; do
    changed=false

    while file $(ls) | grep -q 'bzip2'; do
        bzip2 -d $(ls);
        changed=true
    done

    while file $(ls) | grep -q 'Zip'; do
        f=$(ls)
        mv "${f}" "${f}.zip"
        unzip "${f}.zip" && rm "${f}.zip";
        changed=true
    done

    while file $(ls) | grep -q 'XZ'; do
        f=$(ls)
        mv "${f}" "${f}.xz"
        unxz "${f}.xz"
        changed=true
    done

    while file $(ls) | grep -q 'gzip'; do
        f=$(ls)
        mv "${f}" "${f}.gz"
        gzip -d  "${f}.gz"
        changed=true
    done

done

cat $(ls) | base64 -d
echo

cd ..
rm -rf tmp/
```

---

<details><summary>FLAG:</summary>

```
DUCTF{babushkas_v0dka_was_h3r3}
```

</details>
<br/>
