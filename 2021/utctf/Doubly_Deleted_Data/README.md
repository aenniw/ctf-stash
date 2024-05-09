#### Challenge:

We got a copy of an elusive hacker's home partition and gave it to someone back in HQ to analyze for us. We think the hacker deleted the file with the flag, but before our agent could find it, they accidentally deleted the copy of the partition! Now we'll *never* know what that flag was. :(

[flash_drive.img.tar.lzma](./flash_drive.img.tar.lzma ":ignore")

---

#### Solution:

We are presented with hard drive image. I think the chalange creator wanted us to recover partition and on it recover some deleted file or check command history or something, but I found simpler faster way...

```bash
strings flash_drive.img | grep utflag
```

---

<details><summary>FLAG:</summary>

```text
utflag{d@t@_never_dis@ppe@rs}
```

</details>
<br/>
