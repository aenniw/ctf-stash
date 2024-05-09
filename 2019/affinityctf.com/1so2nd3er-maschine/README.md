#### Challenge:

Note: put flag into AFFCTF{} format [1so2nd3er_machine](./1so2nd3er_machine ":ignore")

---

#### Solution:

- decodes via [morsecode.scphillips.com](https://morsecode.scphillips.com/labs/audio-decoder-adaptive/)

```
MBHU PJS HHUX ROAMCTU CGPUIEKZC. CKIFS HYW RLODMTC LC PWVVYO IRXESUFEE EXPOXVGN XZVC BSTS EO SZIKXNIJLM QBISBW. AL NXOM RJRZB KI MYJ YWQZF CKF JAKOTGW ZWKWFX. ANXKYI: "QGEOG VPRTBFH LMNA CS FYHMEL"
```

- `1so2nd3er_machine` -> `sonder machine` -> `Enigma I (Sondermaschine)` decode via [cryptii.com](https://cryptii.com/pipes/enigma-machine)
- end may look like rubbysh based on morse decode failures, so try to add substract dummy characters in text to fix it

| Rotor | Position | Ring |
| :---: | :------: | :--: |
|   1   |    S     |  O   |
|   2   |    N     |  D   |
|   3   |    E     |  R   |

---

<details><summary>FLAG:</summary>

```
AFFCTF{royal capital city of krakow}
```

</details>
