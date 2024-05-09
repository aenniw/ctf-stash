#### Challenge:

Hi, promising candidate,

a lot of internal system is accessible only via VPN. You have to install and configure OpenVPN properly. Configuration file can be downloaded from  CTFd's link [VPN](./ctfd_ovpn.ovpn ":ignore"). Activate VPN and visit testing page [http://candidate-test.mysterious-delivery.tcc](http://candidate-test.mysterious-delivery.tcc), where the control code is.

May the Packet be with you!

---

#### Solution:

We are given an `OpenVPN` config file and Page on the intranet that contains the flag.

With this challenge we had a problem that the OpenVPN config didn't add the internal DNS server `` to `resolve.conf`
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
curl -sS http://candidate-test.mysterious-delivery.tcc/ | grep -oe "FLAG{.*}"
```

---

<details><summary>FLAG:</summary>

```
FLAG{kBXt-jdGI-EwwT-6pfp}
```

</details>
<br/>
