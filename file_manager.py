import cv2 as _cv2
import pyautogui as _pag
import numpy as _np
import pytesseract as _pyt
from pathlib import Path

def read_first_line(file_path):
    try:
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open('r') as file:
            line = file.readline().strip()
            if not line:
                raise ValueError(f"File '{file_path}' is empty or only contains whitespace")
        return line
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def list_images(folder):
    valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff'}
    try:
        path = Path(folder)
        if not path.is_dir():
            raise FileNotFoundError(f"Folder not found: {folder}")
        
        images = [f.name for f in path.iterdir() 
                  if f.is_file() and f.suffix.lower() in valid_extensions]
        
        if not images:
            print(f"No valid image files found in the folder: {folder}")
        
        return images
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
