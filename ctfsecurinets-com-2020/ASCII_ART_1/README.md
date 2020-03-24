#### Challenge:

Beat me once again...


<font color="red">nc 3.91.74.70 1338</font>

---

#### Solution:

This task is the same as the `ASCII Art 0`. Only difference is that this time only digits and math operands ('+', '-', '*', '/') are used in the captcha, and the expected captcha solution is the (rounded integer) result of the operation.

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
    s = remote('52.73.40.215', 1338)
    
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
            
            for char in list(string.digits) + list(('+', '-', '*', '/')):
                    Art=text2art(char)
                    letter_lines = Art.split('\r\n')
                    flattened_char = transpose_flatten(letter_lines)
                    
                    ### Replace flattened character in flattened captcha if present
                    flattened_captcha = flattened_captcha.replace(flattened_char, char)
    
            print('Result:')
            result = str(int(eval(flattened_captcha)))
            print(flattened_captcha," = ", result)

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
securinets{th1s_w4s_g00d_r1ght??}
```

</details>
<br/>
