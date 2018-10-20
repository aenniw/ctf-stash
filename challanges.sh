#!/bin/bash

SESSION=`cat session.txt 2>/dev/null`
NONCE=`cat nonce.txt 2>/dev/null`

function urlEncode() {
    old_lc_collate=$LC_COLLATE
    LC_COLLATE=C
    
    local length="${#1}"
    for (( i = 0; i < length; i++ )); do
        local c="${1:i:1}"
        case $c in
            [a-zA-Z0-9.~_-]) printf "$c" ;;
            *) printf '%%%02X' "'$c" ;;
        esac
    done
    
    LC_COLLATE=$old_lc_collate
}

function login() {
    USER=${1}
    PASSWORD=${2}
    
    curl -c - 'https://www.thecatch.cz/login' 2>/dev/null  | grep -E 'csrf_nonce|session' > session-tmp.txt
    NONCE=`cat ./session-tmp.txt | grep nonce | awk '{ print $4 }' | tr -d \"`
    SESSION=`cat ./session-tmp.txt | grep session | awk '{ print $7 }'`
    rm ./session-tmp.txt
    
    SESSION=`curl -c - 'https://www.thecatch.cz/login' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -H "Cookie: session=$SESSION"  \
    --data "name=${USER}&password=${PASSWORD}&nonce=${NONCE}" \
    --compressed 2>/dev/null | grep session | awk '{ print $7 }'`
    echo $SESSION > session.txt
    
    NONCE=`curl 'https://www.thecatch.cz/challenges' \
    -H "Cookie: session=$SESSION" --compressed 2>/dev/null | grep csrf_nonce | awk '{ print $4 }' | tr -d \"`
    echo $NONCE > nonce.txt
}

function get() {
    CHALLANGE=$1
    
    curl "https://www.thecatch.cz/chals/${CHALLANGE}" \
    -H "Cookie: session=$SESSION"  \
    -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
    --compressed 2>/dev/null | jq .
}

function dumpChalls() {
    echo '['
    for i in `seq 1 28`; do
        get $i
        if [[ $i -lt 28 ]];then
            echo ','
        fi
    done
    echo ']'
}

function dumpFiles2() {
    for f in `dumpChalls | jq .[] | jq 'select(.name | contains("2<sup>"))' | jq .files[] | tr -d \"`; do
        echo "$f"
        wget --header="Cookie: session=$SESSION" \
        https://www.thecatch.cz/files/$f
    done
}

function submit() {
    CHALLANGE=$1 # '16'
    FLAG=${2} # 'CT18-N23W-RKD0-ZS2O-XCEP'
    
    curl "https://www.thecatch.cz/chal/${CHALLANGE}" \
    -H "Cookie: session=$SESSION"  \
    -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
    --data "key=${FLAG}&nonce=${NONCE}" \
    --compressed 2>/dev/null | jq .
}

function validSession() {
    if curl https://www.thecatch.cz/team \
    -H "Cookie: session=$SESSION"  \
    2>/dev/null | grep -q login; then
        return 1
    else
        return 0
    fi
}

if ! validSession ;then
    login $( urlEncode $CTF_USER ) $( urlEncode $CTF_PASS )
fi

#dumpChalls
#dumpFiles2

#submit 16 CT18-N23W-RKD0-ZS2O-XCEP
