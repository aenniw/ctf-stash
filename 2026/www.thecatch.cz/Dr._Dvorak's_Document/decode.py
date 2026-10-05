#!/usr/bin/env python3
# Typed with Dvorak muscle memory on a QWERTY machine: map QWERTY key -> Dvorak char at same position.
import sys
qwerty = "-=qwertyuiop[]asdfghjkl;'zxcvbnm,./" + '_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'
dvorak = "[]',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz" + '{}"<>PYFGCRL?+AOEUIDHTNS_:QJKXBMWVZ'
t = str.maketrans(qwerty, dvorak)
data = open(sys.argv[1], encoding="utf-8", errors="replace").read() if len(sys.argv) > 1 else sys.stdin.read()
sys.stdout.write(data.translate(t))
