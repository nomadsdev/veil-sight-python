import cv2 as _cv2
import pyautogui as _pag
import numpy as _np
import pytesseract as _pyt
from pathlib import Path
import logging
import functools
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

@functools.lru_cache(maxsize=128)
def read_first_line(file_path):
    path = Path(file_path)
    if not path.is_file():
        logging.error(f"File not found: {file_path}")
        return None

    try:
        with path.open('r', encoding='utf-8') as file:
            line = file.readline().strip()
            if not line:
                raise ValueError(f"File '{file_path}' is empty or only contains whitespace")
        logging.info(f"First line read: {line}")
        return line
    except ValueError as e:
        logging.error(f"Value error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error while reading file: {e}")
        return None

def list_images(folder, valid_extensions=None):
    if valid_extensions is None:
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
        else:
            logging.info(f"Found {len(images)} images in {folder}")
        
        return images
    except Exception as e:
        logging.error(f"Unexpected error while listing images: {e}")
        return []

def execution_time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@execution_time_decorator
def process_images_in_folder(folder):
    images = list_images(folder)
    processed_images = []

    if not images:
        logging.warning("No images to process.")
        return processed_images

    for image_name in images:
        image_path = Path(folder) / image_name
        image = _cv2.imread(str(image_path))

        if image is not None:
            logging.debug(f"Processing image: {image_name}")
            gray_image = _cv2.cvtColor(image, _cv2.COLOR_BGR2GRAY)
            processed_images.append(gray_image)
        else:
            logging.warning(f"Failed to load image: {image_name}")
    
    logging.info(f"Processed {len(processed_images)} images.")
    return processed_images

if __name__ == '__main__':
    file_path = 'example.txt'
    first_line = read_first_line(file_path)
    logging.info(f"First line of the file: {first_line}")
    
    folder_path = 'images'
    processed_images = process_images_in_folder(folder_path)
