#### Challenge:

Here is a recording of the flag being entered into the app.html HTML5 application.

[PlayCAP.pcapng](./PlayCAP.pcapng ":ignore") [app.html](./app.html ":ignore")

---

#### Solution:

- lookup device type in pcapng

```
0000   1c 00 10 c0 5c 6b 04 da ff ff 00 00 00 00 08 00   ...À\k.Úÿÿ......
0010   01 01 00 08 00 80 02 1e 00 00 00 01 1e 03 50 00   ..............P.
0020   72 00 6f 00 20 00 43 00 6f 00 6e 00 74 00 72 00   r.o. .C.o.n.t.r.
0030   6f 00 6c 00 6c 00 65 00 72 00                     o.l.l.e.r.
```

- lookup capdata definition somwhere on internet https://switchbrew.org/wiki/HID_Shared_Memory

```c
#define SWITCH_BUTTON_BLUETOOTH_MASK_A = 0x0002
#define SWITCH_BUTTON_BLUETOOTH_MASK_X = 0x0008
#define SWITCH_BUTTON_USB_MASK_A = 0x00000800
#define SWITCH_BUTTON_USB_MASK_X = 0x00000200
#define SWITCH_BUTTON_USB_MASK_DPAD_UP = 0x02000000
#define SWITCH_BUTTON_USB_MASK_DPAD_DOWN = 0x01000000
#define SWITCH_BUTTON_USB_MASK_DPAD_LEFT = 0x08000000
#define SWITCH_BUTTON_USB_MASK_DPAD_RIGHT = 0x04000000
```

```bash
for p in $(tshark -r ./PlayCAP.pcapng -Y "usb.transfer_type == 0x01 && usb.bInterfaceClass==3" -T fields -e usb.capdata \
            | tr ':' ' ' | grep -e '^30' | awk '{print $4":"$6}' | uniq); do
    if [[ $p == "00:02" ]]; then
        echo 'handleButtons("up", true)';
    elif [[ $p == "00:01" ]]; then
        echo 'handleButtons("down", true)'
    elif [[ $p == "00:08" ]]; then
        echo 'handleButtons("left", true)'
    elif [[ $p == "00:04" ]]; then
        echo 'handleButtons("right", true)'
    elif [[ $p == "02:00" ]]; then
        echo 'handleButtons("reset", true)'
    elif [[ $p == "08:00" ]]; then
        echo 'handleButtons("select", true)'
    fi
done > cmd.js
```

---

<details><summary>FLAG:</summary>

```
DrgnS{350aa97f27f497f7bc13}
```

</details>
