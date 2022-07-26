import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Padding


def create_aes(password: str, iv):
    # hash_pass = (hashlib.md5(password.encode('utf-8')).hexdigest()).encode('utf-8')
    hash_pass = (hashlib.sha256(password.encode('utf-8')).digest())
    return AES.new(hash_pass, AES.MODE_CBC, iv)


def b64encrypt(key: str, raw: str):
    iv = Random.get_random_bytes(AES.block_size)
    cipher = create_aes(key, iv)
    data = Padding.pad(raw.encode('utf-8'), AES.block_size, 'pkcs7')
    return base64.b64encode(iv + cipher.encrypt(data)).decode('utf-8')


def b64decrypt(key: str, b64encrypted: str):
    enc = base64.b64decode(b64encrypted)
    iv = enc[:AES.block_size]
    cipher = create_aes(key, iv)
    data = Padding.unpad(cipher.decrypt(enc[AES.block_size:]), AES.block_size, 'pkcs7')
    return data.decode('utf-8')


if __name__ == '__main__':

    key = 'test'
    row = 'abcdefg'
    enc = b64encrypt(key, row)
    print(enc)

    dec = b64decrypt(key, enc)
    print(dec)
