#### Challenge:

Can you make it through all of the encodings? [binary.txt](./binary.txt ":ignore")

---

#### Solution:

The solution to this challenge is a series of simple decodings with encoded hint in every layer.
The first decoding is `from binary` (to 7-bit ASCII) which reveals another layer of payload and the following hint:

```
Uh-oh, looks like we have another block of text, with some sort of special encoding. Can you figure out what this encoding is? (hint: if you look carefully, you'll notice that there only characters present are A-Z, a-z, 0-9, and sometimes / and +. See if you can find an encoding that looks like this one.)
```

That obviously points to `Base64`, after decoding that, we again get a layer of payload and hint:

```
New challenge! Can you figure out what's going on here? It looks like the letters are shifted by some constant. (hint: you might want to start looking up Roman people).
```

This hints to Caesar so deciphering with the `ROT(16)` gets us another payload and another hint:

```
alright, you're almost there! Now for the final (and maybe the hardest...) part: a substitution cipher. In the following text, I've taken my message and replaced every alphabetic character with a correspondence to a different character - known as a substitution cipher. Can you find the final flag? hint: We know that the flag is going to be of the format utflag{...} - which means that if you see that pattern, you know what the correspondences for u, t, f, l a, and g are. You can probably work out the remaining characters by replacing them and inferring common words in the English language. Another great method is to use frequency analysis: we know that 'e' shows up most often in the alphabet, so that's probably the most common character in the text, followed by 't', and so on. Once you know a few characters, you can infer the rest of the words based on common words that show up in the English language.
```

So using the hint and taking a few guesses, we decrypt the `Substitution cipher` and get the flag.

For convenience, I'm attaching link to [CyberChef recipe](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space')Fork('%5C%5Cn','%5C%5Cn',false)From_Base64('A-Za-z0-9%2B/%3D',true)Fork('%5C%5Cn','%5C%5Cn',false)ROT13(true,true,16)Fork('%5C%5Cn','%5C%5Cn',false)Substitute('vtsoidahwxnjkdylgbufpkrq','utflageconrisyhwypdjbnkv')) (The forks are necessary so that the hints won't contaminate the payload.)

---

<details><summary>FLAG:</summary>

```
utflag{n0w_th4ts_wh4t_i_c4ll_crypt0}
```

</details>
<br/>
