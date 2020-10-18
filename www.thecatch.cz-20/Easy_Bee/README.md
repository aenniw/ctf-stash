#### Challenge:

Hi, junior investigator!

We have for you something malicious called "Easy Bee". We believe that you can analyze it and found what is its purpose. [easy_bee.tar.xz](./easy_bee.tar.xz ":ignore")

Good Luck!

---

#### Solution:

We are given windows executable file, which prints out `Order received.` three times when it is run. Simply capturing and inspecting its network traffic reveals the flag.

```bash
sudo tcpdump -A 'host challenges.thecatch.cz' | grep FLAG &
sudo wine easy_botnet_client.exe;
```

---

<details><summary>FLAG:</summary>

```
FLAG{MXcz-PrQK-FJbJ-jWVA}
```

</details>
<br/>
