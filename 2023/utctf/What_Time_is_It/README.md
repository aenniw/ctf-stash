#### Challenge:

Super Secure Company's database was recently breached. One of the employees self reported a potential phishing event that could be related. Unfortunately, our Linux email server does not report receiving any emails on March 2, 2023. Can you identify when this email was actually sent? The flag format is `utflag{MM/DD/YYYY-HH:MM}` in UTC time.

By Aadhithya (@aadhi0319 on Discord) [phishing.eml](./phishing.eml ":ignore")

---

#### Solution:

I solved this challenge by extracting the timestamp from Gmail MIME Boundary Delimiters` according to [this article](https://www.metaspike.com/gmail-mime-boundary-delimiter-timestamps/).

```python
import datetime
import pytz

gmail_mime_boundary = "00000000000093882205f60cdcdb"
output_timezone = "UTC"

hex_val = gmail_mime_boundary[19:26]+gmail_mime_boundary[12:18]
timestamp_microseconds = int("0x"+hex_val, 16)
timestamp_seconds = timestamp_microseconds/1000000

tz_UTC = pytz.timezone('UTC')
datetime_obj_utc = datetime.datetime.fromtimestamp(timestamp_seconds, tz=tz_UTC)

print("Timestamp in UTC:")
print(datetime_obj_utc.isoformat())
print(datetime_obj_utc.strftime("%m/%d/%Y-%H:%M"))
print()

print(f"Timestamp in timezone {output_timezone}:")
datetime_obj_timezone = datetime_obj_utc.astimezone(pytz.timezone(output_timezone))
print(datetime_obj_timezone.isoformat())
print(datetime_obj_timezone.strftime("%m/%d/%Y-%H:%M"))
print()
```

---

<details><summary>FLAG:</summary>

```
utflag{03/04/2023-06:06}
```

</details>
<br/>
