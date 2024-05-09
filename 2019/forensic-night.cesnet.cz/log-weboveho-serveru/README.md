#### Challenge:

V logu je zachycena podeřelá aktivita. Prozkoumejte ji a zjistěte, co bylo jejím cílem. [server.log.gz](./server.log.gz ":ignore")

---

#### Solution:

- decode payload

```bash
for cmd in $(cat ./server.log | awk '{ print $7 }' | tr '=' ' ' | awk '{ print $3 }' | php -R 'echo urldecode($argn)."\n";'); do \
    echo $cmd | base64 -d; echo; \
done > payload.sql
```

- reverse password based on log timestamp delays

```bash
TIMESTAMPS=`for d in $(cat ./server.log | tail -n +2 | awk '{ print $4 }' | tr -d '[' | tr -s 'Sep' '09' ); do \
    date --date="$( echo $d | sed 's/:/ /' )" +"%s"; \
done`
for t in ${TIMESTAMPS}; do
    case $(( ${t} - ${l:-${t}} )) in
    "0")
        echo -n '00';
        ;;
    "2")
        echo -n '01';
        ;;
    "4")
        echo -n '10';
        ;;
    "6")
        echo -n '11';
        ;;
    esac
    l=$t
done | perl -lpe '$_=pack"B*",$_'
```

---

<details><summary>FLAG:</summary>

```
flag{Bruce_Schneier-1826}
```

</details>
