import threading
import os
from config_manager import load_config
from window_manager import find_window
from file_manager import read_first_line, list_images
from image_processing import find_image_on_screen, extract_text_from_image
from result_saver import save_results

def process_image(img_file, folder, ocr_lang):
    img_path = os.path.join(folder, img_file)
    print(f"Processing image: {img_path}")
    location = find_image_on_screen(img_path)
    if location:
        text = extract_text_from_image(img_path, language=ocr_lang)
        print(f"Extracted Text from {img_file}:\n{text}")
        return (img_file, str(location), text)
    return None

def main():
    config = load_config()
    image_folder = config.get('Settings', 'image_folder')
    default_threshold = config.getfloat('Settings', 'default_threshold')
    default_ocr_language = config.get('Settings', 'ocr_language')
    config_file = config.get('Settings', 'config_file')
    
    window_title = read_first_line(config_file)
    
    if window_title:
        window_handle = find_window(window_title)
        if window_handle:
            images = list_images(image_folder)
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
            ocr_lang = lang_map.get(lang_choice, default_ocr_language)
            
            results = []
            threads = []
            for img_file in selected_images:
                thread = threading.Thread(target=lambda: results.append(process_image(img_file, image_folder, ocr_lang)))
                thread.start()
                threads.append(thread)
            
            for thread in threads:
                thread.join()
            
            save_results(results)
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