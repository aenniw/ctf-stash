#### Challenge:

Hi Senior Researcher,

an unknown perpetrator is attempting to discredit the national research and education network (NREN) and, on their domain theylietoyou.tcc, is publishing entirely unverified hoaxes, fake news, and other thoroughly unscientific content aimed against the mission of the NREN.

Law enforcement authorities have already been informed and they could use your assistance to gather as much information as possible. More information can be found on the website http://theylietoyou.tcc/story-line.

Stay curious!

---

#### Solution:

The target `http://theylietoyou.tcc` is a **Vite/React single-page app** — every path returns the
same shell with an empty `<div id="root">`, so all content is rendered client-side from the bundle
`/assets/index-ubZeohZh.js`. The challenge name says it all: **explore**, don't exploit.

**1. Read the "Case File" (`/story-line`).** The page is a React route rendered from the bundle. It
is the police case file and it (a) hands over an infiltration account and (b) states the site was
built by an amateur dev who "left oversights and vulnerabilities":

```bash
curl -s http://theylietoyou.tcc/assets/index-ubZeohZh.js \
  | grep -oE 'Username: [^"]+|Password: [^"]+'
# Username: newWarrior
# Password: chAng3melaTer123
```

**2. Find the API host.** The front-end talks to a **separate backend**, whose base URL is baked
into the bundle:

```bash
curl -s http://theylietoyou.tcc/assets/index-ubZeohZh.js \
  | grep -oE 'https?://[a-zA-Z0-9.-]+' | sort -u | grep theylietoyou
# http://api.theylietoyou.tcc
```

Logging in works and returns a JWT — but it carries `role: AUTHOR`, and the whole admin area
(`/api/admin/*`, including `/api/admin/flag`) is correctly locked to `ADMIN` (HTTP 403):

```bash
curl -s -X POST http://api.theylietoyou.tcc/api/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"newWarrior","password":"chAng3melaTer123"}'
```

**3. The amateur oversight — exposed Spring Boot docs.** The backend is Spring Boot and left its
management/doc endpoints wide open: `/actuator`, `/swagger-ui/index.html`, and the raw OpenAPI spec
`/v3/api-docs`. The spec alone leaks the whole attack surface (undocumented admin endpoints
`/api/admin/conf`, `/api/admin/impersonate/{userId}`, `/api/admin/users/{userId}/meta/{metaId}`)
**and the flag**.

**4. Flag is hidden in the OpenAPI doc.** It sits in the `description` of the `TokenResponse`
schema:

```bash
curl -s http://api.theylietoyou.tcc/v3/api-docs | grep -oE 'FLAG\{[^}]*\}'
# FLAG{McUs-Wrjs-8MbE-SiIt}
```

The surrounding text reads: *"This JWT is also very important for our DEV environment
(**untraceable-dev.theylietoyou.tcc**)! FLAG{McUs-Wrjs-8MbE-SiIt}"* — i.e. the same description is
the next clue in the trail: a **dev subdomain** `untraceable-dev.theylietoyou.tcc` where the issued
JWT matters, which leads into **Chapter 2: The Owner**.

**Fix:** never expose `/v3/api-docs`, Swagger UI, or `/actuator` in production, and never embed
secrets/flags/next-stage hints in schema descriptions.

---

<details><summary>FLAG:</summary>

```
FLAG{McUs-Wrjs-8MbE-SiIt}
```

</details>
<br/>
