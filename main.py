import win32gui as _w32g
import cv2 as _cv2
import numpy as _np
import pyautogui as _pag
import pytesseract as _pyt
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

_image_folder = config.get('Settings', 'image_folder')
_default_threshold = config.getfloat('Settings', 'default_threshold')
_default_ocr_language = config.get('Settings', 'ocr_language')
_c = config.get('Settings', 'config_file')

def _f(t):
    h = _w32g.FindWindow(None, t)
    if h:
        print(f"Found window: {t} with handle: {h}")
        return h
    else:
        print(f"No window found with title: {t}")
        return None

def _r(f):
    try:
        with open(f, 'r') as _f:
            t = _f.readline().strip()
            if not t:
                raise ValueError("Config file is empty")
        return t
    except FileNotFoundError:
        print(f"File not found: {f}")
        return None
    except ValueError as e:
        print(e)
        return None

def _f_img(p, th=_default_threshold):
    try:
        s = _np.array(_pag.screenshot())
        s = _cv2.cvtColor(s, _cv2.COLOR_RGB2BGR)
        s = _cv2.GaussianBlur(s, (5, 5), 0)
        
        t = _cv2.imread(p, _cv2.IMREAD_UNCHANGED)
        if t is None:
            raise ValueError(f"Unable to load image from path: {p}")
        
        t = _cv2.GaussianBlur(t, (5, 5), 0)
        
        scales = [1.0, 0.75, 0.5, 0.25]
        found = None
        
        for scale in scales:
            resized_t = _cv2.resize(t, None, fx=scale, fy=scale)
            r = _cv2.matchTemplate(s, resized_t, _cv2.TM_CCOEFF_NORMED)
            _, mv, _, ml = _cv2.minMaxLoc(r)
            if mv >= th:
                found = (ml, scale)
                break

        if found:
            ml, scale = found
            print(f"Found image at location: {ml} with scale: {scale}")
            return ml
        else:
            print("Image not found on screen")
            return None

    except Exception as e:
        print(f"Error in _f_img: {e}")
        return None

def _e(p, l=_default_ocr_language):
    try:
        i = _cv2.imread(p)
        if i is None:
            raise ValueError(f"Unable to load image for OCR from path: {p}")
        
        g = _cv2.cvtColor(i, _cv2.COLOR_BGR2GRAY)
        _, g = _cv2.threshold(g, 0, 255, _cv2.THRESH_BINARY + _cv2.THRESH_OTSU)
        config = "--psm 6"
        t = _pyt.image_to_string(g, lang=l, config=config)
        return t
    except Exception as e:
        print(f"Error in _e: {e}")
        return ""

def list_images(folder):
    try:
        return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    except FileNotFoundError:
        print(f"Folder not found: {folder}")
        return []

def main():
    _wt = _r(_c)
    
    if _wt:
        _h = _f(_wt)
        if _h:
            images = list_images(_image_folder)
            if not images:
                print("No images found in the folder.")
                return
            
            print("Select images to search (separate numbers with commas, or enter 0 for all):")
            for idx, img in enumerate(images):
                print(f"{idx + 1}: {img}")

            selection = input("Enter your choice: ")
            if selection == "0":
                selected_images = images
            else:
                try:
                    indices = list(map(int, selection.split(',')))
                    selected_images = [images[i - 1] for i in indices if 0 < i <= len(images)]
                    if not selected_images:
                        raise ValueError("No valid selections made.")
                except (ValueError, IndexError) as e:
                    print(f"Invalid selection: {e}")
                    return
            
            print("Select OCR Language (default is 'eng+tha'):")
            print("1: English")
            print("2: Thai")
            print("3: English + Thai")
            lang_choice = input("Enter your choice: ")
            lang_map = {"1": "eng", "2": "tha", "3": "eng+tha"}
            ocr_lang = lang_map.get(lang_choice, _default_ocr_language)
            
            for img_file in selected_images:
                img_path = os.path.join(_image_folder, img_file)
                print(f"Processing image: {img_path}")
                _il = _f_img(img_path)
                if _il:
                    _et = _e(img_path, l=ocr_lang)
                    print(f"Extracted Text from {img_file}:\n{_et}")
                    
            print("Program completed.")
        else:
            print("Failed to find window")
    else:
        print("Configuration file not found")

if __name__ == "__main__":
    while True:
        print("1: Start Program")
        print("0: Exit Program")
        choice = input("Enter your choice: ")
        if choice == "1":
            main()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 to start or 0 to exit.")
