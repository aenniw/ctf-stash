## Basics

No matter what the challenge always starts with the basics. [Basic.jpg](./Basic.jpg ':ignore')
You need to find the flag in the format tryhackme{}

### Do images have strings?

```bash
strings ./Basic.jpg | grep tryhackme | tr -d ' '
```

<details><summary>FLAG:</summary>

```
tryhackme{7h1s_i5_wh4t_strings_d0es}
```

</details>

### Metadata or EXIF data?.....ah!! I'm so confused

```bash
identify -verbose ./Basic.jpg | grep comment | awk '{ print $2 }' | base64 -d
```

<details><summary>FLAG:</summary>

```
tryhackme{4lway5_ch3ck_m3t4da74}
```

</details>