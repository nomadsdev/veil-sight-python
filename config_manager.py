import configparser

def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config