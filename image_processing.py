import cv2 as _cv2
import pyautogui as _pag
import numpy as _np
import os
import pytesseract as _pyt
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_image_on_screen(image_path, threshold=0.8, blur_radius=5, scales=None):
    start_time = time.time()
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        screen = _np.array(_pag.screenshot())
        screen = _cv2.cvtColor(screen, _cv2.COLOR_RGB2BGR)

        if screen.shape[1] > 1920:
            screen = _cv2.resize(screen, (screen.shape[1] // 2, screen.shape[0] // 2))

        screen = _cv2.GaussianBlur(screen, (blur_radius, blur_radius), 0)

        template = _cv2.imread(image_path, _cv2.IMREAD_UNCHANGED)
        if template is None:
            raise ValueError(f"Unable to load image from path: {image_path}")
        
        template = _cv2.GaussianBlur(template, (blur_radius, blur_radius), 0)
        
        if scales is None:
            scales = [1.0, 0.75, 0.5, 0.25]

        found = None
        for scale in scales:
            resized_template = _cv2.resize(template, None, fx=scale, fy=scale)
            
            result = _cv2.matchTemplate(screen, resized_template, _cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = _cv2.minMaxLoc(result)
            
            if max_val >= threshold:
                found = (max_loc, scale)
                break

        if found:
            max_loc, scale = found
            logging.info(f"Found image at location: {max_loc} with scale: {scale}")
            logging.info(f"Time taken: {time.time() - start_time:.2f} seconds")
            return max_loc, scale
        else:
            logging.info("Image not found on screen")
            return None, None

    except FileNotFoundError as fnf_error:
        logging.error(f"File not found: {fnf_error}")
        return None, None
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
        return None, None
    except Exception as e:
        logging.error(f"Unexpected error in find_image_on_screen: {e}")
        return None, None


def extract_text_from_image(image_path, language='eng', psm=6):
    start_time = time.time()
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        image = _cv2.imread(image_path, _cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Unable to load image for OCR from path: {image_path}")
        
        gray_image = _cv2.cvtColor(image, _cv2.COLOR_BGR2GRAY)

        binary_image = _cv2.adaptiveThreshold(
            gray_image, 255, _cv2.ADAPTIVE_THRESH_GAUSSIAN_C, _cv2.THRESH_BINARY, 11, 2
        )

        config = f"--psm {psm}"  # ตั้งค่า OCR psm
        text = _pyt.image_to_string(binary_image, lang=language, config=config)
        
        if not text.strip():
            logging.info("No text extracted from the image.")
        
        logging.info(f"Time taken for OCR: {time.time() - start_time:.2f} seconds")
        return text.strip()

    except FileNotFoundError as fnf_error:
        logging.error(f"File not found: {fnf_error}")
        return ""
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
        return ""
    except Exception as e:
        logging.error(f"Unexpected error in extract_text_from_image: {e}")
        return ""


if __name__ == "__main__":
    location, scale = find_image_on_screen("test_image.png")
    
    text = extract_text_from_image("test_image.png", language="eng", psm=6)
    logging.info(f"Extracted text: {text}")
