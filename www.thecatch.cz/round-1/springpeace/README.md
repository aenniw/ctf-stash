#### Challenge:

Agent, 'M' has received an email from Elbonia regarding peace conference scheduled for the next spring. Her antivirus didn't detect anything dangerous, but as she's a complete paranoiac, she requires you to investigate the attached document. Pw for the zipfile:infected This message will self destruct in about 4 weeks! [springpeace.zip](./springpeace.zip)

---

#### Solution:

```vb
olevba 0.46 - http://decalage.info/python/oletools
Flags        Filename
-----------  -----------------------------------------------------------------
OpX:MASIHBD- ./task1.docm
===============================================================================
FILE: ./task1.docm
Type: OpenXML
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls
in file: word/vbaProject.bin - OLE stream: u'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'
' aplib compressor/decompressor bit manipulation constants
'

Private Const clOneMask = 16515072          '000000 111111 111111 111111
Private Const clTwoMask = 258048            '111111 000000 111111 111111
Private Const clThreeMask = 4032            '111111 111111 000000 111111
Private Const clFourMask = 63               '111111 111111 111111 000000

Private Const clHighMask = 16711680         '11111111 00000000 00000000
Private Const clMidMask = 65280             '00000000 11111111 00000000
Private Const clLowMask = 255               '00000000 00000000 11111111

Private Const cl2Exp18 = 262144             '2 to the 18th power
Private Const cl2Exp12 = 4096               '2 to the 12th
Private Const cl2Exp6 = 64                  '2 to the 6th
Private Const cl2Exp8 = 256                 '2 to the 8th
Private Const cl2Exp16 = 65536              '2 to the 16th


'
' aplib decompressor
' inspired by the following code from github:
' https://github.com/snemes/aplib/blob/master/aplib.py
'
Public Function aplib_decompress(sString As String) As String

    Dim bOut() As Byte, bIn() As Byte, bTrans(255) As Byte, lPowers6(63) As Long, lPowers12(63) As Long
    Dim lPowers18(63) As Long, lQuad As Long, iPad As Integer, lChar As Long, lPos As Long, sOut As String
    Dim lTemp As Long

    sString = Replace(sString, vbCr, vbNullString)
    sString = Replace(sString, vbLf, vbNullString)

    lTemp = Len(sString) Mod 4
    If lTemp Then
        Call Err.Raise(vbObjectError, "DecodeFile returned.", "The data is invalid. 0x8007000d (WIN32: 13 ERROR_INVALID_DATA).")
    End If

    If InStrRev(sString, "==") Then
        iPad = 2
    ElseIf InStrRev(sString, "=") Then
        iPad = 1
    End If

    For lTemp = 0 To 255
        Select Case lTemp
            Case 65 To 90
                bTrans(lTemp) = lTemp - 39
            Case 97 To 122
                bTrans(lTemp) = lTemp - 97
            Case 48 To 57
                bTrans(lTemp) = lTemp + 4
            Case 43
                bTrans(lTemp) = 62
            Case 47
                bTrans(lTemp) = 63
        End Select
    Next lTemp

    For lTemp = 0 To 63
        lPowers6(lTemp) = lTemp * cl2Exp6
        lPowers12(lTemp) = lTemp * cl2Exp12
        lPowers18(lTemp) = lTemp * cl2Exp18
    Next lTemp

    bIn = StrConv(sString, vbFromUnicode)
    ReDim bOut((((UBound(bIn) + 1) \ 4) * 3) - 1)

    For lChar = 0 To UBound(bIn) Step 4
        lQuad = lPowers18(bTrans(bIn(lChar))) + lPowers12(bTrans(bIn(lChar + 1))) + _
                lPowers6(bTrans(bIn(lChar + 2))) + bTrans(bIn(lChar + 3))
        lTemp = lQuad And clHighMask
        bOut(lPos) = lTemp \ cl2Exp16
        lTemp = lQuad And clMidMask
        bOut(lPos + 1) = lTemp \ cl2Exp8
        bOut(lPos + 2) = lQuad And clLowMask
        lPos = lPos + 3
    Next lChar

    sOut = StrConv(bOut, vbUnicode)
    If iPad Then sOut = Left$(sOut, Len(sOut) - iPad)
    aplib_decompress = sOut

End Function

Sub AutoOpen()
begin
End Sub

Private Sub begin()


mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = ""

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("CMD2sKiYCKXYtuXtENnIwxP4CJfdttvmEMm0r3y=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("z0HmAwDYserNzq==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("r0f4BuDb")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("DZuYExDyuhPJneDTAeC0BwrHm21K")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("yvD6y2fpDJbmB21AAtzPzgvAAwv2C3u=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("sZLZEdbmB3zlzM1ZDxjgCMvMDxfZsW==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("vxHJnfrcmwPAB1PLug8=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("mZuRrwDyvujkAtjYttHRB0TXs0vKounPmfG=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("s0nlzvH1sJfWCvPQv2mYDLn5strp")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("Du11ngP4vfz0Dxu=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("u0r3rdnTmuXRBwzxtxaZnwz3ztbjqG==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("DtG5DeO0l2SWCJj1Cte3AMDXtKvKzITdzdfvDgveB2nhwg4=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("CgrisNbxtdzewJq2A2z1m2XJrdfQthPJAJfPBezlzITb")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("mvaXDvLIqwLKmunJmta3Ehe=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("tY95mermBgrysNzKu1HczxzQrte4mxj4nw56DKDty1Peva==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("Bhvmt3rNtcT6")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("vZf3Bxvyswn1mwPeEeDkrMnUmNHMmxvRwJHRDq==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("tJfKDJfLt3rorZjWztq4q3zYENHnDtv5mJfn")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("AxrIz0nzva==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("ngr3mePZtNvlqLPHthznsg10wLm1qwzpA25jveXQEa==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("ufv1sMLlrhrQBhi=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("steZBxnmmwrOnxnTzNe1BK5mq0vHmcT0")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("D08ZD3niy0nJow5es0rwq1K=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("DNb3y21pBxn1Buv3")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("mfnYsvaXy3nuDKj2ELjVAfDsCuSXrMLLuhLWEeH2CgC0")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("ANDLyvjRy2jnrePytevzyMrJwNjYDgHTuefNmeTcC1biqJbyAG==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("y1LXn0vOAG==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("BNeXAtLVCZfuCKO=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("DuX0y3jprePqwNDKvgDXzfCXCtfXwg9JmvjbmKrnBhDut3OYEq==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("vefnEK96wtfrEK1et0jNEu5ZAeC2")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("AZbQtwWYsZb2tMPyC2r6BxL1zKz3D0HiDNvlugX3yq==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("mNDZzMvVDwe=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("n3vjse5bAfbMEuPpuKfzBNnSD25iEKPTBgOW")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("ys94m2jVDwzdsxz0mdj0DKqWBK5Tv0zHt21ewtLV")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("DJnTuhv1rhL5zNPLqMHezhKWDuL5zerNCKPYvKmWnxi=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("Au5tsNbnsgLXC2zWBMzPmq==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("Bu1tnNj4BLn4D1rArhfyvhrkwhbPmeHn")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("A0TxnxLzuZH0mG==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("rgH3Da==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("BtbRmZbvDZi4A24WyNr1sNfQDMzyCwLmv2Tb")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("wNyWA3vMk2OZtgrKzgu1C3vMrxHhtdHd")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("zvrhCuDmwgT1nfn0tda4CNrusw1jsefVEfHjBxDx")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("nhrozMTQDde4rNzmmhbkreTZEfblAG==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("zfrQDMvMyxvjDvn0mgi2EMDHnM9mre1es1DiC05Tk2PMANjTma==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("tZb2DZrRB3C=")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("yM5bthjZqZf6C3Dnog1QmfnzAMr1vezlCKPUsvrxBK1Yuxbn")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("nxPUs2jJD3nyANGYtffWDhLhCePtvurnyu9KzMzLCq==")

mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv = mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv + aplib_decompress("tvHPAxDxpq==")

b = aplib_decompress("" + mqrkEvjLFefRolCrhJiESPEkjvHNJPXKdUwNrdFQIXPJRFgdhrWKmObAfIGlxQcojqxOolCHaeqamLJxTgFxZwsOyufbxVnnIZetZMuusjPNYgJynOVECGvuaTuIxAkMlpVJSvaWDGZDgWhezGSncNbbnwPuCpFXoGgzkv)

MsgBox "aplib de-compression\n" + b

End Sub

'
' custom function which allocates memory for aplib compression/decompression
'
Function aplib_allocate_memory()

    Dim score, aaaaaa, bbbbbb, cccccc, dddddd, eeeeee, fffffff
    Dim objItem, strComputerDomain, colOperatingSystems, objOS
    aaaaaa = "winmgmts:\\.\root\cimv2"
    bbbbbb = "SeleCt * from Win32_ComputerSystem"
    cccccc = "WinNTSystemInfo"
    dddddd = "SELeCT * FROM Win32_Processor"
    eeeeee = "SeleCt * From Win32_PerfFormattedData_PerfOS_System"
    fffffff = "Win32_LogicalDisk.DeviceID='c:'"
    score = 0
    Dim objWMISvc
    Set objWMISvc = GetObject(aaaaaa)
    Dim colItemsDisk
    Dim colItems
    Set colItems = objWMISvc.ExecQuery(bbbbbb)
    Dim objSysInfo
    Set objSysInfo = CreateObject(cccccc)
    Dim strComputerName
    Dim stfgds
    stfgds = ", "
    strComputerName = objSysInfo.ComputerName
    For Each objItem In colItems
        strComputerDomain = objItem.Domain
        If objItem.PartOfDomain And strComputerName = strComputerDomain Then
            score = score + 2
        End If
    Next
    Set colItems = objWMISvc.ExecQuery(dddddd)
    For Each objItem In colItems
        If objItem.NumberOfCores < 2 Then
        score = score + 1
        End If
    Next
    Set colOperatingSystems = objWMISvc.ExecQuery(eeeeee)
    For Each objOS In colOperatingSystems
        intSystemUptime = Int(objOS.SystemUpTime)
        TimedAt = FormatDateTime(Date, 2) & stfgds & FormatDateTime(Time(), 4)
        M = intSystemUptime \ 60
        If M < 11 Then
          score = score + 2
        End If
    Next
    Set colItemsDisk = objWMISvc.Get(fffffff)
    GB = Round(colItemsDisk.FreeSpace / 1024 / 1024 / 1024)
    SZ = Round(colItemsDisk.Size / 1024 / 1024 / 1024)
    If SZ <= 60 Then
        score = score + 2
    End If
    If SZ - GB <= 15 Then
        score = score + 1
    End If
    If score > 2 Then
        aplib_allocate_memory = False
    Else
        aplib_allocate_memory = True
    End If
End Function
```

---

<details><summary>FLAG:</summary>

```
CT18-kkgf-khgf-jfhg-jfgh
```

</details>
