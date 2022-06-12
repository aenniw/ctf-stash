#### Challenge:

One of the interns, Ducky, accidentally posted DUCTF data publicly, he said he was successful in scrubbing it from what he called "CTF clock" and mentioned the number four hundred and four ¯\\_(ツ)_/¯.

Ducky wouldn't screw up twice would he?

---

#### Solution:

The term "CTF Clock" most probably hints at `CTFTime`. Since the description mentions `404`, we assumed that the page is supposed to be already deleted. With this info in mind and considering the challenge name we tried [the Waybackmachine](https://web.archive.org/web/20210314105546/http://ctftime.org/event/1312) on the CTF event and found that there was a record before the event started with content:

```text
404
Not found. Back to the main page.

Ok, ok — here is your flag: a5abef5222adc680a453607384bcb4d2
```

This is standard 404 page for the `CTFtime`, but this time it was actually used as a flag.

---

<details><summary>FLAG:</summary>

```
DUCTF{a5abef5222adc680a453607384bcb4d2}
```

</details>
<br/>
