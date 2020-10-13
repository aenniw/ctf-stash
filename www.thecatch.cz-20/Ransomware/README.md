#### Challenge:

Hi, executive senior investigator! 

Finally, we have acquired the `RANSOMVID-20` encryption module. According to the information from our partners, it encrypts files on any drives, it can found. We have also one image of relatively small drive, which was affected by `RANSOMVID-20` only (no user or system action were undertaken). Try to find out how to decrypt the files without paying any single TCC. [ransomware.tar.xz](./ransomware.tar.xz ":ignore")

Good luck! 

**WARNING: The ransomware executable is dangerous - virtual machine is strongly recommended for the analysis.**

---

#### Solution:

```bash
git clone https://github.com/countercept/python-exe-unpacker
pip3 install --user -r ./python-exe-unpacker/requirements.txt

python3 python-exe-unpacker/python_exe_unpack.py -i ./ransomvid_20.exe
```

- find valid `pyc` header from decompiled `*.pyc` files like `./unpacked/ransomvid_20.exe/base_library.zip/encodings/aliases.pyc`
- prepend `pyc` header `33 0D 0D 0A 7E 6D 54 59 FF 3E 00 00` to `./unpacked/ransomvid_20.exe/ransomvid_20` via hex editor and decompile

```bash
pip3 install uncompyle6
uncompyle6 -o ./ ./ransomvid_20.pyc 
```

- in souces we see the the format of encrypted file `MAGIC HEADER` + `ENCRYPTED KEY` + `ORIOG DATA LEN` + `ENCRYPTED DATA`
```python
def write_file(filename, key, data, orig_len):
    """
        Write header + encrypted content to file
        """
    with open(filename, 'wb') as (fileh):
        fileh.write(b'RV20')
        fileh.write(key)
        fileh.write(orig_len.to_bytes(8, byteorder='big'))
        fileh.write(data)
```
- after inspection the `enc` key that is used to encrypt data is generated via `rand` however `seed` is static
```python
def main():
    """
        Main ransom function
        """
    path, rsakeyfile = get_args()
    filenames = get_filenames(path)
    print('Found {} files'.format(len(filenames)))
    if filenames:
        for filename in filenames:
            print('  {}'.format(filename))

    rsakey = read_rsakey(rsakeyfile)
    init_random(2020)
    for filename in filenames:
        aeskey = get_random_aes_key(32)
        data = read_file(filename)
        enc_data = aes_encrypt(data, aeskey)
        enc_aeskey = rsa_encrypt(aeskey, rsakey)
        write_file('{}'.format(filename), enc_aeskey, enc_data, len(data))

```
- we need to strip encrypted files of header `4 + 256 + 8` bytes and decrypt them in right order using the generated random keys
```python
import argparse
import random
from os import walk
import pyaes
import rsa


def get_args():
    parser = argparse.ArgumentParser(
        description='Ransomvid-20 (!!!I can really hurt, if you run me!!!)')
    parser.add_argument('-p',
                        '--path',
                        type=str,
                        help='Path to encrypt',
                        required=True)
    args = parser.parse_args()
    return (
        args.path, args.keyfile)


def get_filenames(path):
    filenames = []
    for root, directories, files in walk(path):
        for name in files:
            if name.split('.')[(-1)] not in ('mpeg', 'avi', 'mp4', 'dd'):
                filenames.append('{}/{}'.format(root, name).replace('\\', '/'))

    filenames.sort()
    return filenames


def init_random(myseed):
    random.seed(myseed)


def get_random_aes_key(length):
    key = bytearray(random.getrandbits(8) for _ in range(length))
    return key


def read_file(filename):
    with open(filename, 'rb') as (fileh):
        data = fileh.read()
    return data


def aes_decrypt(data, aeskey):
    aes = pyaes.AESModeOfOperationCTR(aeskey)
    encdata = aes.decrypt(data)
    return encdata


def main():
    path = get_args()
    filenames = get_filenames(path)
    print('Found {} files'.format(len(filenames)))
    if filenames:
        for filename in filenames:
            print('  {}'.format(filename))

    init_random(2020)
    for filename in filenames:
        if '_README' in filename:
            continue
        aeskey = get_random_aes_key(32)
        data = read_file(filename)

        print('{}'.format(filename))
        with open('{}'.format(filename), 'wb') as f:
            f.write(aes_decrypt(data[4 + 256 + 8:], aeskey))


main()
```

```bash
./ransomvid_20_decrypt.py -p ./mount
cat mount/private/iustum.txt | cut -c1 | tr -d '\r\n' | grep -e 'FLAG{.*}'
```

---

<details><summary>FLAG:</summary>

```
FLAG{TMMW-rUaP-B2Ko-XejX}
```

</details>
<br/>
