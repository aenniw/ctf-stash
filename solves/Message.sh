#!/bin/bash

function to-char() { printf "\\$(printf '%03o' "$1")"; }

for c in `cat ../public/data/message.txt | \
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