#### Challenge:

Do we still have some privacy?
or it is easy to get back everything?

https://drive.google.com/file/d/13W2EP5G1ceFTMRLdaBU_6IiwhAgZlwLq/view?usp=sharing
Password : `FOFtWHSOaCqarQwTKzOl`

---

#### Solution:

```bash
file ./chall.E01
ewfmount ./chall.E01 ./ewf
mount ./ewf/ewf1 ./drive -o ro,show_sys_files,streams_interace=windows
sqlitebrowser drive/Users/Semah/AppData/Roaming/WhatsApp/Databases/msgstore.db
```

- after inspecting the `msgstore.db` for message history we found `https://drive.google.com/file/d/1L1xN6R-Za4W1ME2UZE8LXH45gfHSw66D/view?usp=sharing"`

```
Hello Semah,

We are from the dev team, we would like to inform you that we have switched our platform, and that we have changed only your username to : Securinets_Quals2k21. and that your password is still the same. 
New platform : https://for1.q21.ctfsecurinets.com/.

Sorry for any inconvenience, we would love to give you in return something special : 
first part : Securinets{whatsapp_and_
```

- inspecting the `Firefox` metadata we found that `logins.json` contains username and password needed, we just need to decrypt it

```bash
mkdir Firefox
cp drive/Users/Semah/AppData/Roaming/Mozilla/Firefox/Profiles/pyb51x2n.default-release/{cert9.db,cookies.sqlite,key4.db,logins.json} ./Firefox/

git clone https://github.com/unode/firefox_decrypt.git
python2 ./firefox_decrypt/firefox_decrypt.py ./Firefox/
```

```
Website:   https://for1.q21.ctfsecurinets.com
Username: 'Securinets_Quals2k21'
Password: 'GacsriicUZMY4xiAF4yl'
```

---

<details><summary>FLAG:</summary>

```
Securinets{whatsapp_and_saved_passwords_isn't_helpful_after_all_x)}
```

</details>
<br/>
