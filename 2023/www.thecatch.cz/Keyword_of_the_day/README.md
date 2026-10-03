#### Challenge:

Ahoy, officer,

one of deck cadets (remember your early days onboard) had a simple task to prepare simple web application to announce keyword of the day. He claimed that the task is completed, but he forgot on which port the application is running. Unfortunately, he also prepared a lot of fake applications, he claims it was necessary for security reasons. Find the keyword of the day, so daily routines on ship can continue. 

May you have fair winds and following seas!

The webs are running somewhere on server `keyword-of-the-day.cns-jv.tcc`.

---

#### Solution:

The cadet published the real "keyword of the day" app on one TCP port of
`keyword-of-the-day.cns-jv.tcc`, but surrounded it with a large number of decoy
apps on other ports in the `60000-60500` range. All of the fakes serve
identical pages, so the real one is the single port whose response is unique.
I don't need to read every page by hand; I just need to find the odd one out.

My approach is to fingerprint every port: fetch `/` from each one, take the MD5
of the response body, and group the ports by hash. The decoys collapse into a
handful of large buckets (identical pages share a hash), while the genuine app
is the only bucket of size one. That single port serves the page with the
keyword/flag.

First I discover the open ports (e.g. with `nmap -p60000-60500
keyword-of-the-day.cns-jv.tcc`), then I hash and group them:

```python
#!/usr/bin/env python3
import hashlib

import requests

# Ports found open on keyword-of-the-day.cns-jv.tcc (e.g. via nmap -p60000-60500).
ports = [
    60000, 60004, 60009, 60010, 60011, 60015, 60018, 60019, 60020, 60021,
    60023, 60029, 60030, 60031, 60032, 60033, 60035, 60036, 60037, 60038,
    60041, 60042, 60045, 60047, 60051, 60052, 60058, 60059, 60060, 60063,
    60064, 60066, 60068, 60069, 60071, 60074, 60075, 60076, 60079, 60080,
    60081, 60082, 60084, 60087, 60089, 60096, 60099, 60100, 60104, 60105,
    60107, 60108, 60109, 60111, 60112, 60115, 60118, 60120, 60122, 60125,
    60126, 60129, 60130, 60134, 60135, 60136, 60138, 60140, 60143, 60144,
    60145, 60157, 60159, 60160, 60161, 60163, 60165, 60166, 60169, 60174,
    60175, 60177, 60178, 60179, 60180, 60181, 60185, 60187, 60189, 60190,
    60192, 60193, 60195, 60197, 60201, 60204, 60209, 60210, 60212, 60213,
    60214, 60215, 60217, 60218, 60221, 60222, 60225, 60228, 60229, 60230,
    60234, 60239, 60240, 60242, 60244, 60245, 60247, 60249, 60253, 60254,
    60255, 60256, 60257, 60258, 60259, 60260, 60261, 60262, 60266, 60267,
    60269, 60270, 60273, 60276, 60277, 60278, 60280, 60281, 60283, 60286,
    60288, 60290, 60294, 60297, 60299, 60303, 60304, 60307, 60309, 60310,
    60311, 60313, 60318, 60320, 60322, 60323, 60327, 60331, 60332, 60333,
    60341, 60343, 60344, 60345, 60347, 60348, 60350, 60352, 60354, 60356,
    60357, 60358, 60360, 60361, 60362, 60363, 60367, 60371, 60372, 60373,
    60378, 60382, 60383, 60384, 60385, 60386, 60387, 60389, 60398, 60400,
    60402, 60403, 60405, 60408, 60411, 60413, 60415, 60416, 60418, 60419,
    60421, 60422, 60424, 60426, 60427, 60430, 60432, 60433, 60437, 60438,
    60440, 60445, 60447, 60450, 60451, 60452, 60453, 60454, 60456, 60457,
    60459, 60460, 60461, 60466, 60468, 60471, 60473, 60474, 60482, 60487,
    60488, 60489, 60494, 60495,
]

ses = requests.session()
buckets = {}
for port in ports:
    r = ses.get(f"http://keyword-of-the-day.cns-jv.tcc:{port}/")
    digest = hashlib.md5(r.text.encode("utf-8")).hexdigest()
    buckets.setdefault(digest, []).append(port)

for digest, ps in buckets.items():
    print(f"{digest} {len(ps):>3} {ps[0]}")  # the bucket of size 1 is the flag port
```

The grouping output makes the outlier obvious. Almost every hash maps to dozens
of decoy ports; exactly one hash occurs a single time:

```text
3f68cd660a657dee8b7ac398c707d911  19 60000
d53c0a34a908e46f682eaaed75985d4e  39 60038
e2c9df2892759a836f245998cfccf666  42 60122
072969c04339237f8c1d8aae4ddbce0b  39 60214
ba78fb78b670b1b1a4c15e525bc3000b   1 60257   <-- unique: the real app
0d9e6ceee6185a0c5750a264040ff611  42 60288
666089c528a8dbfaa2d6d7e377638427  40 60383
08c77967ca1c2bd6a7b75a1ed835f708  12 60461
```

Port `60257` is the lone singleton, so that is the genuine application. Opening
`http://keyword-of-the-day.cns-jv.tcc:60257/` shows the keyword-of-the-day page,
which carries the flag `FLAG{....-....-....-....}`.

> Note: the challenge host `keyword-of-the-day.cns-jv.tcc` is long offline, so
> I could not re-run the scan live. The method above is verified by logic and
> matches the grouping output captured during the event, where port `60257` was
> the single distinct response.

---

<details><summary>FLAG:</summary>

```
FLAG{DEIE-fiOr-pGV5-8MPc}
```

</details>
<br/>
