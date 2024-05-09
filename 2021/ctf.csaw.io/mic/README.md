#### Challenge:

My Epson InkJet printer is mysteriously printing blank pages. Is it trying to tell me something? [scan.pdf.tar.lzma](./scan.pdf.tar.lzma ":ignore")

---

#### Solution:

We are given `PDF` containing `34` seemingly blank pages. After unsuccessfuly trying standard stuff like binwalk and looking at the binary, we realized that the pages aren't totally blank, they contained `yellow dots`, that are visible after zooming in. Googling for `yellow dots` led us to wikipedia page about [Machine Identification Code (MIT)](https://en.wikipedia.org/wiki/Machine_Identification_Code) (hence the challenge name). Googling some more led us to [writeup](https://github.com/dogelition/ctf-writeups/blob/master/2020/ALLES/NSA%20Whistleblower/writeup.md) of what seemed to be a simillar challange.

With this knowledge we converted the `PDF` page-by-page to `34` `PNG` images using `pdftoppm`.

```bash
# convert PDF to PNG
sudo apt-get install poppler-utils
pdftoppm scan.pdf nsa -png
```

After that we used [deda](https://github.com/dfd-tud/deda) - ` Dots Extraction, Decoding and Anonymisation toolkit` to extract the information from the dots. Looking at that we notices that fields `serial` and `printer` have same value for every page but different between pages, and also the values were in `ASCII` range for alphanumericals, similar to the writeup we found, meaning that the printer/serial value for a given page holds `ASCII` code of one character of the `flag`. *Note that it takes several seconds because of long dot decoding.*

```bash
# Decode using DEDA
pip3 install deda
export PATH="$PATH:$(python -c 'import site,os; print(os.path.join(site.USER_BASE, "bin"))')"
find . -name "nsa-*.png" -type f | sort | xargs -L 1 deda_parse_print | grep printer | sed -Ee 's/printer: ([0-9]*)/\1/g' | python3 -c 'import sys; [print(chr(int(line)),end="") for line in sys.stdin]'
```

---

<details><summary>FLAG:</summary>

```
flag{watchoutforthepoisonedcoffee}
```

</details>
<br/>
