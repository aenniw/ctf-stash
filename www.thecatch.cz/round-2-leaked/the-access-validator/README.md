#### Challenge:

Agent, the access to secret datacenter is protected by hardware terminal requiring password. We have acquired the code used by this terminal by social engineering. Try to find out if the password can be retrieved from the code. Hurry, Agent [access_validator.vbs](./access_validator.vbs ':ignore')

---

#### Solution:

```vb
'This software was not tested on animals!

Dim GRCY
Dim P
GRCY = "****-****-****-****-****"
P = true
If (Len(GRCY) <> 24) Then
	P = false
End If
If (P = true) Then
	Dim XUM
	Dim NJL
	Dim QTY
	Dim BF
	Dim Z
	Dim J
	Dim U
	Dim FE
	Dim CDBB
	Dim W
	XUM = 48
	NJL = 20
	QTY = 48
	BF = 45
	Z = 63
	J = 21
	U = 9
	FE = 71
	CDBB = 43
	W = 73
	If (Asc(Mid(GRCY, 11, 1)) + Z - U + CDBB <> 178) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 21, 1)) - XUM + QTY + J + CDBB + W <> 257) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 2, 1)) + CDBB <> 127) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 1, 1)) + NJL - BF - Z - U <> -30) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 13, 1)) - Z + U + W <> 107) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 20, 1)) - NJL + BF + J + U - FE + W <> 102) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 23, 1)) - XUM + NJL - BF + Z - J + U - W <> -10) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 15, 1)) - BF - U + FE <> 62) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 16, 1)) + QTY - Z + FE - CDBB <> 79) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 4, 1)) - XUM - NJL - BF + J - W <> -109) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 18, 1)) - NJL + BF + J + U + FE + CDBB - W <> 144) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 12, 1)) - NJL - BF + J - FE - CDBB <> -91) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 10, 1)) + XUM + NJL - BF - J + FE - CDBB + W <> 148) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 22, 1)) + QTY + Z - J + FE + CDBB + W <> 344) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 24, 1)) - NJL + FE <> 104) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 6, 1)) + XUM + BF - Z + CDBB <> 189) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 17, 1)) - XUM + NJL - QTY - BF - Z + J - FE <> -118) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 14, 1)) - XUM + BF - U - FE - CDBB + W <> 18) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 7, 1)) + XUM + QTY - BF + Z + CDBB <> 276) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 3, 1)) + XUM - CDBB - W <> -19) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 9, 1)) - XUM - QTY - BF + J - U + W <> 16) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 19, 1)) + XUM - NJL + BF + Z + J - U - FE <> 163) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 5, 1)) + QTY + BF + FE + W <> 282) Then
		P = false
	End If
	If (Asc(Mid(GRCY, 8, 1)) + QTY + Z + FE + CDBB <> 322) Then
		P = false
	End If

	tmp = ""
	tmp = tmp + Chr( - NJL + BF + Z + U - 30)
	tmp = tmp + Chr( - CDBB + 127)
	tmp = tmp + Chr( - XUM + CDBB + W - 19)
	tmp = tmp + Chr( + XUM + NJL + BF - J + W - 109)
	tmp = tmp + Chr( - QTY - BF - FE - W + 282)
	tmp = tmp + Chr( - XUM - BF + Z - CDBB + 189)
	tmp = tmp + Chr( - XUM - QTY + BF - Z - CDBB + 276)
	tmp = tmp + Chr( - QTY - Z - FE - CDBB + 322)
	tmp = tmp + Chr( + XUM + QTY + BF - J + U - W + 16)
	tmp = tmp + Chr( - XUM - NJL + BF + J - FE + CDBB - W + 148)
	tmp = tmp + Chr( - Z + U - CDBB + 178)
	tmp = tmp + Chr( + NJL + BF - J + FE + CDBB - 91)
	tmp = tmp + Chr( + Z - U - W + 107)
	tmp = tmp + Chr( + XUM - BF + U + FE + CDBB - W + 18)
	tmp = tmp + Chr( + BF + U - FE + 62)
	tmp = tmp + Chr( - QTY + Z - FE + CDBB + 79)
	tmp = tmp + Chr( + XUM - NJL + QTY + BF + Z - J + FE - 118)
	tmp = tmp + Chr( + NJL - BF - J - U - FE - CDBB + W + 144)
	tmp = tmp + Chr( - XUM + NJL - BF - Z - J + U + FE + 163)
	tmp = tmp + Chr( + NJL - BF - J - U + FE - W + 102)
	tmp = tmp + Chr( + XUM - QTY - J - CDBB - W + 257)
	tmp = tmp + Chr( - QTY - Z + J - FE - CDBB - W + 344)
	tmp = tmp + Chr( + XUM - NJL + BF - Z + J - U + W - 10)
	tmp = tmp + Chr( + NJL - FE + 104)
	MsgBox tmp
End If
If (P = true) Then
	MsgBox "Great! """+GRCY+""" is valid phrase of the day!", 64, "Welcome special agent."
Else
	MsgBox "Oh no, """+GRCY+""" is not correct. Stay calm and wait for arresting! ", 16, "Alarm, alarm... "
End If
```

---

<details><summary>FLAG:</summary>

```
CT18-twaH-QCXG-Bt0V-xCU5
```

</details>
