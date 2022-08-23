import AES256
import os
from model import model
from view import view


def encrypt_temper(exec_date, temper, key):
    plain_str = exec_date + ' ' + temper
    encrypted = AES256.b64encrypt(key, plain_str)
    return encrypted


def main():
    m = model.Model()
    temper = m.get_temperature()
    exec_date = m.get_exec_datetime()

    encrypted = encrypt_temper(exec_date, temper, '12345')

    output_file = '/home/kurihara/work/202205_temp_sys/temp_sys/data/data.dat'
    db_path = os.getcwd() + sep + 'db' + sep + 'temp_test.db'
    view.save_encrypted_file(encrypted, output_file)

    m.init_db()
    m.temp_create_db()
    m.insert_temper_db(exec_date, exec_date, temper)
    m.select_db()


if __name__ == '__main__':
    main()
