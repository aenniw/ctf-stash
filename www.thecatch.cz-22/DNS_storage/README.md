#### Challenge:

Hi, packet inspector,

biggest surprise of the day is that the AI has started to use DNS as a storage for its own information. The data are stored in TXT resource records in the zone `mysterious-delivery.tcc`. The zone is deployed on DNS servers `ns1.mysterious-delivery.thecatch.cz` and `ns2.mysterious-delivery.thecatch.cz`.

Analyze content of zone and focus on any codes for our depot steel safes (AI has changed the access code and we hope it is stored right in the DNS zone).

May the Packet be with you!

Hint: The zone is secured by DNSSEC.

---

#### Solution:

Trying the zone transfer trick from the [last year](../../www.thecatch.cz-21/Domain_Name_System/README.md) didn't work. Investigating on the issue led me to [this SO question](https://serverfault.com/questions/935075/list-all-txt-records-for-a-doman), where some commenter mentions, that it is possible to walk DNS domain if its secured by `DNSSEC`, which is exactly what the challenge hint said.


```bash
sudo apt-get install ldnsutils

# Dumping all TXT records
ldns-walk mysterious-delivery.tcc @ns1.mysterious-delivery.thecatch.cz | grep " TXT " | sort | uniq > ns.txt

# Noticing record "depot-secret-upon-flag"
dig @ns1.mysterious-delivery.thecatch.cz depot-secret-upon-flag.mysterious-delivery.tcc TXT

# Decoding base64 that it contains:
echo "RkxBR3tZcjMxLVhvWEUtNEZxOC02UElzfQ==" | base64 -d
```

---

<details><summary>FLAG:</summary>

```
FLAG{Yr31-XoXE-4Fq8-6PIs}
```

</details>
<br/>
