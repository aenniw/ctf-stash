#### Challenge:

Do you like baking? Don't leave the oven on for too long! <br><br> <b>Open the <code>Deployment</code> tab to start this challenge.</b>

---

#### Solution:

We are presented with website where we can choose recipes to bake. Each recipe has a time determining how long it will take for it to be baked in the oven. The longest one are `Magic Cookies` (HINT) and they will take 7200 minutes to bake, but ain't nobody got time for that. After putting them in the oven cookie with name `in_oven` and value `{"recipe": "Magic Cookies", "time": "dd/mm/yyy, HH:MM:SS"}` is created. We just edit the time to be in the past and voila.

```bash
echo "{\"recipe\": \"Magic Cookies\", \"time\": \"$(date "+%D, %T" -d @$(( $(date "+%s") - 432300)) )\"}" | base64
```

---

<details><summary>FLAG:</summary>

```
flag{you_are_the_master_baker}
```

</details>
<br/>
