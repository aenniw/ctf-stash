#### Challenge:

Part 1: Mr. Boomer recently visited France and encrypted the first part of the flag using something he learned there and put the encrypted data in 3. He said, "The key to figuring out what 3 says can only be found using 1 and 2".

Part 2: Mr. Boomer encoded the second part of the flag twice, using a different method each time. All he said was that the average was 74.5.

[Part_1.zip](./Part_1.zip ":ignore"), [Part_2.zip](./Part_2.zip ":ignore")

---

#### Solution:

- `Part 1` points out that file `3` is `Vigenere`
  - file `1` is `jpeg` that contains 2 numbers `a` and `b` in [Maya numerals](https://en.wikipedia.org/wiki/Maya_numerals)
  - file `2` seems to be encrypted an based on definition of `a` and `b` its [CyberChef - Affine Cipher](<https://gchq.github.io/CyberChef/#recipe=Affine_Cipher_Decode(7,19)&input=V3F2IEx2ZiB4cCAiaG5vdkl2byI>) that reveals `The Key is "codeRed"`
  - file `3` is encrypted via `Vigenere` based on hint `recently visited France` and secret from file `2` can be used to decrypt it [CyberChef - Vigenere](<https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('codeRed')&input=aHpka3t6X3doZ19tcnlfCg>)
- `Part 2` states that flag was `encoded` twice using just differend method `avg` was `74.5`, thus total was `149`, that leads us to `base` encodings and combination of [CyberChef - base 85](<https://gchq.github.io/CyberChef/#recipe=From_Base85('!-u')&input=QW8obWdIWUhpLkFTIzRvRGZvRGk9QG1nQDEwUXRRPSk7cWQ8QzF0NTFMa1opMTIoOHAxMXRvOEg5dVtWN1FFOCU4OEUhUTsqQCY>) + [CyberChef - base 64](<https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=WVhJelgyWkFiV2xzYVVCeVgzY3hOMmhmTjJnelh6QnNaRjkzUUhra2ZRPT0>)

---

<details><summary>FLAG:</summary>

```
flag{i_see_you_ar3_f@mili@r_w17h_7h3_0ld_w@y$}
```

</details>
<br/>
