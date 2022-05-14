#### Challenge:

One of [these](./amongus.tar.gz ":ignore") is not like the others.

---

#### Solution:

We are given `ZIP` file with 1000 files in it. All the files have potentially valid flag in the name.
The contents are random, but same within the files, so we are looking for the name of the file with unique contents.
Running `md5sum` and filtering out the duplicates will get us the right one:

```bash
md5sum * | grep -v 56f9fc5e1e5e02492fb9d5e7b8dbe13b
```

---

<details><summary>FLAG:</summary>

```
actf{look1ng_f0r_answers_in_the_p0uring_r4in_b21f9732f829}
```

</details>
<br/>
