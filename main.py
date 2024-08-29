import win32gui as _w32g
import cv2 as _cv2
import numpy as _np
import pyautogui as _pag
import pytesseract as _pyt
import os

_c = "bin/title.config"
_image_folder = "image/"
_default_threshold = 0.8

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
    s = _np.array(_pag.screenshot())
    s = _cv2.cvtColor(s, _cv2.COLOR_RGB2BGR)
    s = _cv2.GaussianBlur(s, (5, 5), 0)
    
    t = _cv2.imread(p, _cv2.IMREAD_UNCHANGED)
    if t is None:
        print(f"Error: Unable to load image from path: {p}")
        return None
    
    t = _cv2.GaussianBlur(t, (5, 5), 0)
    r = _cv2.matchTemplate(s, t, _cv2.TM_CCOEFF_NORMED)
    _, mv, _, ml = _cv2.minMaxLoc(r)
    if mv >= th:
        print(f"Found image at location: {ml}")
        return ml
    else:
        print("Image not found on screen")
        return None

def _e(p, l="eng+tha"):
    i = _cv2.imread(p)
    g = _cv2.cvtColor(i, _cv2.COLOR_BGR2GRAY)
    _, g = _cv2.threshold(g, 0, 255, _cv2.THRESH_BINARY + _cv2.THRESH_OTSU)
    config = "--psm 6"
    t = _pyt.image_to_string(g, lang=l, config=config)
    return t

def list_images(folder):
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def main():
    _wt = _r(_c)
    
    if _wt:
        _h = _f(_wt)
        if _h:
            images = list_images(_image_folder)
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
                except (ValueError, IndexError):
                    print("Invalid selection")
                    return
            
            for img_file in selected_images:
                img_path = os.path.join(_image_folder, img_file)
                print(f"Processing image: {img_path}")
                _il = _f_img(img_path)
                if _il:
                    _et = _e(img_path)
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