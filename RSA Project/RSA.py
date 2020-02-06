import random
import math
import sys
import Encryption
import Decryption

# RSA Encryption and Decryption

# Key Setup
# Input N/A
# Output to public_key.txt and private_key.txt

# Generating Large Integer between 2^1024 and 2^2048
def generateInt():
    # Generate p such that 2^1024 <= p < 2^2048
    p = random.randint(2**1024,2**2048)
    # Generate a such that 1 <= a < p and difference between the two is at least 10^95
    a = random.randint((2**1024) - 1, p - 1)
    test = (a , p)
    return test

# Fermat Primality Test correct 99% of time
def Fermat(test):
    a = test[0]
    p = test[1]
    # if gcd(intLessThan, testPrime) == 1, move to next step
    if(math.gcd(a, p) == 1):
        # if intLessThan^(testPrime-1) mod testPrime == 1 then prime
        # inputs to pow are (base, exponent, modulus)
        if(pow(a, p - 1, p) == 1):
            return p
    # default to composite
    return 0

# Extended Euclid Algorithm
def xgcd(a, b):
    # return (g, x, y) such that a*x + b*y = g = gcd(a, b)
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a # // is integer division
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

# Computes the multiplicative inverse
def extendGCD(a, b):
    # return x such that (x * a) % b == 1
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b

# Generate Public Keys and Private Key
print("-------------------")
print("        RSA        ")
print(" By: Cameron Lydon ")
print("-------------------\n")
print("Generating public keys...")

# Generate a prime p
p = 0
while p == 0:
    x = generateInt()
    p = Fermat(x)

# Generate a prime q
q = 0
while q == 0:
    y = generateInt()
    q = Fermat(y)

# Compute public keys n and e, and phi(n) - phiN
n = p * q
phiN = (p - 1)*(q - 1)
e = 2**16 + 1

while math.gcd(e, phiN) != 1:
    e = e + 1

# Compute private key, d
d = extendGCD(e, phiN)

# Save the public keys
f = open("public_key.txt", "w")
f.write('{0} {1}'.format(n, e))
f.close()

# Save the private key
f = open("private_key.txt", "w")
f.write('{0}'.format(d))
f.close()

print("Success!")
print("Check public_key.txt for the Public Keys and private_key.txt for the Private Key.\n")


# Encryption Module
# Input from public_key.txt and message.txt
# Output to ciphertext.txt
Encryption.encrypt()


# Decryption Module
# Input from private_key.txt and ciphertext.txt
# Output to decrypted_message.txt
Decryption.decrypt()