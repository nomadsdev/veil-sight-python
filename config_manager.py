from pathlib import Path
import configparser
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_path(path, check_type='file'):
    p = Path(path)
    if check_type == 'file':
        if not p.is_file():
            raise FileNotFoundError(f"Invalid file path: {path}")
    elif check_type == 'dir':
        if not p.is_dir():
            raise NotADirectoryError(f"Invalid directory path: {path}")
    return p

def validate_threshold(threshold_str):
    try:
        threshold = float(threshold_str.strip())
        if not (0 <= threshold <= 1):
            raise ValueError(f"Threshold must be between 0 and 1: {threshold}")
        return threshold
    except ValueError:
        raise ValueError(f"Invalid threshold value: {threshold_str}")

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

        image_folder = validate_path(config.get('Settings', 'image_folder').strip(), check_type='dir')
        logging.info(f"Image folder path: {image_folder}")

        default_threshold = validate_threshold(config.get('Settings', 'default_threshold').strip())
        logging.info(f"Default threshold: {default_threshold}")

        ocr_language = config.get('Settings', 'ocr_language').strip()
        if not ocr_language:
            raise ValueError(f"OCR language cannot be empty in '{file_path}'")
        logging.info(f"OCR language: {ocr_language}")

        config_file = validate_path(config.get('Settings', 'config_file').strip(), check_type='file')
        logging.info(f"Config file: {config_file}")

    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        logging.error(f"Configuration error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error while reading config: {e}")
        return None
    
    logging.info(f"Configuration loaded successfully from '{file_path}'")
    return config

if __name__ == '__main__':
    config = load_config()
    if config:
        logging.info("Config successfully loaded and ready for use.")
    else:
        logging.error("Failed to load config.")
