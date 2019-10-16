#### Challenge:

While doing his mission preparation tests, R-boy notices in the file he's reading that the data has been inserted in a mysterious order. Read the text with him and discover what's behind it. [jumpyrinth.zip](./jumpyrinth.zip ":ignore")

---

#### Solution:

```python
#!/usr/bin/env python3

file = '2c464e58-9121-11e9-aec5-34415dec71f2.txt'

index = 0
flag = []
stack = []
data = []

with open(file, 'r') as f:
    for l in f:
        line = []
        for c in l:
            if c != '\r' or c != '\n':
                line.append(c)
        data.append(line)


def lookup_begin():
    global index

    lindex = 0
    for l in range(0, len(data)):
        for c in range(0, len(data[l])):
            lindex += 1
            if data[l][c] == '$' and lindex > index:
                index = lindex
                return (l + 1, c)
    exit(0)


def get_op(pos):
    d = data[pos[0]][pos[1]]
    return d


def process_op(op, pos):
    global flag
    global begin

    if op == '>':
        j = ''
        n = ''
        p = 1
        while n == '' or (ord(n) >= ord('0') and ord(n) <= ord('9')):
            j = j + n
            n = get_op((pos[0], pos[1] - p))
            p += 1
        return (pos[0], pos[1] + int(j))
    elif op == '<':
        j = ''
        n = ''
        p = 1
        while n == '' or (ord(n) >= ord('0') and ord(n) <= ord('9')):
            j = j + n
            n = get_op((pos[0], pos[1] + p))
            p += 1
        return (pos[0], pos[1] - int(j))
    elif op == '^':
        j = ''
        n = ''
        p = 1
        while n == '' or (ord(n) >= ord('0') and ord(n) <= ord('9')):
            j = j + n
            n = get_op((pos[0] + p, pos[1]))
            p += 1
        return (pos[0] - int(j), pos[1])
    elif op == 'v':
        j = ''
        n = ''
        p = 1
        while n == '' or (ord(n) >= ord('0') and ord(n) <= ord('9')):
            j = j + n
            n = get_op((pos[0] - p, pos[1]))
            p += 1
        return (pos[0] + int(j), pos[1])
    elif op == ']':
        stack.append(get_op((pos[0], pos[1] - 1)))
        return (pos[0], pos[1] - 2)
    elif op == '[':
        stack.append(get_op((pos[0], pos[1] + 1)))
        return (pos[0], pos[1] + 2)
    elif op == '*':
        stack.append(get_op((pos[0] - 1, pos[1])))
        return (pos[0] - 2, pos[1])
    elif op == '.':
        stack.append(get_op((pos[0] + 1, pos[1])))
        return (pos[0] + 2, pos[1])
    elif op == '-':
        flag = flag[1:]
        j = ''
        n = ''
        p = 1
        while n == '' or (ord(n) >= ord('0') and ord(n) <= ord('9')):
            j = j + n
            n = get_op((pos[0] + p, pos[1]))
            p += 1
        return (pos[0] - int(j), pos[1])
    elif op == '+':
        flag = flag[:-1]
        j = ''
        n = ''
        p = 1
        while n == '' or (ord(n) >= ord('0') and ord(n) <= ord('9')):
            j = j + n
            n = get_op((pos[0] - p, pos[1]))
            p += 1
        return (pos[0] + int(j), pos[1])
    elif op == '%':
        flag = list(reversed(flag))
        return (pos[0] + 1, pos[1])
    elif op == '(':
        flag.insert(0, stack.pop())
        j = ''
        n = ''
        p = 1
        while n == '' or (ord(n) >= ord('0') and ord(n) <= ord('9')):
            j = j + n
            n = get_op((pos[0], pos[1] + p))
            p += 1
        return (pos[0], pos[1] - int(j))
    elif op == ')':
        flag.append(stack.pop())
        j = ''
        n = ''
        p = 1
        while n == '' or (ord(n) >= ord('0') and ord(n) <= ord('9')):
            j = j + n
            n = get_op((pos[0], pos[1] - p))
            p += 1
        return (pos[0], pos[1] + int(j))
    elif op == '@':
        print(''.join(flag))
        flag.clear()
        stack.clear()
        return lookup_begin()
    exit(1)


pos = lookup_begin()

while True:
    op = get_op(pos)
    pos = process_op(op, pos)

```

---

<details><summary>FLAG:</summary>

```
{FLG:H4ckItUpH4ckItInL33tM3B3g1n}
```

</details>
