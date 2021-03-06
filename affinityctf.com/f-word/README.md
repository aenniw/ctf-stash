#### Challenge:

`^^^^!^^^^*-A?*--&-----&&^^^&*^!^^^*-A?*^&!^^^^^*-A?*--&*^^!^^*-----A?*&-!^^^^^*-A?*^^&^!^^^^^*-A?*&*^!^^^*-A?*^^&!^^^*-A?*---&-!^*---A?*&^!^*------A?*&---!^*--A?*&--!^*-----A?*&^^!^^^*--A?*&^^^^^^^^^^^^&^^^&*^!^^^*-A?*^^^&-------------&-!^^^*--A?*--&^^^!^^^^^*-A?*^&---!^*---A?*--&--------&-----&^!^*---A?*^&^!^^^*--A?*^&^!^^^^^*--A?*^&^!--*^^^A?*^&!^^^^^*-A?*--&^^^^^^^^^^^^^^&^^^^^&-!^*---A?*-&&&*^^!^^*---A?*&`

---

#### Solution:

- bruteforce

```bash
function bfs() {
    echo '^^^^!^^^^*-A?*--&-----&&^^^&*^!^^^*-A?*^&!^^^^^*-A?*--&*^^!^^*-----A?*&-!^^^^^*-A?*^^&^!^^^^^*-A?*&*^!^^^*-A?*^^&!^^^*-A?*---&-!^*---A?*&^!^*------A?*&---!^*--A?*&--!^*-----A?*&^^!^^^*--A?*&^^^^^^^^^^^^&^^^&*^!^^^*-A?*^^^&-------------&-!^^^*--A?*--&^^^!^^^^^*-A?*^&---!^*---A?*--&--------&-----&^!^*---A?*^&^!^^^*--A?*^&^!^^^^^*--A?*^&^!--*^^^A?*^&!^^^^^*-A?*--&^^^^^^^^^^^^^^&^^^^^&-!^*---A?*-&&&*^^!^^*---A?*&'
}

for s1 in '+' '-' '>' '<' ']' '.' ; do
    for s2 in '+' '-' '>' '<' ']' '.' ; do
        [[ ${s1} == ${s2} ]] && continue;
        for s3 in '+' '-' '>' '<' ']' '.' ; do
            [[ ${s3} == ${s1} || ${s3} == ${s2} ]] && continue;
            for s4 in '+' '-' '>' '<' ']' '.' ; do
                [[ ${s4} == ${s1} || ${s4} == ${s2} || ${s4} == ${s3} ]] && continue;
                for s5 in '+' '-' '>' '<' ']' '.' ; do
                    [[ ${s5} == ${s1} || ${s5} == ${s2} || ${s5} == ${s3}  || ${s5} == ${s4} ]] && continue;
                    for s6 in '+' '-' '>' '<' ']' '.' ; do
                        [[ ${s6} == ${s1} || ${s6} == ${s2} || ${s6} == ${s3}  || ${s6} == ${s4} || ${s6} == ${s5} ]] && continue;
                        bfs | tr '-' "${s1}" \
                            | tr '&' "${s2}" \
                            | tr '?' "${s3}" \
                            | tr 'A' "${s4}" \
                            | tr '^' "${s5}" \
                            | tr '*' "${s6}" \
                            | tr '!' '[' > /tmp/bfs
                        timeout 1s bf /tmp/bfs 2>/dev/null | grep "AFFCTF"
                    done
                done
            done
        done
    done
done
```

- or encode `AFFCTF{` via [brainfuck](https://copy.sh/brainfuck/text.html) compare and substitute

```bash
bfs | tr '&' '.' \
    | tr '?' ']' \
    | tr 'A' '<' \
    | tr '-' '+' \
    | tr '^' '-' \
    | tr '!' '[' \
    | tr '*' '>' > /tmp/bfs
bf /tmp/bfs
```

---

<details><summary>FLAG:</summary>

```
AFFCTF{JuSt_4n0theR_BrainF-w0rd_!!!}
```

</details>
