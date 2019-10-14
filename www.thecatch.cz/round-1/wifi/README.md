#### Challenge:

Agent, you are in critical situation, you desperately need to connect to the network and send intel to our headquarters, but there is no LTE. The only way is to connect to encrypted wifi. Are you able to connect? The login form is here: http://challenges.thecatch.cz/Wifi.php Good luck, Agent

---

#### Solution:

```bash
PASSWD=`curl https://ubee.deadcode.me/index.php?ssid=UPC3946855 2>/dev/null | grep -i "647c3411eaa0" | awk '{ print $5 }'`
curl 'http://challenges.thecatch.cz/Wifi.php' --data "password=${PASSWD}&submit=Submit" 2>/dev/null | grep "CT18"
```

---

<details><summary>FLAG:</summary>

```
CT18-Yy90-AkfF-x4S5-sQuy
```

</details>
