#### Challenge:

I was looking at my network traffic, and found some interesting packets that seem to malformed. Can you figure out what's going on?

[capture.pcapng](./capture.pcapng ":ignore"), [server.go](./server.go ":ignore")

---

#### Solution:

Once again we are provided with a `PCAP` file. Going through it, I found a `DNS` query, requesting a `TXT` record with name `publickey` from a host with IP `3.93.213.98`.
The response to this request was an actual RSA public key:

```text
-----BEGIN RSA PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsSgZJjG5danof9SH+/iD
eboGxnIE49CxFLZTA3KXeKw4EhhtvKF7gxVoy9L6GCVqYCrA10U21aqgU65kvJqQ
RHzre1znuCSdecZHbcKTpHjIwSJ6yYnv9A5Pm6mB7ShnWsL6EEM5KTR4MmTaP7Ly
xw/oJ0NRXzbZubOGDtU33FX9C0l31Xrb6u3ptZxOI8Lx3/du0Zgxm8YoKmOLm5lI
wvchvzp5Ck1fevF6qxLbetwBb306aeCo3tEGbzaGEz29A/NqYtwA1EoajKkd8N7W
85QnJpLksv6dRLAh7byB3DilruxQRBJj1k46/SnRgikRwZ7RM8dAyKe81iQmHcm/
8QIDAQAB
-----END RSA PUBLIC KEY-----
```

After that, there was another request that `WireShark` was not able to parse otherwise as UDP data, and the response to it (also UDP data), looked like the output of the `ls -al` command (listing a file named `flag.txt`) with some other data (`.........7...`) probably headers of the unidentified protocol:

```text
total 3028
drwxr-xr-x    1 root     root          4096 Mar 11 03:07 .
drwxr-xr-x    1 root     root          4096 Mar 11 03:07 ..
-rw-rw-r--    1 root     root           102 Mar 11 03:01 Dockerfile
-rw-rw-r--    1 root     root           718 Mar 11 03:01.........7... README.md
-rw-rw-r--    1 root     root         24846 Mar 11 03:01 capture.pcap
-rw-rw-r--    1 root     root          1132 Mar 11 03:01 challenge.yml
-rw-rw-r--    1 root     root          3670 Mar 11 03:01 client.go
-rwxrwxr-x    1 root     root      .........7...     155 Mar 11 03:01 docker-compose.yml
-rw-rw-r--    1 root     root            33 Mar 11 03:01 flag.txt
-rwxr-xr-x    1 root     root       3030096 Mar 11 03:07 server
-rw-rw-r--    1 root     root          4167 Mar 11 03:01 server.go
```

Looking at the enclosed `server.go` file (published later in the competition), we see that the second malformed request/response pair is actually supposed to be modified DNS.

From that, it is also clear, that we need to request current public key (like in the first request in `PCAP`) and use it to encrypt the second request that will contain command to return the flag.
The encrypted second request will surely be bigger that `254 characters` allowed by `DNS standard` therefore we have to tamper with the query to work like the one in the provided `PCAP` - allow for multipart requests - requests containing payloads longer than 254 characters by splitting them between DNS questions within the single request.

After trying some Python DNS libraries, I found out that none of them allow me to manipulate the request structure so I decided to tamper with the second request manually.

The original DNS request from the `PCAP` explained part-by-part:
(also check this out for general DNS request form explanation https://www.firewall.cx/networking-topics/protocols/domain-name-system-dns/160-protocols-dns-query.html)

```text
######## DNS HEADER


#### DNS TRANSACTION ID - (2 bytes):
000c
#### DNS Flags - "0100" = Standard query - (2 bytes):
0100
#### DNS Questions - Indicates number of DNS queries (2) with max size 254 chars in this request - (2 bytes):
0002
#### DNS Answer RRs - (2 bytes):
0000
#### DNS Authority RRs - (2 bytes):
0000
#### DNS Additional RRs - (2 bytes):
0000


######## After the HEADER follow the 2 actual DNS Questions/Queries:


#### DNS Query 1 size (1 byte) DNS Query Size - max 254 chars (= "fe" because this is the first query and we are supposed to be 2 based on the number of DNS Questions):
fe
#### DNS Query 1 content (254 chars = 508 bytes):
51e95adb69107f965c449475fa96d9a29274b774c71adb018db94c0f4b6fc02e20845166ee7243039f239779bc402c5dfa119030395a2b85e4568b274a86a79a5d69439a54fb624dcdf792bafdd313b308ff405ec0ee12e7022f4ffb56ea36db4e51a9aeae4597c564c6b26c70fb148af549a5fb86e20480ba61c27e392cf722829551a57fba0af3ee0ee374c82609a16d11ee40877002ff30ec8f3e8d31b5bd0695f048156fda78167fca9c6f1739d6aaabe7a838e146ca7513f3e71e16f1518e09adb6af1bd699aed99b6c16c14a7e6eeda306eb9c459854c0b9105d7d19afa26abaf566bf469684bd01632839111432f352b7e44660176174f736bc5a
#### Null byte as the end of the DNS Query string (last char always, thats why the full query can have at most 254 chars)
00
#### DNS Query 1 Type Flag - (0010 = TXT) (2 bytes):
0010
#### DNS Query 1 Class Flag - (0001 = IN) (2 bytes):
0001


#### DNS Query 2 size (1 byte) DNS Query Size - 2 = 2 chars = 4 bytes
02
#### DNS Query 2 content (2 chars = 4 bytes):
5296
#### Null byte as the end of the DNS Query string (last char always)
00
#### DNS Query 2 Type Flag - (0010 = TXT) (2 bytes):
0010
#### DNS Query 2 Class Flag - (0001 = IN) (2 bytes):
0001
```

From the format above, I created function in `python` that can send arbitrarily long message by splitting it into several queries and settign up the related values in the DNS header accordingly:

```python
#!/usr/bin/env python

from pwn import *
from struct import *

import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA512

def my_dns_request_builder(raw_payload_content):

    # Split to subqueries by 254 chars = 508 bytes
    n=508
    payload_subqueries = [raw_payload_content[index : index + n] for index in range(0, len(raw_payload_content), n)]

    # Put subquery lengt in front of it and Null byte + Type + Class after it:
    payload_parts=""
    for payload_subcontent in payload_subqueries:
        payload_subcontent_length = format((len(payload_subcontent)//2), '02x')
        print(payload_subcontent_length)
        print(payload_subcontent)
        print("00" + "0010" + "0001")
        payload_parts = payload_parts + payload_subcontent_length + payload_subcontent + "00" + "0010" + "0001"

    # Setup the Request header and append the subqueries
    dns_payload = bytearray.fromhex("000c"+"0100"+format((len(payload_subqueries)), '04x')+"0000"+"0000"+"0000"+payload_parts)
    return dns_payload


#####################################
## First DNS request to get the RSA key

q = dns.message.make_query('publickey', dns.rdatatype.TXT)

print(q)

r = dns.query.udp(q, '3.93.213.98', port=9855)
rsa_public_key = (str(r.answer[0][0])+str(r.answer[0][1])).replace('"', '').replace('\\010', '\n')
print(rsa_public_key)

# Load the key
key = RSA.importKey(rsa_public_key)
cipher = PKCS1_OAEP.new(key, hashAlgo=SHA512)


#####################################
## Second DNS request containing encrypted "cat flag.txt" command

## Encrypt command
plaintext_payload_bytes = "cat flag.txt".encode('utf-8')
print(plaintext_payload_bytes)
encrypted_payload = cipher.encrypt(plaintext_payload_bytes)

## Send reqest
r = remote('3.93.213.98', 9855, typ="udp")
dns_payload = my_dns_request_builder(binascii.hexlify(encrypted_payload).decode("utf-8"))
print(binascii.hexlify(dns_payload))

r.send(dns_payload)
response = r.recv(6000)
print("")
print(response)


r.close()
```

---

<details><summary>FLAG:</summary>

```
utflag{i_love_me_some_spicy_dns}
```

</details>
<br/>
