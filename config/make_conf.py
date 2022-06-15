import os
import configparser


config = configparser.ConfigParser()
config['database'] = {
    'file_name': 'temper.db'
}
config['data'] = {
    'file_name': 'tms3.dat'
}
config['key'] = {
    'key': 'test'
}


file_name = os.path.join(os.getcwd(), 'config.ini')
with open(file_name, 'w') as config_file:
    config.write(config_file)
