#### Challenge:

In the heart of the Misc Realm, R-Boy prepares for the decisive battle. He never expected to encounter an old foe: the master of the digital underworld in this realm is Zer0, someone he knows well. The atmosphere grows increasingly tense, and Zer0 reveals an ace up his sleeve: an extremely advanced Artificial Intelligence called "Nethra," programmed to predict and counter every move R-Boy makes. However, it seems that some clues for gaining an advantage have been disguised.

[misc-100.zip](./misc-100.zip ":ignore")

---

#### Solution:

- inspecting the `email` and reading through it point us to look into `png` attributes where next hint show us the `zip` password format
```
# Artist                          : birthDateMail***R3ply!
# Copyright                       : checkArtistFieldForPwdFormat
```
- all the required information is already provided in `email` so we need to build the wordlist and crack the zip

- build the `wordlist`` for testing
```python
import itertools
import string

chrs = string.ascii_letters + string.digits + string.punctuation

n = 3
for xs in itertools.product(chrs, repeat=n):
    password = ("900802jfeng@veryrealmail.com" + ''.join(xs) + "R3ply!")
    print(password)
```

- as the `zip` cannot be opened with `unzip` also `fcrackzip` fails to do so we reverted directly using `7z`

```bash
python3 ./wordlist.py > words.txt

for p in `cat ./words.txt`; do
    rm flag.txt 2>/dev/null;
    7z x ./important_dental_information.zip -p${p} >/dev/null 2>/dev/null;
    [ -s ./flag.txt ] && { echo $p; cp ./flag.txt "flag.$p.txt"; };
done

cat ./flag.*.txt | grep '{FLG:'
```

---

<details><summary>FLAG:</summary>

```
{FLG:J4n1c3_h4s_g0t_s0m3_b4d_t33th}
```

</details>
