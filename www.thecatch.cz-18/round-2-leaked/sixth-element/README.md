#### Challenge:

Agent, the "Nth element" is codename used by foreign agent for some kind of secret data transfer. Today, we have caught the courier and seize a drive labeled `Sixth Element`. Download the image, analyze it and get the secret message. _ URL: [https://owncloud.cesnet.cz/index.php/s/Itkz1zbREfBt4QJ](./sixth_element.dd.tar.lzma ":ignore") _ Password: `the_sixth_element` Good luck, Agent

---

#### Solution:

- note: run as sudo

```bash
#!/bin/bash

function mount-lo() {
  img="$1"
  dev="$(sudo losetup --show -f -P "$img")"
  echo "$dev"
  for part in "$dev"?*; do
    if [ "$part" = "${dev}p*" ]; then
      part="${dev}"
    fi
    basepart=$(basename "$part")
    dst="/mnt/${basepart%p*}p$(printf "%03d" ${basepart##*p})"
    echo "$dst"
    sudo mkdir -p "$dst"
    sudo mount "$part" "$dst"
  done
}

function umount-lo() {
  dev="/dev/loop$1"
  for part in "$dev"?*; do
    if [ "$part" = "${dev}p*" ]; then
      part="${dev}"
    fi
    basepart=$(basename "$part")
    dst="/mnt/${basepart%p*}p$(printf "%03d" ${basepart##*p})"
    sudo umount "$dst"
    sudo rmdir "$dst"
  done
  sudo losetup -d "$dev"
}

tar --lzma -xvf sixth_element.dd.tar.lzma
mount-lo sixth_element.dd

for p in /mnt/loop*; do
    test -f ${p}/.file && \
        cat ${p}/.file || \
        printf "000000\n0x00\n"
done > parts.txt

umount-lo

function toDec() { printf "%d\n" $1; }
function fromHex() { echo $1 | xxd -r -p; }

function getPart() {
    cat ./parts.txt | sed -n "$(( $1 * 2 - 1 )) p"
}

function getAddr() {
    cat ./parts.txt | sed -n "$(( $1 * 2 )) p"
}

ADDR=6
CODE=""
while true; do

    PART=$(fromHex `getPart ${ADDR}`)
    if [[ "$PART" == "" ]]; then
        break
    fi
    CODE="$CODE$PART"
    ADDR=$(( $(toDec `getAddr ${ADDR}`) + 1 ))
done

echo $CODE
```

---

<details><summary>FLAG:</summary>

```
CT18-bBMe-A8cF-tqMD-6d8Z
```

</details>
