#### Challenge:

Agent, a list of coordinates was quietly downloaded from car navigation, which belongs to agent "Traveler". Our psychotronic department believes that some message is encoded in it. Try to find it. Good luck, [message.txt](./message.txt ":ignore")

---

#### Solution:

```bash
#!/bin/bash

function to-char() { printf "\\$(printf '%03o' "$1")"; }

while read l; do
    lat=${l%%N*}
    lon=${l%%E*}; lon=${lon##*\ }

    c=`curl "https://en.mapy.cz/whereami?lon=${lon}&lat=${lat}&zoom=18" \
        2> /dev/null | jq .poi.title | grep -o -P '(?<=/).*(?=,)' | tr -d , | awk '{ print $1 }'`
    echo -n $( to-char $c )
done < message.txt
```

---

<details><summary>FLAG:</summary>

```
CT18-TCrp-se9H-OKa9-7jI3
```

</details>
