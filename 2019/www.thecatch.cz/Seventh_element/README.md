#### Challenge:

Hi Commander,

thanks to your discovery of the drone as a false target, our radars could concentrate on the detection of the second drone. This one was classic quadcopter and our trained falcon has caught it up and took it off the sky. The last broadcast was `Seventh element down, malfunction due claws and beak in propellers`. The wreck has been completely shattered and just one operational flash drive has been rescued from the crashsite. According to the intelligence, we believe that the drone was ordered to transport some coded message to the elementary school library in city of Ostrava in order to create backup uprising centre. You have to analyse the content of the drive and decode the message.

Good luck! [Dowloand challenge file](https://owncloud.cesnet.cz/index.php/s/3xY8uberbY7fdXe) [16.2 MB, use password `7th-element2019`]

---

#### Solution:

- based on [TheCatch-18 - Sixth element](/www.thecatch.cz-18/round-2-leaked/README?id=sixth-element)
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

tar --lzma -xvf seventh_element.dd.tar.lzma
mount-lo seventh_element.dd

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

ADDR=7
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
FLAG{tPJ4-idCH-GWlh-JjL8}
```

</details>
