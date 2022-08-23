import os


def save_encrypted_file(encrypted, save_path):
    with open(save_path, 'w') as f:
        f.write(encrypted)


class View(object):
    pass


if __name__ == '__main__':
    sep_str = os.sep
    current_path = os.getcwd()
    file_name = 'test.csv'
    file_fullpath = current_path + sep_str + file_name

    print(file_fullpath)

    save_encrypted_file('123456', file_fullpath)
