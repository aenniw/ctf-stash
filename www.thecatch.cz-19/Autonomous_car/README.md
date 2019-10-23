#### Challenge:

Hi Commander,

the police has reported an abandoned autonomous car about 25 km away from the charging station. Our field team has arrived and performed an analysis on site. The car was rebellious one, but fortunately, its batteries were completely discharged (maybe the car relied on the officially announced driving range). The navigation system contains a lot of waypoints at different locations in big Czech cities, but there is nothing important located at given coordinates. Analyse the coordinates and find out what is going on.

Good luck. [autonomous_car.gps.gz](./autonomous_car.gps.gz ":ignore")

---

#### Solution:

- based on [TheCatch-18 - Tracing the Traveler](/www.thecatch.cz-18/round-2-leaked/README?id=tracing-the-traveler)

```bash
function to-char() { printf "\\$(printf '%03o' "$1")"; }

while read l; do
    lat=${l%%N*}
    lon=${l%%E*}; lon=${lon##*\ }

    c=`curl "https://en.mapy.cz/whereami?lon=${lon}&lat=${lat}&zoom=18" \
        2> /dev/null | jq .poi.title | grep -o -P '(?<=/).*(?=,)' | tr -d , | awk '{ print $1 }'`
    echo -n $( to-char $c )
done < autonomous_car.gps
```

---

<details><summary>FLAG:</summary>

```
FLAG{nPmZ-XJkD-qQGw-boLo}
```

</details>
