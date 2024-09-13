import cv2 as _cv2
import pyautogui as _pag
import numpy as _np
import os
import pytesseract as _pyt
import logging
import time
from concurrent.futures import ThreadPoolExecutor
from skimage.transform import resize

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_image_on_screen(image_path, threshold=0.8, blur_radius=5, scales=None):
    start_time = time.time()
    
    if not os.path.isfile(image_path):
        logging.error(f"Image file not found: {image_path}")
        return None

    try:
        screen = _cv2.cvtColor(_np.array(_pag.screenshot()), _cv2.COLOR_RGB2BGR)

        if screen.shape[1] > 1920:
            screen = _cv2.resize(screen, (screen.shape[1] // 2, screen.shape[0] // 2))

        screen = _cv2.GaussianBlur(screen, (blur_radius, blur_radius), 0)

        template = _cv2.imread(image_path, _cv2.IMREAD_UNCHANGED)
        if template is None:
            raise ValueError(f"Unable to load image from path: {image_path}")
        
        template = _cv2.GaussianBlur(template, (blur_radius, blur_radius), 0)
        
        if scales is None:
            scales = [1.0, 0.75, 0.5, 0.25]

        found = find_image_parallel(screen, template, scales, threshold)

        if found:
            max_loc, scale = found
            logging.info(f"Found image at location: {max_loc} with scale: {scale}")
        else:
            logging.info("Image not found on screen")

        logging.info(f"Time taken: {time.time() - start_time:.2f} seconds")
        return found

    except ValueError as ve:
        logging.error(f"Value error: {ve}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error in find_image_on_screen: {e}")
        return None

def extract_text_from_image(image_path, language='eng', psm=6):
    start_time = time.time()
    
    if not os.path.isfile(image_path):
        logging.error(f"Image file not found: {image_path}")
        return ""

    try:
        image = _cv2.imread(image_path, _cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Unable to load image for OCR from path: {image_path}")

        gray_image = _cv2.cvtColor(image, _cv2.COLOR_BGR2GRAY)
        binary_image = _cv2.adaptiveThreshold(
            gray_image, 255, _cv2.ADAPTIVE_THRESH_GAUSSIAN_C, _cv2.THRESH_BINARY, 11, 2
        )

        config = f"--psm {psm}"
        text = _pyt.image_to_string(binary_image, lang=language, config=config)

        if not text.strip():
            logging.info("No text extracted from the image.")
        
        logging.info(f"Time taken for OCR: {time.time() - start_time:.2f} seconds")
        return text.strip()

    except ValueError as ve:
        logging.error(f"Value error: {ve}")
        return ""
    except Exception as e:
        logging.error(f"Unexpected error in extract_text_from_image: {e}")
        return ""

def find_image_parallel(screen, template, scales, threshold=0.8):
    try:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(match_template_at_scale, screen, template, scale, threshold) for scale in scales]
            for future in futures:
                result = future.result()
                if result:
                    return result
    except Exception as e:
        logging.error(f"Error during parallel image search: {e}")
    return None

def match_template_at_scale(screen, template, scale, threshold):
    try:
        resized_template = resize(template, (int(template.shape[0] * scale), int(template.shape[1] * scale)), anti_aliasing=True)
        resized_template = _np.array(resized_template * 255, dtype=_np.uint8)  # Convert back to uint8
        result = _cv2.matchTemplate(screen, resized_template, _cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = _cv2.minMaxLoc(result)
        if max_val >= threshold:
            return max_loc, scale
    except Exception as e:
        logging.error(f"Error during matching template at scale {scale}: {e}")
    return None

if __name__ == "__main__":
    location, scale = find_image_on_screen("test_image.png")
    if location:
        logging.info(f"Image found at: {location}, scale: {scale}")
    else:
        logging.info("Image not found.")
    
    text = extract_text_from_image("test_image.png", language="eng", psm=6)
    logging.info(f"Extracted text: {text}")
