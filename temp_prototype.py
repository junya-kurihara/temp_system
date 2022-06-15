import datetime
import random
import os
import configparser

import AES256
from model.model import BaseEngine


def get_temper():
    # test function
    return random.uniform(10, 30)

def main():
    script_dir = os.getcwd()

    # config read
    config_ini = configparser.ConfigParser()
    config_dir = script_dir + '/config/'
    config_ini.read(config_dir + 'config.ini')

    # db config
    db_dir = script_dir + '/db/'
    db_file_name = config_ini['database'].get('file_name')
    db_file = db_dir + db_file_name

    # key string
    key = config_ini['key'].get('key')

    # get temp value
    temp_value = get_temper()
    temp_str = str(temp_value)

    # encrypt and decrypt
    encrypted = AES256.b64encrypt(key, temp_str)
    decrypted = AES256.b64decrypt(key, encrypted)

    print(temp_value)
    print(temp_str)
    print(encrypted)
    print(decrypted)

    now = datetime.datetime.now()

    db = BaseEngine(db_file)
    db.temp_create_db()
    db.write_db(now, now, temp_value)
    db.select_db()


if __name__ == '__main__':
    main()

