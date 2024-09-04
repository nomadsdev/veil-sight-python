import threading
import os
import logging
from concurrent.futures import ThreadPoolExecutor
from config_manager import load_config
from window_manager import find_window
from file_manager import read_first_line, list_images
from image_processing import find_image_on_screen, extract_text_from_image
from result_saver import save_results

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_image(img_file, folder, ocr_lang):
    img_path = os.path.join(folder, img_file)
    logging.info(f"Processing image: {img_path}")
    try:
        location = find_image_on_screen(img_path)
        if location:
            text = extract_text_from_image(img_path, language=ocr_lang)
            logging.info(f"Extracted Text from {img_file}:\n{text}")
            return (img_file, str(location), text)
        else:
            logging.warning(f"Image not found on screen: {img_file}")
    except Exception as e:
        logging.error(f"Error processing image {img_file}: {e}")
    return None

def select_images(images):
    print("Select images to search (separate numbers with commas, or enter 0 for all):")
    for idx, img in enumerate(images):
        print(f"{idx + 1}: {img}")

    selection = input("Enter your choice: ")
    if selection == "0":
        return images
    try:
        indices = list(map(int, selection.split(',')))
        selected_images = [images[i - 1] for i in indices if 0 < i <= len(images)]
        if not selected_images:
            raise ValueError("No valid selections made.")
        return selected_images
    except (ValueError, IndexError) as e:
        logging.error(f"Invalid selection: {e}")
        return []

def select_ocr_language(default_lang):
    print("Select OCR Language (default is 'eng+tha'):")
    print("1: English")
    print("2: Thai")
    print("3: English + Thai")
    lang_choice = input("Enter your choice: ")
    lang_map = {"1": "eng", "2": "tha", "3": "eng+tha"}
    return lang_map.get(lang_choice, default_lang)

def main():
    try:
        config = load_config()
        if config is None:
            logging.error("Failed to load configuration.")
            return
        
        image_folder = config.get('Settings', 'image_folder')
        default_ocr_language = config.get('Settings', 'ocr_language')
        config_file = config.get('Settings', 'config_file')
        
        window_title = read_first_line(config_file)
        if not window_title:
            logging.error("No window title found in config file.")
            return
        
        window_handle = find_window(window_title)
        if not window_handle:
            logging.error(f"Failed to find window with title: {window_title}")
            return

        images = list_images(image_folder)
        if not images:
            logging.error("No images found in the folder.")
            return
        
        selected_images = select_images(images)
        if not selected_images:
            return
        
        ocr_lang = select_ocr_language(default_ocr_language)

        results = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(process_image, img_file, image_folder, ocr_lang) for img_file in selected_images]
            for future in futures:
                result = future.result()
                if result:
                    results.append(result)

        save_results(results)
        logging.info("Program completed successfully.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        print("1: Start Program")
        print("0: Exit Program")
        choice = input("Enter your choice: ")
        if choice == "1":
            main()
        elif choice == "0":
            logging.info("Exiting program.")
            break
        else:
            logging.warning("Invalid choice. Please enter 1 to start or 0 to exit.")
