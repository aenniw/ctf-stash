#!/bin/bash

# declare -a arr=("Monday"
# "Tuesday"
# "Wednesday"
# "Thursday"
# "Friday"
# "Saturday"
# "Sunday")

declare -a arr=("Tuesday")


for i in "${arr[@]}"
do
   python Roche.py "48024325d765d74677381378554d" "$i"  | xxd -r -p
   python Roche.py "2c650d5380073602407d94440000" "$i"  | xxd -r -p
done
