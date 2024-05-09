#### Challenge:

Beat me...


<font color="red">nc 3.91.74.70 1337</font>

---

#### Solution:

After connecting to provided endpoint we are greeted with information that says, that we need to solve ASCII art captchas. There is quite short timeout and more than one captcha needed to by solved in order to get the flag. Luckily, I was able to find the [library](https://pypi.org/project/art/) that generated exactly the same asci art characters as those in the challenge, so there was no manual categorizing needed. Only problem left to solve is how to compare the characters. The characters in captchas had different widths, but always the same heights (7 lines). I have transposed and flattened this two-dimensional array by reading it column by column from top to bottom, while excluding the line endings (which were windows BTW). This way I got single flattened captcha string, where all bytes representing single captcha character are grouped together. Then I iterated over all alphanumerical characters and for each I generated it's ascii art form, convert it into transposed flattened string and simply did search and replace on transposed flattened captcha string. After the iteration the string contained only resolved captcha.

```python
#!/usr/bin/env python

from pwn import *
from art import *

def transpose_flatten(chaptcha_string):
    LINE_LENGTH = len(chaptcha_string[0])
    flattened_captcha = ""
    for y in range (0, LINE_LENGTH):
        for x in range (0,6):
            flattened_captcha = flattened_captcha + chaptcha_string[x][y]
    return flattened_captcha

try:
    s = remote('52.73.40.215', 1337)
    
    try:
        print('skip', s.recvline())
        print('skip', s.recvline())
        print('skip', s.recvline())

        while True:
            print('Captcha:')
            print('#################')
            captcha_lines = []
            for x in range (0,6):
                captcha_lines.append(s.recvline().decode('UTF-8').replace('\r\n',''))
                print(captcha_lines[x])
            print('#################')

            flattened_captcha = transpose_flatten(captcha_lines)
            print(flattened_captcha)
            print(len(flattened_captcha))
            
            for char in list(string.ascii_lowercase+string.ascii_uppercase+string.digits):
                    Art=text2art(char)
                    letter_lines = Art.split('\r\n')
                    flattened_char = transpose_flatten(letter_lines)

                    ### Replace flattened character in flattened captcha if present
                    flattened_captcha = flattened_captcha.replace(flattened_char, char)

            print('Result:')
            print(flattened_captcha)

            s.sendline(result)

            ## Read and print char-by-char until next prompt is found
            while True:
                tmp = s.recv()
                print(tmp)
                if ( '>' in str(tmp)):
                    break

    finally:
        s.close()
except Exception as e:
    raise
```

---

<details><summary>FLAG:</summary>

```
securinets{w3ll_d0n3_g00d!!}
```

</details>
<br/>
