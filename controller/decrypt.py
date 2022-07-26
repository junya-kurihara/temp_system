import sys
import AES256


args = sys.argv

path = args[1]
key = args[2]

with open(path, 'r') as f:
    encrypted = f.read()
    decrypted = AES256.b64decrypt(key, encrypted)
    print(decrypted)




