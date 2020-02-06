# Decryption Module
# Input from public_key.txt, private_key.txt and ciphertext.txt
# Output to decrypted_message.txt
def decrypt():
    # Get inputs from public_key.txt
    with open("public_key.txt") as f:
        modN, expo = [int(i) for i in next(f).split()] # I suppose I don't need to be pulling expo here

    # Get input from private_key.txt
    f = open("private_key.txt")
    privKey = f.readline()
    privKey = int(privKey)
    f.close()

    # Get input from ciphertext.txt
    f = open("ciphertext.txt")
    encrypted = f.readline()
    encrypted = int(encrypted)
    f.close()

    # Compute decrypted message and Output it into decrypted_message.txt
    message = pow(encrypted, privKey, modN)
    f = open("decrypted_message.txt", "w")
    f.write('{0}'.format(message))
    f.close()

    print("Decryption Successful!")
    print("Check decrypted_message.txt for the Original Message.")