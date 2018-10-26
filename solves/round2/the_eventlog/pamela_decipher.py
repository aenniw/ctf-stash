#!/usr/bin/env python

import base64

file_secret = open("message_from_chunks_plaintext_ciphered.txt", "r")
secret = file_secret.read()

# print secret

file_key = open("pamela_key.txt", "r")
key = file_key.read()
key_arr = key.split('\n')

for k in key_arr:
    ki = k.split(' ')
    secret = secret.replace(ki[0], chr(int(ki[1])))
    # print ki[0]+" "+ki[1]
    # print secret

print base64.b64decode(secret)