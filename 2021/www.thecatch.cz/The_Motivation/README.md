#### Challenge:

Hi Expert,

one of the discovered servers on IP `78.128.216.7` was somehow used to increase the motivation and morale of people. At least the chief archaeologist thinks so. Have a closer look.

Good Luck!

---

#### Solution:

```bash
nmap -p- 78.128.216.7
# PORT      STATE    SERVICE
# 17/tcp    open     qotd
# 65000/tcp filtered unknown
```
- `nc 78.128.216.7 17` returns citations of famous people, and between them hint `Once a correct sequence of connection attempts is received, the firewall rules are dynamically modified to allow the host. Sequence of three ports is 65000 + {DNS, LDAP, Syslog). Btw. look at 65000 again.  - The Catcher`

```bash
for PORT in 65053 65389 65514; do
    nmap -Pn --host-timeout 100 --max-retries 0 -p $PORT 78.128.216.7
done
nc 78.128.216.7 65000
```

---

<details><summary>FLAG:</summary>

```
FLAG{qC6Z-dQS7-4qoC-tR1m}
```

</details>
<br/>
