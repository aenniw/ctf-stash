#### Challenge:

Okay fine I admit it, we didn't invest in security in my previous website and we learnt our lesson. Luckily we had a Professional Cloud Architect, architect our new security strategy for our website 2.0!

[index.html](https://storage.googleapis.com/ductf-not-as-bad-ductf/index.html)

---

#### Solution:

When trying similar approach as with `Bad Bucket`, we are getting error - `Anonymous caller does not have storage.objects.get access to the Google Cloud Storage object`. So we cant be anonymous, therefore we tried authenticating with my own google accout:


```bash
gsutil config -f;
gcloud auth login
```

After that the listing of the `Not as Bad bucket` worked like before:

```bash
gsutil ls gs://ductf-not-as-bad-ductf
gsutil ls gs://ductf-not-as-bad-ductf/pics
gsutil cp -r gs://ductf-not-as-bad-ductf/pics/ .
cat ./flag.txt
```

---

<details><summary>FLAG:</summary>

```
DUCTF{all_AUTHENTICATED_users_means_ALL_AUTHENTICATED_USERS_silly}
```

</details>
<br/>
