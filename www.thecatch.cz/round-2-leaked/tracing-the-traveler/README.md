#### Challenge:

Agent, a list of coordinates was quietly downloaded from car navigation, which belongs to agent "Traveler". Our psychotronic department believes that some message is encoded in it. Try to find it. Good luck, [message.txt](./message.txt)

---

#### Solution:

```bash
#!/bin/bash

function to-char() { printf "\\$(printf '%03o' "$1")"; }

for c in `cat message.txt | \
		while read l; do
			lat=${l%%N*}
			lon=${l%%E*}; lon=${lon##*\ }

			# echo "https://en.mapy.cz/whereami?lon=${lon}&lat=${lat}&zoom=18"
			curl "https://en.mapy.cz/whereami?lon=${lon}&lat=${lat}&zoom=18" \
				2> /dev/null | jq .poi.title | grep -o -P '(?<=/).*(?=,)' | tr -d , | awk '{ print $1 }'
		done`; do
	to-char $c
done
echo
```

---

<details><summary>FLAG:</summary>

```
CT18-7Uiz-VZrd-EhOy-MJWd
```

</details>
