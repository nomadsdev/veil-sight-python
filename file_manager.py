import cv2 as _cv2
import pyautogui as _pag
import numpy as _np
import pytesseract as _pyt
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_first_line(file_path):
    path = Path(file_path)
    if not path.is_file():
        logging.error(f"File not found: {file_path}")
        return None

    try:
        with path.open('r') as file:
            line = file.readline().strip()
            if not line:
                raise ValueError(f"File '{file_path}' is empty or only contains whitespace")
        return line
    except ValueError as e:
        logging.error(f"Value error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None

def list_images(folder):
    valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff'}
    path = Path(folder)
    
    if not path.is_dir():
        logging.error(f"Folder not found: {folder}")
        return []

    try:
        images = [f.name for f in path.iterdir() 
                  if f.is_file() and f.suffix.lower() in valid_extensions]
        
        if not images:
            logging.info(f"No valid image files found in the folder: {folder}")
        
        return images
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return []
