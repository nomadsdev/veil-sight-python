from pathlib import Path
import configparser

def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    path = Path(file_path)

    try:
        if not path.is_file():
            raise FileNotFoundError(f"Configuration file not found: {file_path}")
        
        config.read(path)
        
        if not config.sections():
            raise ValueError(f"No sections found in '{file_path}'")
        
        required_sections = ['Settings']
        required_keys = {
            'Settings': ['image_folder', 'default_threshold', 'ocr_language', 'config_file']
        }
        
        for section in required_sections:
            if section not in config:
                raise ValueError(f"Missing section: {section} in '{file_path}'")
            
            for key in required_keys[section]:
                if key not in config[section]:
                    raise ValueError(f"Missing key: {key} in section: {section} in '{file_path}'")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while reading config: {e}")
        return None
    
    return config
