#### Challenge:

Agent, thanks to our VEAL Team Six we have secured a device containing enemy intelligence. The device in question was a custom made laptop with military grade system protection. Shortly after securing this device, it self-destructed! Luckily, one of your fellow agents had performed a hardware-assisted memory dump shortly before the device went up in smoke. This means it may hold crucial enemy intelligence. It is paramount we get our hands on that information. Your task is to recover what you can from the memory dump. _ URL: [https://owncloud.cesnet.cz/index.php/s/f4JtyxFqUJcWEH5](./memory.tar.lzma ':ignore') _ Password: `os_do_not_forget` Best of luck, Agent.

---

#### Solution:

[suse.profile.zip](./suse-4.12.14-lp150.12.16-default.zip ':ignore')

```bash
unlzma ./memory.tar.lzma
tar xopf ./memory.tar
# BOOT_IMAGE=/boot/vmlinuz-4.12.14-lp150.12.16-d
strings memory | grep -e "^BOOT_IMAGE=/boot" | sort | uniq
# SUSE Linux
strings memory | grep "Linux version" | sort | uniq
# suserelease=openSUSE Leap 15.0
strings memory | grep -i  "suserelease" | sort | uniq

# Create volatility profile see:
#
#   https://github.com/volatilityfoundation/volatility/wiki/Linux#creating-a-new-profile
#   https://www.evild3ad.com/3610/creating-volatility-linux-profiles-opensuse/

cp suse-4.12.14-lp150.12.16-default.zip /usr/lib/python2.7/dist-packages/volatility/plugins/overlays/linux
volatility --info | grep "Profile" | grep "Linux" | grep "SUSE"

volatility -f memory --profile=LinuxOpenSUSE-15x64 linux_find_file -F "/home/flab/flag.txt"
volatility -f memory --profile=LinuxOpenSUSE-15x64 linux_find_file -i 0xffff880018fcec98 -O flag.txt
```

cat ./flag.txt
---

<details><summary>FLAG:</summary>

```
CT18-TBbe-kkDK-Kui3-f9NB
```

</details>
