import cv2 as _cv2
import pyautogui as _pag
import numpy as _np
import pytesseract as _pyt

def read_first_line(file_path):
    try:
        with open(file_path, 'r') as file:
            line = file.readline().strip()
            if not line:
                raise ValueError(f"File '{file_path}' is empty or only contains whitespace")
        return line
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def list_images(folder):
    import os
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    try:
        if not os.path.exists(folder):
            raise FileNotFoundError(f"Folder not found: {folder}")
        
        images = [f for f in os.listdir(folder) 
                  if os.path.isfile(os.path.join(folder, f)) 
                  and f.lower().endswith(valid_extensions)]
        
        if not images:
            print(f"No valid image files found in the folder: {folder}")
        
        return images
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
