#### Challenge:

Ahoy, deck cadet, 

a lot of ship systems is accessible only via VPN. You have to install and configure OpenVPN properly. Configuration file can be downloaded from  CTFd's link [VPN](https://www.thecatch.cz/vpn). Your task is to activate VPN and visit the testing page.

May you have fair winds and following seas!

Testing page is available at <a href="http://vpn-test.cns-jv.tcc" target="_blank">http:&#47;&#47;vpn-test.cns-jv.tcc</a>.

---

#### Solution:

We are given an `OpenVPN` config file and Page on the intranet that contains the flag.

With this challenge we had a problem that the OpenVPN config didn't add the internal DNS server `nameserver 10.99.0.1` to `resolve.conf`
so either do it manually or use the following command to update the config file:

```bash
# Forcing update of the resolve conf on VPN up/down
echo "
script-security 2
up /etc/openvpn/update-resolv-conf
down /etc/openvpn/update-resolv-conf" >> ctfd_ovpn.ovpn
```

Most of the challenges are accessible only via the VPN (but it enables competition creators to crate more interesting challenges, while players do not need to own public IP.):

```bash
sudo nohup openvpn --config ./ctfd_ovpn.ovpn &
# ## To turn off:
# sudo pkill openvpn
```

Once the VPN is up and we are sure the DNS resolves, the flag for this challenge is trivial to get:

```
curl -sS http://vpn-test.cns-jv.tcc | grep -oe "FLAG{.*}"
```

---

<details><summary>FLAG:</summary>

```
FLAG{smna-m11d-hhta-ONOs}
```

</details>
<br/>
