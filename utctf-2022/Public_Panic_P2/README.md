#### Challenge:

With the information we got from the previous problem we can surely get on their system!

For this challenge you can run nmap, but only against misc2.utctf.live on port 8622. 

`misc2.utctf.live:8622`

---

#### Solution:

- using the password from prev. challenge and using the user naming first letter of first name + surname reveals the flag

```bash
sshpass -p defaultpw5678! ssh cshackleford@misc2.utctf.live -p 8622 cat flag.txt
```

---

<details><summary>FLAG:</summary>

```
utflag{conventions_knowledge_for_the_win}
```

</details>
<br/>
