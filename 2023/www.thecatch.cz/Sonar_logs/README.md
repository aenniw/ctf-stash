#### Challenge:

Ahoy, officer, 

each crew member must be able to operate the sonar and understand its logs. Your task is to analyze the given log file, and check out what the sonar has seen.

May you have fair winds and following seas!

Download [sonar_logs.zip](./sonar_logs.zip ":ignore").\
(MD5 checksum:` b946f87d0231fcbdbc1e76e27ebf45c7`)

---

#### Solution:

```bash
{
    while read p; do
        echo "$p" | grep 0x >/dev/null || continue
        time=${p% - *}
        timestamp=${time% *}

        echo "$(TZ=${time##* } date -d "${timestamp}" +"%s") $(echo ${p##* } | tr -d '()' | xxd -r -p)" 
    done < sonar.log;
} | sort -s -k 1 | cut -d' ' -f2 | tr -d '\n' ; echo;
```

---

<details><summary>FLAG:</summary>

```
FLAG{3YAG-2rbj-KWoZ-LwWm}
```

</details>
<br/>
