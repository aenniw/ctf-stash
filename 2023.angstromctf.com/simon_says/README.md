#### Challenge:

This guy named Simon gave me a bunch of tasks to complete and not a lot of time. He wants to run a unique zoo but needs the names for his animals. Can you help me?

`nc challs.actf.co 31402`


---

#### Solution:

This is basically a coding challenge. You just have to code a script that will solve the tasks given by the challenge correctly and fast enough to beat it before timeout:

```python
#!/env python3

from pwn import *
import re

r = remote('challs.actf.co', 31402)

while True:
    task =r.recvline().decode('utf-8').strip()
    print(task)

    match = re.search("Combine the (.*) (.*) letters of (.*) with the (.*) (.*) letters of (.*)", task)

    animal_1_chars_num = int(match[2])
    print(animal_1_chars_num)
    animal_1 = match[3]
    print(animal_1)

    animal_2_chars_num = int(match[5])
    print(animal_2_chars_num)
    animal_2 = match[6]
    print(animal_2)


    payload = animal_1[:animal_1_chars_num]+animal_2[-animal_2_chars_num:]
    print(payload)
    r.sendline(payload.encode('utf-8'))

```

---

<details><summary>FLAG:</summary>

```
actf{simon_says_you_win}
```

</details>
<br/>
