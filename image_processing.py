import cv2 as _cv2
import pyautogui as _pag
import numpy as _np
import pytesseract as _pyt

def find_image_on_screen(image_path, threshold=0.8):
    try:
        screen = _np.array(_pag.screenshot())
        screen = _cv2.cvtColor(screen, _cv2.COLOR_RGB2BGR)
        screen = _cv2.GaussianBlur(screen, (5, 5), 0)
        
        template = _cv2.imread(image_path, _cv2.IMREAD_UNCHANGED)
        if template is None:
            raise ValueError(f"Unable to load image from path: {image_path}")
        
        template = _cv2.GaussianBlur(template, (5, 5), 0)
        
        scales = [1.0, 0.75, 0.5, 0.25]
        found = None
        
        for scale in scales:
            resized_template = _cv2.resize(template, None, fx=scale, fy=scale)
            result = _cv2.matchTemplate(screen, resized_template, _cv2.TM_CCOEFF_NORMED)
            _, max_val, _, min_loc = _cv2.minMaxLoc(result)
            if max_val >= threshold:
                found = (min_loc, scale)
                break

        if found:
            min_loc, scale = found
            print(f"Found image at location: {min_loc} with scale: {scale}")
            return min_loc
        else:
            print("Image not found on screen")
            return None

    except Exception as e:
        print(f"Error in find_image_on_screen: {e}")
        return None

def extract_text_from_image(image_path, language='eng'):
    try:
        image = _cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Unable to load image for OCR from path: {image_path}")
        
        gray_image = _cv2.cvtColor(image, _cv2.COLOR_BGR2GRAY)
        _, binary_image = _cv2.threshold(gray_image, 0, 255, _cv2.THRESH_BINARY + _cv2.THRESH_OTSU)
        config = "--psm 6"
        text = _pyt.image_to_string(binary_image, lang=language, config=config)
        return text
    except Exception as e:
        print(f"Error in extract_text_from_image: {e}")
        return ""