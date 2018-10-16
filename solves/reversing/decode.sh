#!/bin/bash

function toChar() {
	printf "\\$(printf '%03o' "$1")"
}

for o in `cat ./access_validator.vbs`; do toChar $o;done

