#### Challenge:

I love Celeste Speedrunning so much!!! It's so funny to watch!!!

[Here's my favorite site!](https://mount-tunnel.web.actf.co/)


---

#### Solution:

We are presented with a website that has a scoreboard of the fastest players ("Old Lady" has a time `0`) and we are told to beat them.

Inspecting the source of the page it can be seen that there is hidden input for the start time which is pre-set to the timestamp of the page load. Setting it to some time in the future we get a negative time and beat the record.

```bash
# Just use any time in the future so its less than `0` which player "Old Lady" has
curl 'https://mount-tunnel.web.actf.co/submit' --data-raw 'start=2682231179.5145428'
```

---

<details><summary>FLAG:</summary>

```
actf{wait_until_farewell_speedrun}
```

</details>
<br/>
