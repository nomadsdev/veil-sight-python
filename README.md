# VeilSight

**VeilSight** is a robust automation tool for Windows designed to streamline repetitive tasks through automation. It supports window detection, image recognition, and text extraction, making it ideal for boosting productivity.

## Features

- **Window Detection**: Identify specific windows based on titles defined in the configuration file.
- **Screen Image Search**: Search for and identify specific images on your screen with multi-scale search capability for improved accuracy.
- **Text Extraction**: Extract text from images using Tesseract OCR, supporting both English and Thai languages.
- **Multiple Window Support**: Process multiple windows based on titles specified in the configuration file.
- **Configurable Settings**: Customize settings like window titles, image folder paths, and OCR language preferences in the `config.ini` file.
- **Enhanced Error Handling**: Includes error handling for file loading, image processing, and configuration issues.
- **User-Friendly Interaction**: Allows users to select specific images to search or choose all images in the `image/` folder.
- **Detailed Logging**: Logs actions and errors for debugging and tracking purposes.

## Installation

1. **Install Required Libraries**:

   ```bash
   pip install pywin32 opencv-python numpy pyautogui pytesseract
   ```

2. **Install Tesseract OCR**:

   - Download and install Tesseract OCR from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).
   - Ensure that Tesseract’s installation path is added to your `PATH` environment variable.

## Configuration

1. **Prepare Configuration File**:
   - Edit the `config.ini` file to specify window titles, image folder paths, default OCR language, and other settings.
   
   Example `config.ini`:
   ```ini
   [Window]
   title = Your Window Title

   [Image]
   folder = image/

   [OCR]
   language = eng+tha
   ```

2. **Place Images**:
   - Store the images you want to search for in the folder specified in the `config.ini` file (default is `image/`).

## Usage

1. **Run the Script**:
   - Execute the script using Python:

   ```bash
   python main.py
   ```

2. **Image Selection**:
   - The script will prompt you to select images for the search. Choose specific images by entering their corresponding numbers or select all images by entering `0`.

3. **Select OCR Language**:
   - Choose the OCR language before processing images, based on the settings in `config.ini`.

## Project Structure

- **`main.py`**: The primary script that orchestrates window detection, image searching, and text extraction.
- **`config.ini`**: Configuration file where window titles, image folder paths, and OCR settings are defined.
- **`image/`**: Folder containing images to be used in the screen search.

## Detailed Functions

- **Window Detection**: `find_window(title)` locates a window based on the title provided.
- **Configuration File Reading**: `load_config(file_path)` reads window titles and other settings from the `config.ini` file.
- **Image Search and Processing**: `find_image_on_screen(image_path, threshold)` searches for an image on the screen with multi-scale support and Gaussian blur for accuracy.
- **Text Extraction**: `extract_text_from_image(image_path, language)` extracts and processes text from images using OCR.
- **User Interaction and Execution**: The `main()` function manages user input, image processing, and language selection.
- **Logging**: `save_results(results)` logs detailed updates about the script's activities and errors.

## Development

To further develop or modify this project:

- **Window Interaction**: Adjust `find_window(title)` for more complex window searches or handle multiple windows.
- **Image Search Logic**: Enhance `find_image_on_screen(image_path, threshold)` for different image matching techniques or thresholds.
- **Text Extraction Settings**: Modify `extract_text_from_image(image_path, language)` to fine-tune OCR configurations or support additional languages.
- **Configuration Management**: Expand or customize `config.ini` to include more settings or parameters.

## Support

For issues, suggestions, or contributions, please use GitHub Issues or contact the developer directly via email.

## License

This project is licensed under the MIT License (LICENSE).
