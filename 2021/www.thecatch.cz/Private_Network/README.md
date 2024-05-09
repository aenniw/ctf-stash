#### Challenge:

Hi Expert,

the archaeologists have found some network scheme (we suppose that mentioning the ancient cave painting was just a joke) and they think that there exists some very important web server in network `10.20.32.0/21`. The same scheme indicates that IP address `78.128.216.8` should be used to get access to private network. Get the data from above mentioned web server.

Good Luck!

---

#### Solution:

- expand the network subnet range to addresses and check each for response

```bash
while read p; do 
    echo -n "$p "; curl -x 78.128.216.8:3128 "http://$p" -v 2>&1 | grep 'HTTP/1.1 ';
done <hosts.csv

curl -x 78.128.216.8:3128 "http://10.20.35.11"
```

---

<details><summary>FLAG:</summary>

```
FLAG{XG5T-WLWl-HqjH-2E7V}
```

</details>
<br/>
