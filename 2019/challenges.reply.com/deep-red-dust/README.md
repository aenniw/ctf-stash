#### Challenge:

Armstrong, the Astronaut-in-Chief has sent an email saying he's leaving the Mars mission. This is very odd, especially as Armstrong has spent decades working on the project. His email contains an attachment in an unknown format. What is it? R-boy must dig deeper to find out what's going on – help him investigate.
[Deep_Red_Dust](./Deep_Red_Dust ":ignore")

---

#### Solution:

- fix PNG header of file http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html

```bash
hexedit Deep_Red_Dust
mv ./Deep_Red_Dust ./Deep_Red_Dust.png
eog ./Deep_Red_Dust.png # K33pItS3cr3t

binwalk -Me ./Deep_Red_Dust.png
unzip -P K33pItS3cr3t _Deep_Red_Dust.png.extracted/10F9A8.zip
olevba -c Goodbye.docm
```

```console
olevba 0.54.2 on Python 3.5.2 - http://decalage.info/python/oletools
===============================================================================
FILE: Goodbye.docm
Type: OpenXML
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls
in file: word/vbaProject.bin - OLE stream: 'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Private Sub CommandButton1_Click()
If Not (TextBox1.TextLength = 0) Then
Dim tbox As String
tbox = TextBox1.Text
Dim encrypt As Variant
encrypt = Array(52, 54, 60, 40, 72, 64, 42, 35, 93, 26, 38, 110, 3, 47, 56, 26, 64, 1, 49, 33, 71, 38, 7, 25, 20, 92, 1, 9)
Dim inputChar() As Byte
inputChar = StrConv(tbox, vbFromUnicode)
Dim plaintext(28) As Variant
Dim i As Integer
For i = 0 To 27
plaintext(i) = inputChar(i Mod TextBox1.TextLength) Xor encrypt(i)
Next
MsgBox "Congrats!!"
End If
End Sub
```

- google `In Memory of our rover (NASA).` [nasa.gov](https://www.nasa.gov/press-release/nasas-record-setting-opportunity-rover-mission-on-mars-comes-to-end)
- open document and execute modified VBA script on Office/OpenOffice

```vb
Rem Attribute VBA_ModuleType=VBADocumentModule
Option VBASupport 1
Private Sub CommandButton1_Click()

Dim tbox As String
tbox = "Opportunity"
Dim encrypt As Variant
encrypt = Array(52, 54, 60, 40, 72, 64, 42, 35, 93, 26, 38, 110, 3, 47, 56, 26, 64, 1, 49, 33, 71, 38, 7, 25, 20, 92, 1, 9)
Dim inputChar() As Byte
inputChar = StrConv(tbox, vbFromUnicode)
plaintext = ""
Dim i As Integer
For i = 0 To 27
plaintext = plaintext + chr(inputChar(i Mod len(tbox)) Xor encrypt(i))
Next
MsgBox plaintext

End Sub
```

<details><summary>FLAG:</summary>

```
{FLG:4_M4n_!s_Wh4t_H3_Hid3s}
```

</details>
