from pathlib import Path
import configparser
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    path = Path(file_path)
    
    if not path.is_file():
        logging.error(f"Configuration file not found: {file_path}")
        return None

    try:
        config.read(path)
        
        if not config.sections():
            raise ValueError(f"No sections found in '{file_path}'")
        
        required_sections = ['Settings']
        required_keys = {
            'Settings': ['image_folder', 'default_threshold', 'ocr_language', 'config_file']
        }
        
        for section in required_sections:
            if section not in config:
                raise ValueError(f"Missing section: '{section}' in '{file_path}'")
            
            for key in required_keys[section]:
                if key not in config[section]:
                    raise ValueError(f"Missing key: '{key}' in section: '{section}' in '{file_path}'")
        
        image_folder = config.get('Settings', 'image_folder').strip()
        if not Path(image_folder).is_dir():
            raise ValueError(f"Invalid image folder path: {image_folder}")
        
        try:
            default_threshold = float(config.get('Settings', 'default_threshold').strip())
            if not (0 <= default_threshold <= 1):
                raise ValueError(f"Threshold must be between 0 and 1: {default_threshold}")
        except ValueError:
            raise ValueError(f"Invalid value for default_threshold in '{file_path}'")
        
        ocr_language = config.get('Settings', 'ocr_language').strip()
        if not ocr_language:
            raise ValueError(f"OCR language cannot be empty in '{file_path}'")
        
        config_file = config.get('Settings', 'config_file').strip()
        if not Path(config_file).is_file():
            raise ValueError(f"Config file path is invalid: {config_file}")

    except ValueError as e:
        logging.error(f"Configuration error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error while reading config: {e}")
        return None
    
    logging.info(f"Configuration loaded successfully from '{file_path}'")
    return config
