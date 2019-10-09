#### Challenge:

Agent, the foreign agents sometimes needs to evacuate (due to injury or disclosure) and they need to provide proper password at proper place to authorize the evacuation. Recently, we have acquired the instruction, how the agents should do it, but it does not make sense at the first sight: `Wanna stay alive forever? check.infinite.thecatch.cz dustoff.infinite.thecatch.cz` Find the sense of the message. Good luck, Agent

---

#### Solution:

```bash
var='ns.v3n06cd.infinite.thecatch.cz.'

while :
do
	dig @challenges.thecatch.cz $var >> text.txt
	var=`dig @challenges.thecatch.cz $var | grep ";; AUTHORITY SECTION:" -A 1 | grep NS | awk '{ print $5 }'`
	echo $var | grep '0x' | tr . ' ' | awk '{ print $2 }' | cut -c 3- | xxd -r -p
done
```

---

<details><summary>FLAG:</summary>

```
CT18-cHnE-oE9n-iKTT-6byx
```

</details>
