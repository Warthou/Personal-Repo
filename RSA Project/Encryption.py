# Encryption Module
# Input from public_key.txt and message.txt
# Output to ciphertext.txt
def encrypt():
    # Get inputs from public_key.txt
    with open("public_key.txt") as f:
        modN, expo = [int(i) for i in next(f).split()]

    # Get input from message.txt
    f = open("message.txt")
    plaintext = f.readline()
    plaintext = int(plaintext)
    f.close()

    # Compute ciphertext and Output it to ciphertext.txt
    ciphertext = pow(plaintext, expo, modN)
    f = open("ciphertext.txt", "w")
    f.write('{0}'.format(ciphertext))
    f.close()

    print("Encryption Successful!")
    print("Check ciphertext.txt for the Ciphertext.\n")