#### Challenge:

Hi Senior Researcher,

we've received a report about an unregistered web service operating somewhere in the `10.100.26.0/24` network. There is one problem: the subnet has become unusually noisy. Every address and every port seems eager to talk, driving our AI-driven automated scanner completely mad.

Your task is to find the web service.

Stay curious!

---

#### Solution:

The whole `10.100.26.0/24` is a **SYN-ACK-spoofing tarpit** (think `portspoof`): roughly every
address answers a SYN on **every** port, so a port scan reports all 65535 ports "open" on all 254
hosts — but the spoofed services never send a single byte of data. That is what drives the automated
scanner "mad". The real web service is one genuine daemon hiding in the noise; the trick is to stop
trusting "open port" and look at **TCP behaviour** instead.

**1. Confirm it's a tarpit.** Pick any host — every port looks open, yet nothing ever talks back:

```bash
nmap -Pn -n --top-ports 20 10.100.26.26          # all 20 "open"
printf 'GET / HTTP/1.0\r\n\r\n' | nc 10.100.26.26 80   # ...silence, no banner
```

**2. Find the real hosts by how they treat a *closed* port.** A spoofing host forges a SYN-ACK for
everything; a genuine host's kernel **refuses** a closed port instantly (RST). So time the connect
across the whole range — the real machines are the ones that connect/refuse in near-zero time:

```bash
seq 1 254 | xargs -P80 -I{} sh -c \
 'printf "%s 10.100.26.{}\n" "$(curl -s -m6 -o /dev/null -w %{time_connect} http://10.100.26.{}:80/)"' \
 | sort -n | head        # => 10.100.26.1, .10, .66 respond instantly; the rest hang/spoof
```

**3. Scan only the real hosts and grab the flag.** Of the three, only `.66` exposes a web port — a
little Python `SimpleHTTP` page ("In memoriam — Pavel Vachek") on `2025`:

```bash
nmap -Pn -n -p- --open 10.100.26.66              # 22/ssh, 2025, 5666
curl -s http://10.100.26.66:2025/ | grep -oE 'FLAG\{[^}]*\}'
```

**Fix / takeaway:** port-spoofing tarpits defeat naive "is the port open?" scanning. Fingerprint
real services by protocol behaviour and connection timing (fast RST on closed ports, actual data on
open ones), not by the SYN-ACK alone.

---

<details><summary>FLAG:</summary>

```
FLAG{O2pS-yj4k-Qd8U-v9ft}
```

</details>
<br/>
