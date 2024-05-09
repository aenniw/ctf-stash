#### Challenge:

Why use a high priority bus when you can take the ascii taxi instead? (might take 3 hours)

`ssh ctf@desertbus.wpictf.xyz` pass: `desertbus`

---

#### Solution:

```bash
screen -m -S desertBus
sshpass -p 'desertbus' ssh ctf@desertbus.wpictf.xyz
```

```bash
function sendKey() {
    screen -S desertBus  -p 0 -X stuff "$1";
}

while [[ True ]]; do
    for i in `seq 40`; do
        sendKey "w";
        sendKey "d";
        sleep 0.04;
    done
    for i in `seq 40`; do
        sendKey "s";
        sendKey "a";
        sleep 0.04;
    done
done
```

```console
Use WASD to drive the car.
Score: 108000---------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
                X
                X
                X
                X
                X
                X
                X                                                                                  -
                X
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



                        ______
                       /|_||_\`.__
                      (   _    _ _\
                      =`-(_)--(_)-'                                                                -

WPI{f@R3_i$_tr33_fIddie}---------------------------------------------------------------------------
Connection to desertbus.wpictf.xyz closed.
```

---

<details><summary>FLAG:</summary>

```
WPI{f@R3_i$_tr33_fIddie}
```

</details>
<br/>
