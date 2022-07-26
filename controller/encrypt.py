import sys
import AES256

args = sys.argv

key = args[1]
raw = args[2]

encrypted = AES256.b64encrypt(key, raw)
print(encrypted)

