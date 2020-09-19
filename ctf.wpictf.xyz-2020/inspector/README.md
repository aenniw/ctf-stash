#### Challenge:

my sources tell me that the flag might be at `wpictf.xyz`

---

#### Solution:

Going to the site [https://wpictf.xyz/](https://wpictf.xyz/) and `inspecting` the source code we find:

```html
<!-- If you are looking for a WPI{FLAG}, you CANT be a robot! -->
```

So [https://wpictf.xyz/robots.txt](https://wpictf.xyz/robots.txt) gives us:

```robots
User-agent: * Disallow: /inspector.txt
```

The [https://wpictf.xyz/inspector.txt](https://wpictf.xyz/inspector.txt) returns:

```text
I heard that the WPICSC club webpage may be of use to you.
```

Googling for `WPICSC club` lands us at [https://web.cs.wpi.edu/~csc/index.html](https://web.cs.wpi.edu/~csc/index.html)

Which contains one red herring in the source:

```html
<!-- VGhpcyBzaXRlIGlzIHB1cmVseSBpbmZvcm1hdGlvbi4gQnV0IHdlIGFwcHJlY2lhdGUgdGhlIGVmZm9ydCBkZWNvZGluZyB0aGlzLg== -->
```

which decodes to:

```text
This site is purely information. But we appreciate the effort decoding this.
```

and also the next clue:

```html
<!-- Check out our prizes-->
```

Source code of the [https://ctf.wpictf.xyz/prizes](https://ctf.wpictf.xyz/prizes) finally contains the flag.

---

<details><summary>FLAG:</summary>

```
WPI{1nsp3ct0r_H@ck3R}
```

</details>
<br/>
