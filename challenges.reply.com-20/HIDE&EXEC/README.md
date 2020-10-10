#### Challenge:

Virgilia is now free, R-Boy turns on again the time machine but immediately faces a challenge set by Zer0 to prevent anyone following him from the limbo zone. Only by deciphering a code can R-Boy unlock the door and use again the time machine. [coding_300.zip](./coding_300.zip ":ignore")

---

#### Solution:

```bash
#!/usr/bin/env bash

pip install zxing python-brainfuck

while true; do
    for img in ./*.png; do
        python3 -c "import zxing; print(zxing.BarCodeReader().decode('${img}').raw);" > code.txt
        
        cat code.txt | php 2>/dev/null > password.txt && password=$(cat password.txt)
        cat code.txt | python3 2>/dev/null > password.txt && password=$(cat password.txt)
        cat code.txt | node 2>/dev/null > password.txt && password=$(cat password.txt)
        cat code.txt | grep -q 'class Main {' && \
            cp code.txt code.java && \
            java code.java 2>/dev/null > password.txt && password=$(cat password.txt)
        bash code.txt 2>/dev/null > password.txt && password=$(cat password.txt)
        python3 -c "import brainfuck; b=brainfuck.to_function('$(cat code.txt)'); print(b())" > password.txt && password=$(cat password.txt)

        if [ "${password}" == "$(cat code.txt)" ] || [ -z "$password" ]; then
            cat code.txt
            exit 1
        fi
        echo ${password}
        7z x ${img%.png}.zip -p${password} >/dev/null && \
            rm -rf ${img%.png}.*
        rm -rf code.* password.txt
    done

    ls -l | grep -q '.png' || exit 0
done
```

---

<details><summary>FLAG:</summary>

```
{FLG:P33k-4-b0o!UF0undM3,Y0urT0olb0xIsGr8!!1}
```

</details>
