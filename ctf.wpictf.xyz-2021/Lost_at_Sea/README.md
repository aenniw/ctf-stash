#### Challenge:

I lost me sea shanties! They are one of the few things that make me happy during the pandemic... and I accidentally deleted them. Here is the disk image. I think there's someone talking about a flag in each of the shanties, if you can manage to recover them.

*When you hear the flag ("W P I open curly bracket..."), submit it in all caps and don't include spaces

[me-shanties-disk_img.zip](./me-shanties-disk_img.zip ":ignore")

---

#### Solution:

This challenge took me more time that all other `WPICTF-21` challenges combined. First part of the challenge was quite easy, we are given `NTFS` disk image and have to recover deleted `MP3s`:

```bash
unzip me-shanties-disk_img.zip
ntfsundelete --scan me-shanties-disk.img
ntfsundelete -u -i 64-66 me-shanties-disk_img
```

We recovered three MP3s (sea shanties) and we can hear that there is synthetic voice message in them (the flag), but it's incomprehensible due to the original songs. I managed to track down the original songs without the flag, align them with single sample accuracy, invert them and merge them with their flag counterparts. This made the flag stand out more. Even with this the flag was still quite hard to understand and it took a lot of trial and error to get it right.

---

<details><summary>FLAG:</summary>

```
WPI{ICOMEFROMTHEDAYSOFTHEPIRATEBAYWHENWEWOULDTORRENTANDLEECHALLDAY}
```

</details>
<br/>
