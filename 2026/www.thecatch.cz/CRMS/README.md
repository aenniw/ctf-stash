#### Challenge:

Hi Associate Researcher,

cats are valued members of the NREN-TCC community. Their curiosity, intelligence, and dedication help advance science, research, and education. Always eager to assist, these furry colleagues work tirelessly to support everyone—one paw, one discovery, and one helpful message at a time. 

"Need help? Just ask the NREN cat team. For example, they have recently created a new service called CRMS", says the Head of the Department of Feline Research.

Stay curious!

Access the service at http://crms.nren.tcc/

---

#### Solution:

- the page has a single button *"I like you too. Send me the e-mail."* that POSTs to `/send`. CRMS is a **reverse** mail service: it does not accept a connection, it dials **back to your own VPN IP** and delivers the mail over SMTP.
- triggering delivery once and letting it fail reveals exactly where it connects to — `TCP/2525` on the client's IPv6 address:

```
IP address: 2001:db8:ffff::2c
Port:       TCP/2525
Error:      timed out
```

- so the whole task is to **listen on TCP 2525 and catch the e-mail**. No real mail stack is needed — a raw socket that speaks just enough SMTP (`220` → `EHLO` → `MAIL`/`RCPT` → `DATA` → `250`) and prints the body does the job. See [sink.py](./sink.py ":ignore"):

```python
import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("::", 2525))
s.listen(1)
conn, _ = s.accept()
f = conn.makefile("rwb", buffering=0)
f.write(b"220 sink\r\n")
for raw in f:
    line = raw.decode(errors="replace").strip()
    print(line)
    u = line.upper()
    if   u.startswith(("EHLO", "HELO")): f.write(b"250 OK\r\n")
    elif u.startswith("MAIL"):           f.write(b"250 OK\r\n")
    elif u.startswith("RCPT"):           f.write(b"250 OK\r\n")
    elif u.startswith("DATA"):           f.write(b"354 go\r\n")
    elif u == ".":                       f.write(b"250 queued\r\n")
    elif u.startswith("QUIT"):           f.write(b"221 bye\r\n"); break
    else:                                f.write(b"250 OK\r\n")
```

- the one gotcha is the **local firewall**: the connect-back keeps timing out because `ufw` (default INPUT policy `DROP`) silently drops the inbound SYN. Open the port first:

```bash
# open the port for the connect-back, then start the sink
sudo ufw allow 2525/tcp
python3 sink.py &

# trigger delivery — the server now connects back to TCP/2525
curl -X POST http://crms.nren.tcc/send
```

- the flag arrives in the SMTP `DATA` body:

```
From: Tiger the Cat <tigercat@dfr.nren.tcc>
Subject: Message from Tiger (not a tiger)

I'm sending you a secret code, to make you happy.

FLAG{...}

Do not share it with dogs!
```

---

<details><summary>FLAG:</summary>

```
FLAG{eEA9-WUne-CloQ-Ofaz}
```

</details>
<br/>
