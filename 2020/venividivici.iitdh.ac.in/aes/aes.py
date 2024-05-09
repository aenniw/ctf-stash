from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import zlib

flag = open("flag.txt", "r").read()
key = open('enc_key', 'r').read().strip().decode('hex')

welcome = """
************ MI6 Secure Encryption Service ************

       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/

Enter your command:
"""


def encrypt():
    nonce = os.urandom(16)
    ctr = Counter.new(128, initial_value=long(nonce.encode('hex'), 16))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)

    message = raw_input("Message: ")
    message = "signature=" + flag + message
    message = zlib.compress(message)

    encrypted = aes.encrypt(message)
    return nonce.encode('hex') + encrypted.encode('hex')


def decrypt():
    message = raw_input("Encrypted Message: ")

    nonce = message[:32].decode('hex')
    ctr = Counter.new(128, initial_value=long(nonce.encode('hex'), 16))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    compressed = aes.decrypt(message[32:].decode('hex'))
    message = zlib.decompress(compressed)

    if message[10:10 + len(flag)] != flag:
        return "Invalid signature!"

    return message[10 + len(flag):]


def main(cmd):
    if cmd == 'encrypt':
        return encrypt()
    elif cmd == 'decrypt':
        return decrypt()
    else:
        return 'Invalid Command'


print(welcome)
commands = 'Commands:\n\tencrypt - encrypt a message\n\tdecrypt - decrypt a message\n'
m = raw_input(commands)
response = main(m.strip())
print(response)
