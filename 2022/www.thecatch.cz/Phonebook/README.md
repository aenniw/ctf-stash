#### Challenge:

Hi, packet inspector,

you should already get access to the phone book &ndash; as a new employee &ndash; but the AI is too busy right now. This condition can last several ... who knows ... years?

Your task is to gain access to the application running on [http://phonebook.mysterious-delivery.tcc:40000](http://phonebook.mysterious-delivery.tcc:40000).

May the Packet be with you!

---

#### Solution:

We are given a site called `Phonebook`. It has a search functionality and a login form requiring username and password.
Putting the `*` into the search returns `65 records` with fields `UID`, `Description`, `Phone`, `DN` and `Groups`. The field names and their content indicate that the data are pulled from `LDAP`.

This is confirmed by a hint comment left in the page source code:

```html
<!-- New LDAP server host: 10.99.0.121 -->
<!-- 1/2/2022 Temporary search filter (|(&(memberof=cn=users,ou=groups,dc=local,dc=tcc)(uid=_DATA_))(memberof=cn=nonmigrated,ou=groups,dc=local,dc=tcc)) -->
<!-- 6/8/2022 Filter after migration  (|(&(memberof=cn=users,ou=groups,dc=local,dc=tcc)(uid=_DATA_}))) -->
```

Searching for `LDAP` and `filter injection`, I found this [writeup](https://medium.com/@Victor.Z.Zhu/csaw-ctf-quals-18-ldab-web-50-write-up-ldap-injection-victor-zhu-7adbe4984137). Using the injection payload from it - `*)(uid=*))(|(uid=*` we get 4 additional accounts, we didn't see before:

```text
phone_reader | Limited account for phonebook webapp    |            | uid=phonebook_reader,ou=people,dc=local,dc=tcc |
admin1	     | Admin account                           | 7254437132 | uid=admin1,ou=people,dc=local,dc=tcc           | cn=admins,ou=groups,dc=local,dc=tcc
admin2       | Admin account                           | 5452487532 | uid=admin2,ou=people,dc=local,dc=tcc           | cn=admins,ou=groups,dc=local,dc=tcc,cn=web_admins,ou=groups,dc=local,dc=tcc
ldap_sync    | Don't change password. gasg35faCasgt%AF |            |                                                |
```

It seems that there are 2 admin accounts: `admin1` and `admin2`. `admin2` seems to have more permissions, since it belongs to both groups - `admins` and `web_admins`.

Then there are 2 service accounts: `phone_reader` and `ldap_sync`. Phone_reader is limited according to description, but `ldap_sync` is interesting because it has what seems to be a password saved in the description - `gasg35faCasgt%AF`. Unfortunately trying its username/password combination in the login form is futile. But using them in the `LDAP server`, mentioned in the comment hint, gives us (read-only) access to the LDAP data.

Here is the command I used to dump all the data from the LDAP:

```bash
ldapsearch -x -H 'ldap://10.99.0.121' -D 'uid=ldap_sync,ou=people,dc=local,dc=tcc' -w 'gasg35faCasgt%AF' -b "dc=local,dc=tcc"
```

This provided mostly the same info we have already seen in the web search, except that each user has 2 additional fields that are of interest to us - `sambaLMPassword` and `sambaNTPassword`. These contain `LM` resp. `NT` password hashes. I have tried to put all of them into [crackstation](https://crackstation.net/), but I only got one hit, and even that one was actually `partial hit`. Good news was, that the hit was for the `LM` hash of `admin2`'s password (`48448F207404DB05F3BAC3A9216F6D52`), which has the `web_admin` permissions. Anyway, I found out, that `partial hit` means, that only the (first) half of the LM hash matched against the crackstation's database (because of how LM hashes work). Trying out the [http://rainbowtables.it64.com/](http://rainbowtables.it64.com/), which is site specifically dedicated to `LM hash craking`, I got both halves of the password for the `LM hash`:

```text
Hash             |  Pass
48448f207404db05 | TOOSTRO
f3bac3a9216f6d52 | NGPASS.
```

Unfortunately trying to login with this password (`TOOSTRONGPASS.`) still didn't work. But because `LM` algorithm in the process of hash creation changes all characters to uppercase, I created a little [script](./cases.py  ":ignore") that generated all `8192` possible uppercase/lowercase permutations and saved them to a wordlist file - `wlist.txt`. Then I tried to login with all the case permutations using another [python script](./bruteforcer.py  ":ignore") instead of `hydra`, because the login form was secured with `CSRF` token. To my great disappointment this was also futile.

After trying and googling lots of different stuff - all in vain - I came across this [page](https://www.thebitmill.com/articles/nt_password.html). It helped me to realize, why I wasn't aby to crack the `sambaNTPassword` hash - `32644235283BC5561CC7FE4FFFADDAEE` for the `admin2` with my `wlist.txt`, even though I was 100% sure, that I have generated all the case permutations.

The reason was again the way how LM hashing algorithm works. LM hash requires the passwords to be `14` characters long (and btw also in special charset). If the password is shorter, then the algorithm fills the rest with `NUL` characters. If the password is longer, it is usually truncated to `14` characters by most implementations (like in [this function](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html)).

So my new theory was that the `NT` hash password was actually longer than the one we recovered from the `LM` hash, while it contained one of its case permutations as prefix. Using `wlist.txt` containing LM password case permutations as base and incrementally brute-forcing following characters, I set out to test my theory with `hashcat`:

```bash
hashcat -a 6 -m 1000 NTHash.txt wlist.txt -1 "?l?u?d?s" "?1?1?1?1?1" --increment
```

That gave me the `NT hash` password - `TooStrongPass.2022` and with that I was finally able to login as `admin2` into the web and find the flag!

---

<details><summary>FLAG:</summary>

```
FLAG{iLcT-HnNF-egs3-mCSN}
```

</details>
<br/>
