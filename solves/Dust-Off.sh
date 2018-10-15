#!/bin/bash

var='ns.v3n06cd.infinite.thecatch.cz.'

while :
do
	dig @challenges.thecatch.cz $var >> text.txt
	var=`dig @challenges.thecatch.cz $var | grep ";; AUTHORITY SECTION:" -A 1 | grep NS | awk '{ print $5 }'`
	echo $var | grep '0x'
done
