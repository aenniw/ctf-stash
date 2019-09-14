#### Challenge:

Korunní princ potřebuje Vaši pomoc, asi nějaké diamanty nebo tak něco! Pospěšte na královský chat:

http://forensic-night.cesnet.cz/princeofpersia

Mimochodem, princ má v oblibě server http://keyserver.insect.com/

---

#### Solution:

```bash
gpg --gen-key
gpg --armor --output pubkey.gpg --export ctf@gmail.com # upload key to http://keyserver.insect.com/
gpg --keyserver keyserver.insect.com --search-key ctf@cesnet.cz
echo 'DCFBFF67CD11405890DBECBA6D0ED7075C7A8D61' | gpg --encrypt --armor --recipient ctf@cesnet.cz
echo '-----BEGIN PGP MESSAGE-----

hIwDlE6IKcAz0t0BA/sGx0RdMlmLekeyAJr1gygIh79NgX7GYU+EVunbUY0WhaGa
Y7xlRTQo5mLJS3RTfeFvLDFNCXzBnee8z5SVWLXvyZzyzCcu9wu48miWpw7b8Axy
lkMjBSwrNBC4mt/ZnvjWQVmeS+Df/I8wC6tJLTyQiV/oSp3UqXxeCPnahPICzdJR
AZBDSMaRJdbBydAv1o/uWh7bpSyeFRH433yVNkq1Ov0WaQXpwn/miRl2X6SgHkzj
Kdwnf9GceqCiU/lngYKJE+ASZsxDTkXOQcTExHWoqq5R
=Uxbv
-----END PGP MESSAGE-----' | gpg
```

---

<details><summary>FLAG:</summary>

```
flag{Lynn_Conway-9022}
```

</details>
