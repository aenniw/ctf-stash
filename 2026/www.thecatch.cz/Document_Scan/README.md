#### Challenge:

Hi Senior Researcher,

an awkward incident occurred at the NREN headquarters: an important  document was scanned and immediately shredded for security reasons. However, the digital copy has since disappeared, and no trace can be found on the file servers.

Fortunately, a network capture of the scanner’s communication was recorded at the time of the incident. Your task is to reconstruct the missing document from the PCAP.

Stay curious!

Download the [evidence](https://owncloud.cesnet.cz/index.php/s/KhE0CZd8G49VIa3/download).
(SHA256 fingerpring `09982464cc16f288be66d33874de8bb1db6a414503e99666d15087dc5e1f3269`)

---

#### Solution:

The "evidence" download is a ZIP (not a bare PCAP). It holds the real capture
`document_scan.pcapng`, plus a `reference_scan.pcapng` / `reference_scan.png` pair that
serves as ground truth to validate the reconstruction method.

```bash
curl -sL https://owncloud.cesnet.cz/index.php/s/KhE0CZd8G49VIa3/download -o scan.zip
sha256sum scan.zip   # 09982464cc16f288be66d33874de8bb1db6a414503e99666d15087dc5e1f3269
unzip scan.zip -d extracted
```

The protocol hierarchy shows the HTTP/TLS traffic is just ESET/Windows-update noise; the
scanned document is a single ~36 MB TCP conversation on port **8610** — Canon's **MFNP**
(Multi-Function Network Protocol). Dump that stream's server→client payload:

```bash
tshark -r extracted/document_scan.pcapng -q -z conv,tcp          # -> big stream on :8610
tshark -r extracted/document_scan.pcapng \
  -Y "tcp.stream==13 && tcp.srcport==8610 && tcp.len>0" \
  -T fields -e tcp.payload | tr -d '\n' | xxd -r -p > doc_s2c.bin
```

Each MFNP packet is a 16-byte frame header `"MFNP"(4) + type(2) + seq(4) + 0x0001(2) +
length(4)`. The raster lives in the `0x8220` packets, each of whose payload starts with an
8-byte sub-header (`0606` + 4-byte length). Concatenating the `0x8220` payloads minus those
8 bytes yields exactly `4960*7015 = 34,794,400` bytes — an 8-bit grayscale 600-DPI A4 page
(`0xff` = white):

```python
import struct
data = open("doc_s2c.bin","rb").read()
raster, off = bytearray(), 0
while off + 16 <= len(data):
    assert data[off:off+4] == b"MFNP"
    ptype = struct.unpack(">H", data[off+4:off+6])[0]
    plen  = struct.unpack(">I", data[off+12:off+16])[0]
    payload = data[off+16:off+16+plen]
    if ptype == 0x8220:
        raster += payload[8:]        # strip the 0606 sub-header
    off += 16 + plen
open("doc.gray","wb").write(raster)  # len == 4960*7015
```

```bash
magick -size 4960x7015 -depth 8 gray:doc.gray document_reconstructed.png
```

The page is an invitation ("You're Invited to the NREN-TCC Annual Ball") with a QR code in
the bottom-left corner. Crop and decode it:

```bash
magick document_reconstructed.png -crop 1100x1100+750+5050 -threshold 50% qr_bw.png
zbarimg --raw qr_bw.png          # -> FLAG{GOTO-NREN-BALL-BABY}
```

Reconstructing `reference_scan.pcapng` the same way and diffing against the provided
`reference_scan.png` matches to within rounding (≈1917 of 34.7 M pixels), confirming the
method.

---

<details><summary>FLAG:</summary>

```
FLAG{GOTO-NREN-BALL-BABY}
```

</details>
<br/>
