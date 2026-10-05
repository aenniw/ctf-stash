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
