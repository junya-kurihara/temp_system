import datetime
import random
import os
import configparser

import AES256
from model.model import BaseEngine


def get_temper():
    # test function
    temp = random.uniform(10, 30)
    return f'{temp:.2f}'

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

    # data config
    data_dir = script_dir + '/data/'
    data_file_name = config_ini['data'].get('file_name')
    data_file = data_dir + data_file_name

    # key string
    key = config_ini['key'].get('key')

    # get temp value
    temp_value = get_temper()

    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')

    row = now + ' ' + temp_value

    # encrypt and decrypt
    encrypted = AES256.b64encrypt(key, row)
    decrypted = AES256.b64decrypt(key, encrypted)

    with open(data_file, 'w') as f:
        f.write(encrypted)

    db = BaseEngine(db_file)
    db.temp_create_db()
    db.write_db(now, now, temp_value)
    db.select_db()

    print(row)
    print(decrypted)


if __name__ == '__main__':
    main()

