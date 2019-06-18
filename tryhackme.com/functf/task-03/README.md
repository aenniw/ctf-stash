## F*(u+BPD!g

You know the drill, focus on the Title. [hide.jpg](./hide.jpg ':ignore')

[CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base85('!-u')&input=RioodStCUEQhZw)

```bash
steghide extract -sf hide.jpg -p $(file hide.jpg |  cut -d'"' -f 2 | base32 -d)
cat ./flag-1.txtg
```

<details><summary>FLAG:</summary>

```
tryhackme{st3gh1d3_i5_l0v3}
```

</details>
