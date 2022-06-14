import datetime
import random
import string
import os
#import configparser
from crypt import AESCipher

from model.model import Migration, Crud


#config_ini = configparser.ConfigParser()
#config_ini.read('config/config.ini')
#config = config_ini['database']
#db_file_path = config.get('file_path')

key = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(32)])  # -> '4yKxQ5hMcUJixcG4Z8Lc5ZPBr5McS65X'

def get_temper():
    temp_value = random.uniform(10, 30)
    return temp_value

def encrypt_temper(temp_value: str):
    cipher = AESCipher(key)
    encrypted = cipher.encrypt(temp_value)
    return encrypted 

def decrypt_temper(encrypted: str):
    cipher = AESCipher(key)
    decrypted = cipher.decrypt(encrypted)
    return decrypted

if __name__ == '__main__':

    now = datetime.datetime.now()

    temp_value = get_temper()
    temp_str = str(temp_value)

    encrypted = encrypt_temper(temp_str)
    decrypted = decrypt_temper(encrypted)

    mg = Migration()
    dbcon = Crud()

    mg.temp_create_db()

    #print(temp_value)
    #print(temp_str)
    #print(encrypted)
    #print(decrypted)

    dbcon.write_db(now, now, encrypted)

    dbcon.select_db()
    
