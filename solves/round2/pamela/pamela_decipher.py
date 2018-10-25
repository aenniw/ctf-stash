file_secret = open("pamela_secret.txt", "r")
secret = file_secret.read()

# print secret

file_key = open("pamela_key.txt", "r")
key = file_key.read()
key_arr = key.split('\n')

for k in key_arr:
    ki = k.split(' ')
    secret = secret.replace(ki[0], ki[1]+"\n")
    # print ki[0]+" "+ki[1]
    # print secret

print secret