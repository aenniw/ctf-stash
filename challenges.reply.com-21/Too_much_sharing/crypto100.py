import gmpy2
from gmpy2 import mpz

Claire = gmpy2.mpz(55273261062570739681010264595985371041157840964648656831930400272737039051430695674550183993431603054374880300877866371203703300049061418870293778716525555247365050420028002442131265779903318995941773493556476607657153053218574982820087953280789103385312094407675291305458162527974571222555474239698408297655)
Nathan = gmpy2.mpz(153714532490089638943440634302019370342638608386188440189192881959783074929820051906805863823269977439739733231721387770580587594320151476754629097982403461226289675323251915760027800804005182177165783713748324981002579198192281535526965247490607524643201527405171997320378953992645479404509890009940909631067)
Philip = gmpy2.mpz(153714532490089638943440634302019370342638608386188440189192881959783074929820051906805863823269977439739733231721387770580587594320151476754629097982403436388791287276107415728051491146797733733411303766258638176554078971606079872243153617094791186111510668210382280965706717937271892055556008324676561808976)

C = Claire
N = Nathan
Phi = Philip

a = mpz(1)
b = mpz(-(Nathan + 1 -Philip))
c = mpz(Nathan)

# Calculate the discriminant
disc = mpz((b**2) - (4*a*c))

gmpy2.get_context().precision=100
print("Test discriminant:")
assert(gmpy2.isqrt(disc)*gmpy2.isqrt(disc) == disc)

# Find two solutions
Portia = mpz((-b - gmpy2.isqrt(disc)) // (2*a))
Quincy = mpz((-b + gmpy2.isqrt(disc)) // (2*a))
P = Portia
Q = Quincy

print("Test N = P*Q:")
assert(Nathan==(Portia*Quincy))

print("Test Phi = (P-1)*(Q-1):")
assert(Philip==((Portia-1)*(Quincy-1)))

Edgard = int(str(Portia)[0:32])+int(str(Quincy)[0:32])
while not gmpy2.is_prime(Edgard):
    Edgard += 1


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

d = modinv(Edgard, Philip)
print("Test private key d:")
assert((d*Edgard) % Philip == 1)

# Decryption
plain=gmpy2.powmod(C,d,N)

print("Test encrypt plaintext = cryptext:")
assert(gmpy2.powmod(plain, Edgard, N) == C)

def convert_decimal_num_to_ascii_str(decimal_number):
    # Slice string to remove leading `0x`
    hex_string = hex(decimal_number)[2:]

    # Convert to bytes object
    bytes_object = bytes.fromhex(hex_string)

    # Convert to ASCII string
    ascii_string = bytes_object.decode("ASCII")
    return ascii_string 

print(convert_decimal_num_to_ascii_str(plain))
