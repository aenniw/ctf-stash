#### Challenge:

Ahoy, officer,

the chief security officer has told you, he came across a very suspicious event in ship's security logs on the occasion of a planned monthly log check. The event is related to accessing the secret file `secret.db` on server on cargo deck. Luckily, the ship is equipped with an automatic network traffic recorder, which was activated by the suspicious event and provided corresponding packet capture. Your task is to confirm that the mentioned file has been exfiltrated and to examine its contents. 

May you have fair winds and following seas!

Download the [suspicious_traffic.pcap](./suspicious_traffic.pcap ":ignore").\
(MD5 checksum: `6e7cfe473b222ff766e04196e35df304`)

---

#### Solution:

The `suspicious_traffic.pcap` download is actually a **zip** wrapping the real capture, so I unzip
it first. Looking at the conversations, I find two exfiltration channels: a cleartext **FTP**
session and an encrypted **SMB3** session. I need both.

```bash
unzip suspicious_traffic.pcap            # -> inner suspicious_traffic.pcap
```

##### 1. FTP &mdash; how the file was encrypted

The FTP control channel is in cleartext, so I can read the login and the two uploads done in active
(`PORT`) mode:

```
USER james
PASS james.f0r.FTP.3618995
TYPE I                 # binary
STOR home.tgz
STOR etc.tgz
```

I follow / export the two data streams (Wireshark: *Follow &rarr; TCP Stream*, save raw) and get
valid gzip tarballs. Inside `home.tgz` the `.bash_history` shows how `secret.db` was encrypted before
it was exfiltrated:

```bash
grep -a openssl home/.bash_history
# openssl enc -aes-256-cbc -salt -pbkdf2 -in secret.db -out secret.db.enc -k R3alyStr0ngP4ss!
```

So I have the key material: `aes-256-cbc` + `pbkdf2` + password `R3alyStr0ngP4ss!`. But
`secret.db.enc` itself is **not** in the FTP transfer &mdash; it went over the encrypted SMB3 session.

##### 2. SMB3 &mdash; recovering the session key

The SMB traffic (`172.20.0.7` &rarr; `172.20.0.6`, dialect **3.1.1**, cipher **AES-128-GCM**) is
encrypted (`SMB2_TRANSFORM` headers). To decrypt it I need the SMB **session key**, which is the
NTLMv2 `ExportedSessionKey`. I pull the NTLMv2 authentication out of the `SESSION_SETUP` and crack it.

The leaked credentials follow a pattern (`james.f0r.FTP.3618995`, `admin:james.f0r.HTTP.4648507`),
so I assume the SMB password is `james_admin.f0r.SMB.<7 digits>` and run a mask attack
(**rainbow tables / online lookups do not work on NetNTLMv2** &mdash; it is salted with the server +
client challenge, so a dictionary/mask attack is the only option):

```bash
# NetNTLMv2 hash extracted from the capture (user james_admin, domain LOCAL.TCC):
#   james_admin::LOCAL.TCC:<server_chal>:<ntproofstr>:<blob>
hashcat -m 5600 james_admin.netntlmv2 -a 3 'james_admin.f0r.SMB.?d?d?d?d?d?d?d'
# -> james_admin.f0r.SMB.8089078
```

With the password I derive the keys (`NTOWFv2 -> NTProofStr -> SessionBaseKey -> RC4-decrypt the
EncryptedSessionKey`) to obtain `RandomSessionKey = 7a93dee25de4c2141657e7037dddb8f1`
(session id `49b136b9...`). I confirm the whole chain in Python &mdash; the computed `NTProofStr`
matches the one in the capture:

```python
import hmac, hashlib
from Crypto.Hash import MD4                    # NTLM hash = MD4(UTF-16LE(password))
pw   = "james_admin.f0r.SMB.8089078"
user, dom = "JAMES_ADMIN", "LOCAL.TCC"
nthash  = MD4.new(pw.encode("utf-16-le")).digest()
respkey = hmac.new(nthash, (user + dom).encode("utf-16-le"), hashlib.md5).digest()
# ntproofstr / server_challenge / blob / encrypted_session_key taken from NTLMSSP_AUTH + CHALLENGE
assert hmac.new(respkey, server_challenge + blob, hashlib.md5).digest() == ntproofstr
sbk = hmac.new(respkey, ntproofstr, hashlib.md5).digest()       # SessionBaseKey
rsk = rc4(sbk, encrypted_session_key)                           # RandomSessionKey (the SMB key)
```

##### 3. Decrypt SMB3, carve the file, decrypt the DB

I give the key to Wireshark &mdash; *Edit &rarr; Preferences &rarr; Protocols &rarr; SMB2 &rarr;
Secret session keys*, adding `49b136b9...,7a93dee25de4c2141657e7037dddb8f1`. The SMB3 traffic now decrypts; I can
see `secret.db.enc` being `WRITE`n to the share, and I export it with
*File &rarr; Export Objects &rarr; SMB*. Finally I decrypt it with the password from the history and
read the database:

```bash
openssl enc -aes-256-cbc -d -pbkdf2 -in secret.db.enc -out secret.db -k 'R3alyStr0ngP4ss!'
sqlite3 secret.db 'select * from secrets;'
```

The `secrets` table contains the flag, confirming the file was exfiltrated and recovering its
contents.

> SMB3 decryption background: [Decrypting SMB3 Traffic with just a
> pcap](https://medium.com/maverislabs/decrypting-smb3-traffic-with-just-a-pcap-absolutely-maybe-712ed23ff6a2).

---

<details><summary>FLAG:</summary>

```
FLAG{5B9B-lwPy-OfRS-4uEN}
```

</details>
<br/>
