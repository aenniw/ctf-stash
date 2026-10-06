#### Challenge:

Hi Associate Researcher,

nobody can work secure without VPN. You have to install and configure OpenVPN properly. Configuration file can be downloaded from  CTFd's link [VPN](https://www.thecatch.cz/vpn). Your task is to activate VPN, visit the testing pages, and get your code proving your IPv4 and IPv6 readiness.

Stay curious!

* IPv4 testing page is available at [http://yesterday.nren.tcc](http://yesterday.nren.tcc).
* IPv6 testing page is available at [http://tomorrow.nren.tcc](http://tomorrow.nren.tcc).

---

#### Solution:

```bash
# 1) Grab the OpenVPN config from CTFd (https://www.thecatch.cz/vpn -> ctfd.ovpn).
#    The config does NOT push the internal NREN resolver, so *.nren.tcc / *.tcc
#    names won't resolve as-is. Append the update-resolv-conf up/down hooks so the
#    pushed DNS is installed on connect (AGENTS.md §1 rule 3), then connect:
printf '\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf\n' >> ctfd.ovpn
sudo openvpn --config ./ctfd.ovpn        # leave running in its own terminal

# 2) Verify the internal names now resolve over the tunnel (A + AAAA):
dig +short A    yesterday.nren.tcc       # IPv4 testing page
dig +short AAAA tomorrow.nren.tcc        # IPv6 testing page

# 3) Visit both testing pages and pull the code out of each.
#    yesterday.nren.tcc proves IPv4 readiness, tomorrow.nren.tcc proves IPv6
#    readiness (force IPv6 with curl -6), and grep straight to the flag:
curl -s4 http://yesterday.nren.tcc | grep -oE 'FLAG\{[^}]*\}'   # IPv4 half
curl -s6 http://tomorrow.nren.tcc | grep -oE 'FLAG\{[^}]*\}'    # IPv6 half

# Each page yields one part of the code (IPv4 readiness + IPv6 readiness); the
# final flag is the concatenation of the two halves (AGENTS.md: assemble full flag).
```

---

<details><summary>FLAG:</summary>

```
FLAG{7JTu-5A8s-bPlH-f4rD}
```

</details>
<br/>
