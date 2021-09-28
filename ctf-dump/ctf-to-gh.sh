#!/bin/bash

# NOTE: snap install gh to create GH issues
# ./ctf-to-gh.sh ./ctf-directory/ https://ctf-url/

CTF_DIR=${1%/*}
CTF_URL=${2}
CTF_NAME=${CTF_DIR##*/}
CTF_SUMMARY=${CTF_DIR}/README.md

echo -e "**[${CTF_NAME}](${CTF_URL})**\n\n---\n" > $CTF_SUMMARY
for dir in ${CTF_DIR}/*/; do
    CATEGORY=${dir#${CTF_DIR}/}; CATEGORY=${CATEGORY%%/*};
    echo -e "# ${CATEGORY}\n" >> $CTF_SUMMARY
    
    for file in ${dir}/*/README.md; do
        CHALLENGE=${file%/*}; CHALLENGE=${CHALLENGE##*/};
        echo -e "## ${CHALLENGE}\n" >> $CTF_SUMMARY
        echo -e "[${CHALLENGE}](./${CHALLENGE}/README.md \":include\")\n" >> $CTF_SUMMARY

        mv ${dir}${CHALLENGE} ${dir%/*/*}

        hash gh 2>/dev/null && \
            gh issue create \
                --title "[${CTF_NAME}] - ${CHALLENGE} writeup" \
                --label "writeup" \
                --body ""
    done
    rmdir ${dir}
done