#### Challenge:

R-Boy finds the time machine, which Zer0 used to travel to another era. Nearby, lies a copy of HG Wells’ The Time Machine. Could this book from the past help R-Boy travel in time? Unfortunately, R-Boy can’t read or understand it, because the space-time continuum has changed some of the words. Help R-Boy to start his time travels! [coding-100.zip](./coding-100.zip ":ignore")

---

#### Solution:

We are given `HG Wells’ The Time Machine` with malformed words and wordlist with correct words which we are supposed to use to fix malformed words. The difference between malformed and correct words should give us the secret message containing the flag. Since this book is freely available from [Project Gutenberg](http://www.gutenberg.org/files/35/35-0.txt), I decided to compare the malformed text to the original which should be faster than `miss-spelling detection` with wordlist, but Gutenberg version contained some errors in ligature which needed to be fixed manually, like characters `æ -> ae`, `œ -> oe` `… -> ...` and etc, but after detecting and fixing these we were able to get the flag.

```bash
# download Wells from Project Gutenberg
wget http://www.gutenberg.org/files/35/35-0.txt -O gutenberg_wells.txt

# delete gutenberg header
sed '0,/START OF THIS PROJECT GUTENBERG EBOOK THE TIME MACHINE/d' -i gutenberg_wells.txt

# delete gutenberg footer
sed -n '/End of the Project Gutenberg EBook of The Time Machine, by H. G. Wells/q;p' -i gutenberg_wells.txt

# change Windows line endings to Unix in both files
sed 's/\r//g' -i gutenberg_wells.txt
sed 's/\r//g' "The Time Machine by H. G. Wells.txt" > challange.txt

# delete empty lines from both files
sed '/^$/d' -i gutenberg_wells.txt
sed '/^$/d' -i challange.txt

# remove dots after chapter numbers
sed -r 's/^( [IVX]*I)\.$/\1/g' -i gutenberg_wells.txt
sed -r 's/^( [IVX]*V)\.$/\1/g' -i gutenberg_wells.txt
sed -r 's/^( [IVX]*X)\.$/\1/g' -i gutenberg_wells.txt

# "normalize" some characters or words
sed 's/“/"/g' -i gutenberg_wells.txt
sed 's/”/"/g' -i gutenberg_wells.txt
sed "s/’/'/g" -i gutenberg_wells.txt
sed "s/‘/'/g" -i gutenberg_wells.txt
sed 's/—/--/g' -i gutenberg_wells.txt
sed 's/…/.../g' -i gutenberg_wells.txt
sed 's/æ/ae/g' -i gutenberg_wells.txt
sed 's/œ/oe/g' -i gutenberg_wells.txt
sed 's/arroused/aroused/g' -i gutenberg_wells.txt
```

```python
#!/usr/bin/env python3

import os
import difflib

original_lines = open('gutenberg_wells.txt').readlines()
changed_lines = open('challange.txt').readlines()

original_text = "".join(original_lines)
changed_text = "".join(changed_lines)
diff_text = ""

for char in range(len(original_text)-8):

    ## Find place where three consecutive characters don't match, which indicates a mistake in "original" text
    # if original_text[char] != changed_text[char] and original_text[char+1] != changed_text[char+1]:
    #     print(original_text[char]+original_text[char+1]+original_text[char+2]+original_text[char+3]+original_text[char+4]+original_text[char+5]+original_text[char+6]+original_text[char+7]+original_text[char+8])
    #     print(changed_text[char]+changed_text[char+1]+changed_text[char+2]+changed_text[char+3]+changed_text[char+4]+changed_text[char+5]+changed_text[char+6]+changed_text[char+7]+original_text[char+8])
    #     break

    if original_text[char] != changed_text[char]:
        diff_text = diff_text+changed_text[char]

print(diff_text)
```

```bash
python3 diff.py | grep -Poe {FLG:.*?}
```

---

<details><summary>FLAG:</summary>

```
{FLG:1_kn0w_3v3ryth1ng_4b0ut_t1m3_tr4v3ls}
```

</details>
