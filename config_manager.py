import configparser

def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        if not config.sections():
            raise ValueError(f"No sections found in '{file_path}'")
    except FileNotFoundError:
        print(f"Error: Configuration file not found: {file_path}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while reading config: {e}")
        return None
    
    return config
