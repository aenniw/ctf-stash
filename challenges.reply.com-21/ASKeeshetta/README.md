#### Challenge:

In the meantime, Ironcode and R-boy head towards the Temple of the Master Bank. Here, the great caves hold the most powerful reserves of zirconium in the region. Zer0 has managed to take over them and block access to them using traps with complex codes. The two heroes need your help to decrypt them and take them out of the hands of the arch enemy. [misc300-askeeshetta.apk](./misc300-askeeshetta.apk ":ignore")

---

#### Solution:

- reversing the the `apk` reveals 3 REST endpoints:
  - `https://gamebox1.reply.it/a3a1be5a7903afaf6a2573fb7aedd21a/answer` with parameters `question` and `answer`, this endpoint is however secured in some way
  - `https://gamebox1.reply.it/a3a1be5a7903afaf6a2573fb7aedd21a/open_ticket` with parameter `path`
  - `https://gamebox1.reply.it/a3a1be5a7903afaf6a2573fb7aedd21a/aboutus` -> `Web page under construction. Send us the full path using the dedicated area on the app so we can debug the specific file.`
- also `OkHttp` client is secured via certificate pinning, thus to find out what the `apk` consists of we need to get rid of it and replace it with `BurpSuite` proxy cert - see [Bypass OkHTTP CertificatePinner on Android](https://medium.com/@z2hteam/bypass-okhttp-certificatepinner-on-android-a085b8074e25)

```bash
# convert cert
openssl x509 -inform der -in CA.cer -out CA.pem
openssl x509 -in CA.pem  -pubkey -noout | openssl rsa -pubin -outform der | openssl dgst -sha1 -binary | openssl enc -base64
# decompile apk
java -jar ./apktool_2.6.0.jar d ./misc300-askeeshetta.apk
# find and update cert for our custom one
grep -r "sha256/dUgaSWFBY4l54eispHBdTYpGm/jqBTRZJKGNigLkHzY=" # misc300-askeeshetta/smali_classes4/reply/misschiscia/NetworkUtils.smali
# recompile apk
java -jar ./apktool_2.6.0.jar b misc300-askeeshetta/ -o SSL-Unpinned.apk
# resign apk
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore ./SSL-Unpinned.apk alias_name
```

- configure android to use `BurpSuite` proxy and playing with app reveals that `User-Agent: okhttp/4.9.1` is required for `anwser` endpoint

```python
import requests
import base64
import hashlib

questions = [
    'Is it a male?',
    'Is it a human?',
    'Is it a female?',
    'Does it love tiny onions?',
    'Is it he or it is not he?',
    'Does it have long hair?',
    'Did they lose Giacomino?',
    'Is it a worldwide actor loved by everyone?',
    'Is it rich?',
    'Is it real?',
    'Is it still alive?',
    'Is it an athlete?',
    'Did it change the world thanks to its mind?',
    'Does it run fast?',
    'Is it pink?',
    'Do you personally know it?',
    'Do you like it?',
    'Is it a politician?',
    'Does it come from your country?',
    'Is it coming home?',
    'Does it love sun and whisky?',
    'Does it have green hair?',
    'Does it love singing?'
]


hashes = []
ses = requests.session()

while len(hashes) != len(questions):
    for q in range(0, len(questions)):
        resp = ses.post('https://gamebox1.reply.it/a3a1be5a7903afaf6a2573fb7aedd21a/answer', data={
            'question': str(q), 'answer': ''}, headers={'User-Agent': 'okhttp/4.9.1'})

        type = resp.headers['Content-Type']

        if type == 'text/html; charset=utf-8':
            continue
        elif type == 'image/jpg':
            body = resp.content
            if 'ETag' not in resp.headers:
                body = base64.b64decode(body)
            md5 = hashlib.md5(body).hexdigest()
            name = "./dumps/{}.jpg".format(md5)

            if md5 in hashes:
                continue
            hashes.append(md5)

            with open(name, 'wb') as f:
                f.write(body)
        else:
            print(resp.headers, resp.text)

```

- dumping all the images revealed that one of them was not encoded `5eb92a061cd3c50928641e3b3d05380b.jpg` and also contains `URL` set in metadata.  Submitting this URL to the "debug" endpoint as hinted in the `aboutus` endpoint reveals the flag.

```bash
exiftool ./dumps/5eb92a061cd3c50928641e3b3d05380b.jpg # URL                             : /top_actors/leeno_bunphy.jpg
curl -X POST https://gamebox1.reply.it/a3a1be5a7903afaf6a2573fb7aedd21a/open_ticket -d 'path=/top_actors/leeno_bunphy.jpg'
```

---

<details><summary>FLAG:</summary>

```
{FLG:Christm4s_V4c4tion_83}
```

</details>
