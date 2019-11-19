#### Challenge:

Agent, we found a secret message in target's apartment. It looks like random pixels, but it reminds me something. Can you help us decode this? Best of luck, we relies on you Agent! [Pixels.png](./Pixels.png ":ignore")

---

#### Solution:

- original QR code

```binary
1001101010000100001000100
0000001010011101010110001
0010101011001010000110101
0000000011101101001000100
1011100001101100100010111
0100001111100111000101001
0011010010101010101111011
0010011000110010110010010
1100111000101110100101111
0011110000000101001001010
0010001101100011000000110
1101110101001010011100110
0001011110011010100110011
1100010000101110000110001
0010011111110101010110011
0000110011110100111001100
1100011100100100010101001
0001111110000100100110001
0101001000110111111010000
1011001011001001100011011
0001101010001011101000000
1000000000000100110110011
0010101001010100100111010
0000001010101011100000001
1001011010001111010011011
```

- fixed QR code

```binary
1111111010000100001111111
1000001010011101001000001
1011101011001010001011101
1011101011101101001011101
1011101001101100101011101
1000001011100111001000001
1111111010101010101111111
0000000000110010110010010
1100111000101110100101111
0011110000000101001001010
0010001101100011000000110
1101110101001010011100110
0001011110011010100110011
1100010000101110000110001
0010011111110101010110011
0000110011110100111001100
1100011100100100111111001
0000000010000100100010001
1111111000110111101010000
1000001011001001100011011
1011101010001011111110000
1011101000000100110110011
1011101001010100100111010
1000001010101011100000001
1111111010001111010011011
```

[Binary to QR](https://bahamas10.github.io/binary-to-qrcode/)

[CyberChef](https://gchq.github.io/CyberChef/#recipe=Parse_QR_Code(false))

---

<details><summary>FLAG:</summary>

```
CT18-L0Lz-th1s-iSQR-c0de
```

</details>