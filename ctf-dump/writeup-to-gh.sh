#!/bin/bash

# NOTE: snap install gh to create GH pull request
# execute from CTF directory so that PR is created per changed directory
# ./writeup-to-gh.sh CTF-NAME reviewer-name

CTF=$1
REVIEWER=$2

git reset
base=$(git rev-parse --abbrev-ref HEAD)
for chal in $(git status . | grep modified | sed 's/.*modified:[ \t]*//g' | sed 's/\/.*$//g'); do
    git branch "writeup/${chal// /-}"
    git checkout "writeup/${chal// /-}"
    git add "./${chal}"
    git commit -S -m "Add ${CTF} - ${chal} writeup"
    git push origin "writeup/${chal// /-}"

    if hash gh 2>/dev/null; then
        issue=$(gh issue list -a @me -S "${chal}" | cut -f 1)
        gh pr create \
            -B "${base}" \
            -b "Closes #${issue}" -l "writeup" \
            -t "Add ${CTF} - ${chal} writeup" \
            --reviewer "${REVIEWER}" -a @me 
    fi

    git checkout "${base}"
done