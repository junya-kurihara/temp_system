import AES256
from model import model


def encrypt_temper(exec_date, temper, key):
    plain_str = exec_date + ' ' + temper
    encrypted = AES256.b64encrypt(key, plain_str)
    return encrypted


#def main():
#    temper = model.model.get_temperature()
#    exec_date = model.model.get_exec_datetime()


if __name__ == '__main__':
    temper = model.Model().get_temperature()
    exec_date = model.Model().get_exec_datetime()
    encrypted = encrypt_temper(exec_date, temper, '12345')
    print(encrypted)

