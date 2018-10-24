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

# submit 16 CT18-N23W-RKD0-ZS2O-XCEP
#dumpChalls
#dumpFiles2

# The Eventlog<br>(2<sup>nd</sup> Round) id:1
# The Colonel<br>(2<sup>nd</sup> Round) id:2
# Sixth Element<br>(2<sup>nd</sup> Round) id:4
# The Access Validator<br>(2<sup>nd</sup> Round) id:5
# Tracing the Traveler<br>(2<sup>nd</sup> Round) id:6
# The Targets<br>(2<sup>nd</sup> Round) id:9
# The Process<br>(2<sup>nd</sup> Round) id:11
# The Real Cloud<br>(2<sup>nd</sup> Round) id:13
# Cookie 2 <br>(2<sup>nd</sup> Round) id:25

# cat public/data/sample.json | jq .[] | jq 'select(.name | contains("2<sup>"))' | jq '. | .name + " id:" + (.id | tostring)' | tr -d \"

## CHALS round 2

# submit 2 CT18-hpWx-uGVM-pyLS-F6DX # The Colonel
# submit 13 CT18-s8G7-o8Ks-0YUX-3feT # The Real Cloud
# submit 4 CT18-bBMe-A8cF-tqMD-6d8Z # Sixth Element
# submit 5 CT18-twaH-QCXG-Bt0V-xCU5 # The Access Validator
# submit 1 CT18-QnTK-50Uq-vQ5o-jAS5 # The Eventlog
# submit 9 CT18-TCrp-se9H-OKa9-7jI3 # The Targets

# Traveller:
# submit 6 CT18-7Uiz-VZrd-EhOy-MJWd # Tracing the Traveler

# Alternatively:
# submit 6 CT18-7Uiz-VZrd-FhOy-MJWd # Tracing the Traveler
# submit 6 CT18-7Ulz-VZrd-EhOy-MJWd # Tracing the Traveler
# submit 6 CT18-7Ulz-VZrd-FhOy-MJWd # Tracing the Traveler