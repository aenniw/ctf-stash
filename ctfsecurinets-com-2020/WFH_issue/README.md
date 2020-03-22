#### Challenge:

Some user was suspected of sending client data from his work laptop. What did he send ? [for3.zip](./for3.zip ":ignore")

---

#### Solution:

```bash
tshark -r ./for3.pcapng -T fields -e data -Y 'icmp and data.len lt 44' | fold -w2 | uniq | tr -d '\n' |  xxd -r -p
#   pastebin
for d in $(tshark -r ./for3.pcapng -T fields -e ip.ttl -Y 'icmp and ip.ttl != 128 and ip.ttl != 64'); do
    printf \\$(printf "%o" $d);
done
#   J6cDw61m
```

- visit https://pastebin.com/J6cDw61m -> `https://anonfile.com/30g9F6ifo0/backup_pst`
- download [backup.pst](./backup.pst ":ignore")

```bash
file backup.pst # backup.pst: Microsoft Outlook email folder (>=2003)
readpst backup.pst
file ./Brouillons.mbox # contains `base64` encoded file inside
munpack ./Brouillons.mbox
binwalk -Me ./passwords.docm
grep -R -i Securinets ./_passwords.docm.extracted/*
strings ./_passwords.docm.extracted/word/vbaProject.bin
echo -n 'KNSWG5LSNFXGK5DTPMYXIXZRONPVI2BTL5FDA5LSNZCXSX2EGR2F63LBOR2DG4TTPU======' | base32 -d
```

---

<details><summary>FLAG:</summary>

```
Securinets{1t_1s_Th3_J0urnEy_D4t_matt3rs}
```

</details>
<br/>
