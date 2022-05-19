import os
import configparser


config = configparser.ConfigParser()
config['database'] = {
        'file_path': os.path.join('db','temper.db')   
}

file_name = os.path.join('config', 'config.ini')
with open(file_name,'w') as config_file:
    config.write(config_file)
