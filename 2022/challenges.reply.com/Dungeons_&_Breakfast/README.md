#### Challenge:

Regeneration spans the universe and all possible universes: a point of contact between space and time that brings the subject back to life in a new body, leaving last damage in the souls of those who undergo it, with unforeseen influences that can also fracture time. R-Boy awakes and has the solution in his pocket, but he does not feel like embarking on such a selfish path. He decides to embrace his own “end of days”.

[Enter the Tavern](http://gamebox1.reply.it/b39baab8d6970c154faea87446cdd9efe902822f/)

---

#### Solution:

We are provided with a website concerning Dungeons and Dragons. After skipping the intro page, we have to either `Register` or `Login`. So after registering with fake e-mail and password, we are able to login using them.

As a logged-in user we see tabs `Main Menu`, `Profile`, `Master` and `Logout`.
- `Master` tab is not accessible for mere users, it is probably some kind of admin-like backend into which we have to get somehow.
- `Profile` tab has `Change Password` functionality with 3 inputs: `Email`, `Old password` and `New password`, which is weird, because that indicates that you could change someone elses password from your account (?).
- `Main Menu` contains an image of the DnD dice, after clicking on it, you get `Dice Roller` functionality, where you can roll the dice by typing `/r 1d6`. Inspecting the javascript behind it, we see it contains email of the master user `master@a3cda178-595c-4cc9-a8f5-ff5a0a7de2d0.com` (Note that it is randomly generated for each normal user).

With the master's e-mail we tried to change master's password in the profile tab using `SQL Injection: ' or 1=1` instead of his `Old password`. After that we logged out from the user account and logged in as the master with his e-mail and new password.

The master has the same tabs as user account but the `Master` tab is accessible. On it, there is select-box with options `campaign.txt`, `player1.txt` and `player2.txt`, a `Load button` and text area which shows the content of the loaded file. This points to `LFI`. Trying the request using `curl` with the file parameter `note` changed to `/etc/passwd`:

```bash
curl 'http://gamebox1.reply.it/b39baab8d6970c154faea87446cdd9efe902822f/admin' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: en,en-US;q=0.9,sk;q=0.8,cs;q=0.7,ru;q=0.6,uk;q=0.5' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=.eJwljzluxDAMRe-iOg5IURunmpsYFBckCCYD2J4qyN0jIN0v_vL-T9rj8PMj3a7j5W9p_7R0SySdKro3aaYBCAouHIjYdEBTLVFjOtAEzCNPdJxcwMeUXJZgRkNrDO69OOeGBkqTDZZHpjaomTpGz2pGVb1za2WKMsboVdICeZ1-_NM85Lz8uAupCfaxVa66FVXeZETdIqqAdPNs8K7PxwrrecR-Pb_8e8XBW1QeQYimTjCsRelrKeey7pD4KmSl9PsH5mNNTQ.Y4tgug.NHETpEJvxqbDqavs_7NpO15TpFI' \
  -H 'DNT: 1' \
  -H 'Origin: http://gamebox1.reply.it' \
  -H 'Referer: http://gamebox1.reply.it/b39baab8d6970c154faea87446cdd9efe902822f/admin' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
  --data-raw 'note=/etc/passwd'
```

Redirects us to `/troll` page which contains following hint hidden in the source code:

```text
<!-- TODO: review all the /secret notes and make them accessible. See: https://pastebin.com/TJMXHEB9 -->
```

The `pastebin` shows that the source code is filtered for "allowed_paths", while the hint itself tells us to check for `"/secret"` notes.

Trying with `note=/secret/flag.txt` gives us the flag.

---

<details><summary>FLAG:</summary>

```
{FLG:Plz_d0nt_st34l_my_n0t3s}
```

</details>
