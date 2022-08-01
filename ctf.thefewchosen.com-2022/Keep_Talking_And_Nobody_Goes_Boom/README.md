#### Challenge:

Just have fun playing this with a teammate!

(... or, you know, a bot that could solve these fast enough)

---

#### Solution:

```python
from pwn import *
from struct import *
import base64
from collections import Counter


# if there are more than 2 red wires, cut the third and fifth wire
# if the third wire is green, cut the first wire
# if there are less than 5 wires, ignore the next rule and cut wire 3
# if the second to last wire is blue, cut it
# if no rules apply cut wires 2 and 6
def solveKey1(msg):
    wires = msg.split('|')
    wire_count = Counter(wires)
    key = []
    if wire_count['RED'] > 2:
        key.append(3)
        key.append(5)
    if wires[2] == 'GREEN':
        key.append(1)
    if len(wires) < 5:
        key.append(3)
    else:
        if not wires[0] == 'BLUE' and (wire_count['BLUE'] + 1) == len(wires):
            for i in range(1, len(wires)):
                key.append(i+1)

    if len(key) == 0:
        key = [2, 6]

    key = ' '.join([str(x)for x in key])
    return key


# cut the third black wire
# if there are less than 10 blue wires and more than 20 red ones, cut the first two blue wires
# if there are more green wires than black ones, cut the wires adjacent to the ones on positions 3, 16 and 21
def solveKey21(msg):
    wires = msg.split('|')
    wire_count = Counter(wires)
    key = []
    count = 0
    for i in range(0, len(wires)):
        if wires[i] == 'BLACK':
            count += 1
            if count == 3:
                key.append(i + 1)
                break
    if wire_count['BLUE'] < 10 and wire_count['RED'] > 20:
        count = 0
        for i in range(0, len(wires)):
            if wires[i] == 'BLUE':
                count += 1
                if count < 3:
                    key.append(i + 1)
                else:
                    break
    if wire_count['GREEN'] > wire_count['BLACK']:
        for i in [2, 4, 15, 17, 20, 22]:
            key.append(i)
    key = ' '.join([str(x)for x in key])
    return key


# cut the wire equal to the number of white wires
# if there are more green wires than blue and red wires combined, cut the wires 5, 20, 27 and 31
# if you are the first player that joined the game, cut all wires
# if the number of red wires is divisible by 2, cut ALL the wires adjacent to the ones stated at rule 2
# if the 14th wire is blue, cut it
def solveKey22(msg):
    wires = msg.split('|')
    wire_count = Counter(wires)
    key = []
    key.append(wire_count['WHITE'])
    if wire_count['GREEN'] > wire_count['BLUE'] + wire_count['RED']:
        for i in [5, 20, 27, 31]:
            key.append(i)
    if not int(wire_count['RED']/2) - wire_count['RED'] / 2 < 0:
        for i in [4, 6, 19, 21, 26, 28, 30, 32]:
            key.append(i)
    if wires[14] == 'BLUE':
        key.append(14)
    key = ' '.join([str(x)for x in key])
    return key


context.log_level = 'error'

r1 = remote("01.linux.challenges.ctf.thefewchosen.com", 50754)
r2 = remote("01.linux.challenges.ctf.thefewchosen.com", 50754)
print('1', r1.recvuntil(b'Press any key to start...').decode('utf-8').strip())
print('2', r2.recvuntil(b'Press any key to start...').decode('utf-8').strip())

r1.sendline()
r2.sendline()

print('1', r1.recvuntil(b'Have fun!').decode('utf-8').strip())
print('2', r2.recvuntil(b'Have fun!').decode('utf-8').strip())

print('####################################################################')

msg = r1.recvuntil(b"Don't share it with anyone!").decode('utf-8').strip()
print('1', msg)
print('2', r2.recvuntil(b'What is the secret key?').decode('utf-8').strip())
key2 = msg.split("key: ")[1].split(" Don't")[0]
r2.sendline(key2.encode())
print('2', key2)

print('####################################################################')

print('1', r1.recvuntil(b'...\n\n\n').decode('utf-8').strip())
print('2', r2.recvuntil(b'...\n\n\n').decode('utf-8').strip())

msg = base64.b64decode(r2.recvline()).decode('utf-8').strip()
print('1', base64.b64decode(r1.recvline()).decode('utf-8').strip())
print('2', msg)
key1 = msg.split("key: ")[1].split(" Don't")[0]
r1.sendline(key1.encode())
print('1', key1)


print('####################################################################')

print('2', r2.recvuntil(b'Instructions:\n\n').decode('utf-8').strip())
print('2', r2.recvline().decode('utf-8').strip())
print('2', r2.recvline().decode('utf-8').strip())
print('2', r2.recvline().decode('utf-8').strip())
print('2', r2.recvline().decode('utf-8').strip())
print('2', r2.recvline().decode('utf-8').strip())

print('1', r1.recvuntil(b'These are the wires of the bomb:\n\n').decode('utf-8').strip())
msg = r1.recvline().decode('utf-8').strip()
print('1', msg)
print('1', r1.recvline().decode('utf-8').strip())
print('1', r1.recvline().decode('utf-8').strip())

wires1 = solveKey1(msg)
r1.sendline(wires1.encode())
print('1', wires1)


print('####################################################################')

print('1', r1.recvuntil(b'Instructions:\n\n').decode('utf-8').strip())
print('1', r1.recvuntil(
    b'These are the wires of your bomb:\n\n').decode('utf-8').strip())
msg1 = r1.recvline().decode('utf-8').strip()
print('1', msg1)
print('1', r1.recvuntil(
    b'What wires do YOU need to cut? (Separate them by SPACE | Indexing starts from 1)\n').decode('utf-8').strip())

print('2', r2.recvuntil(b'Instructions:\n\n').decode('utf-8').strip())
print('2', r2.recvuntil(
    b'These are the wires of your bomb:\n\n').decode('utf-8').strip())
msg2 = r2.recvline().decode('utf-8').strip()
print('2', msg2)
print('2', r2.recvuntil(
    b'What wires do YOU need to cut? (Separate them by SPACE | Indexing starts from 1)\n').decode('utf-8').strip())

wires21 = solveKey21(msg1)
r1.sendline(wires21.encode())
print('1', wires21)

wires22 = solveKey22(msg2)
r2.sendline(wires22.encode())
print('2', wires22)

print('####################################################################')

print('1', r1.recvuntil(b'Hmmm 5 seconds for you!\n').decode('utf-8').strip())
print('2', r2.recvuntil(b'Hmmm 5 seconds for you!\n').decode('utf-8').strip())

keys1 = "".join(f"{ord(i):08b}" for i in (key1 + key2))
r1.sendline(keys1.encode())
print('1', key1, key2, keys1)

keys2 = "".join(f"{ord(i):08b}" for i in (key2 + key1))
r2.sendline(keys2.encode())
print('2', key2, key1, keys2)

print('####################################################################')
print('####################################################################')

for i in range(0, 2):
    print("1", r1.recvline().decode('utf-8').strip())
    print("2", r2.recvline().decode('utf-8').strip())

r1.close()
r2.close()
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{Y0U_n33d_t34mmA73s_7o_f0rM_4_73aM}
```

</details>
<br/>
