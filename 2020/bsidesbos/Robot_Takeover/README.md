#### Challenge:

You know what it is, you know what to do... but can you handle the twist? <br><br> <b>Open the <code>Deployment</code> tab to start this challenge.</b>

---

#### Solution:

```bash
#!/bin/bash

URL="http://challenge.ctf.games:30095/"

while true; do
    curl ${URL}/robots.txt 2>/dev/null > robots.txt

    AGENT=""
    while read l; do
        echo $l | grep -q 'User-agent:' && \
            AGENT=$l
        
        echo $l | grep -q 'Disallow:' && \
        {
            RESP=`curl -H "${AGENT}" ${URL}${l#* } 2>/dev/null`;
            echo ${RESP} | grep -q 'REJOICE' && \
                echo "${RESP} - ${l#* }" | sed 's/ \([0-9]\) IS/ 0\1 IS/g' >> resps.txt;
        }
    done <robots.txt

    if [ -f resps.txt ]; then
        while read l; do
            l=${l#*CHARACTER AT INDEX}
            INDEX=${l% IN*}
            NAME=${l#*- /}
            echo -n ${NAME:$INDEX:1}
        done < <( cat resps.txt | sort | uniq)
        echo
    fi
done
```

---

<details><summary>FLAG:</summary>

```
flag{beep_boop_are_you_a_robot_too}
```

</details>
<br/>
