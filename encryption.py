# This program encrypts and decrypts a message using a simple substitution cipher.
# The program generates a random key for encryption and decryption.
# The program takes a message from the user and encrypts it using the key.

import random
import string

chars=" "+string.punctuation+string.digits+ string.ascii_letters
chars=list(chars)
keys=chars.copy()
random.shuffle(chars)
#ENCRYPTION MSG
plain_msg=input("Enter the message to be encrypted: ")
encrupted_msg=""
for letterr in plain_msg:
    index=chars.index(letterr)
    encrupted_msg+=keys[index]
print(f"original message: {plain_msg}")
print(f"encrypted message: {encrupted_msg}")
#DECYPTION MSG
encrupted_msg=input("Enter the message to be decrypt: ")
plain_msg=""
for letterr in encrupted_msg:
    index=keys.index(letterr)
    plain_msg+=chars[index]

print(f"encrypted message: {encrupted_msg}")
print(f"original message: {plain_msg}")