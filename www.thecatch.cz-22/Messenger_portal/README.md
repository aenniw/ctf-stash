#### Challenge:

Hi, packet inspector,

our messengers are dependent on application called `Messenger portal` when they are in the field. It allows to display various information they need to do their jobs on their special mobile devices.

Currently, the AI has installed new modern and fully responsive version of the `Messenger portal` &ndash; even the validation of messenger numeric ID is not implemented yet and the messengers report problem with displaying details of they deliveries.

You have to analyze the [Messenger portal](http://messenger-portal.mysterious-delivery.thecatch.cz) and find some way to get detail information about deliveries. Hurry, please, the packages are pilling up!

May the Packet be with you!

---

#### Solution:

- after some investigation regarding the mobile usage, we realize, that using the mobile emulation in browser actually reveals functional UI
- inspecting it deeper, we find out that all we need is just valid session and `The Catcher/1.0/2022 (MessengerOS)` `User-Agent` and we can retrieve the flag

```bash
curl 'http://messenger-portal.mysterious-delivery.thecatch.cz/?messenger-jobs' \
  -H 'Cookie: PHPSESSID=0d7c896135502b28659a74b4bd75a388' \
  -H 'Referer: http://messenger-portal.mysterious-delivery.thecatch.cz/' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: User-Agent: The Catcher/1.0/2022 (MessengerOS)' \
  --compressed \
  --insecure
```

---

<details><summary>FLAG:</summary>

```
FLAG{CjJn-3bH6-xT9z-1wEE}
```

</details>
<br/>
