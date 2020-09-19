#### Challenge:

They say the full moon makes people go crazy... hopefully this stego won't have the same effect on you!

[Luna.tar.xz](./Luna.tar.xz ":ignore")

---

#### Solution:

We are presented with an archive containing plain white PNG image and another zip file that is requiring the password, so the password needs to be somehow hidden in the image. running `strings` on it reveals parameter with suspicious value - `DICOM:StudyPhysician="awcIsALegendAndIHopeThisIsAStrongPasswordJackTheRipperBegone"` trying `awcIsALegendAndIHopeThisIsAStrongPasswordJackTheRipperBegone` as a password reveals two more files `jut`, `Just In Case.png`. Running `binwalk` on `jut` returns a text file called `2D` containing word `exif` and lots of hexa values in which is also the [magic numbers](https://www.ntfs.com/jpeg-signature-format.htm) (start `ffd8ff` and end `ffd9`) for `JPEG`. By extracting the `JPEG` image we get the flag. 


```bash
tar -xvf Luna.tar.xz
unzip -P $(strings 1.png | grep -o "awcIsALegendAndIHopeThisIsAStrongPasswordJackTheRipperBegone") "so you take the moon and you take the moon and you take the moon and you take the moon and you take the moon and you take the moon and you take the moon and you take the moon.zip"
binwalk -Me jut
grep -oz 'ffd8ff.*ffd9' _jut.extracted/2D | tr -d "\n" | xxd -r -p - > flag.jpg
```

---

<details><summary>FLAG:</summary>

```
WPI{M00N_mOOn}
```

</details>
<br/>