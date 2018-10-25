#!/bin/bash

# fdisk -lu  ./sixth_element.img
# for p in /mnt/loop*p*;do cat $p/.file || { echo 000000; echo 0x00; };done > parts-all.txt

function toDec() { printf "%d\n" $1; }
function fromHex() { echo $1 | xxd -r -p; }

function getPart() {
	cat ./parts.txt | sed -n "$(( $1 * 2 - 1 )) p"
}

function getAddr() {
	cat ./parts.txt | sed -n "$(( $1 * 2 )) p"
}

ADDR=6
CODE=""
while true; do
	
	PART=$(fromHex `getPart ${ADDR}`)
	#echo "$ADDR `getAddr ${ADDR}` $PART"
	if [[ "$PART" == "" ]]; then
		break
	fi
	CODE="$CODE$PART"
	ADDR=$(( $(toDec `getAddr ${ADDR}`) + 1 ))
done

echo $CODE