# VeilSight

**VeilSight** is a robust automation tool for Windows, designed to automate tasks like window detection, image recognition, and text extraction. It's ideal for streamlining repetitive tasks and boosting productivity.

## Features

- **Window Detection**: Identify specific windows based on titles defined in a configuration file.
- **Screen Image Search**: Search for and identify specific images on your screen with multi-scale search capability for improved accuracy.
- **Text Extraction**: Extract text from images using Tesseract OCR, with support for both English and Thai languages.
- **Multiple Window Support**: Handle multiple windows by processing each title specified in the configuration file.
- **Configurable Settings**: All essential settings, including window titles, image folder paths, and OCR language preferences, are stored in a `config.ini` file for easy customization.
- **Enhanced Error Handling**: Comprehensive error handling for file loading, image processing, and configuration issues.
- **User-Friendly Interaction**: Users can select specific images to search or choose all available images in the `image/` folder.
- **Detailed Logging**: Logs actions and errors to facilitate debugging and tracking.

## Installation

1. **Install Required Libraries**:

   ```bash
   pip install pywin32 opencv-python numpy pyautogui pytesseract
   ```

2. **Install Tesseract OCR**:

   - Download and install Tesseract OCR from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).
   - Ensure Tesseract’s installation path is added to your `PATH` environment variable.

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
   - Store the images to be searched for in the folder specified in the `config.ini` file (default is `image/`).

## Usage

1. **Run the Script**:
   - Execute the script using Python:

   ```bash
   python main.py
   ```

2. **Image Selection**:
   - The script will prompt you to select images for the search. Choose specific images by entering their corresponding numbers or select all images by entering `0`.

3. **Select OCR Language**:
   - The script allows you to choose the OCR language before processing images, based on the settings in `config.ini`.

## Project Structure

- **`main.py`**: The primary script that handles window detection, image searching, and text extraction.
- **`config.ini`**: Configuration file where window titles, image folder paths, and OCR settings are defined.
- **`image/`**: Folder containing images to be used in the screen search.

## Detailed Functions

- **Window Detection**: `_f(t)` locates a window based on the title provided.
- **Configuration File Reading**: `_r(f)` reads window titles and other settings from the `config.ini` file.
- **Image Search and Processing**: `_f_img(p, th)` searches for the image on the screen with multi-scale support, applying Gaussian blur for better accuracy.
- **Text Extraction**: `_e(p, l)` extracts and processes text from images using OCR.
- **User Interaction and Execution**: The `main()` function orchestrates the overall process, including user input, image processing, and language selection.
- **Logging**: `_log_update(message)` logs detailed updates about the script's activities and errors.

## Development

To further develop or modify this project:

- **Window Interaction**: Adjust `_f(t)` for more complex window searches or handle multiple windows.
- **Image Search Logic**: Enhance `_f_img(p, th)` for different image matching techniques or thresholds.
- **Text Extraction Settings**: Modify `_e(p, l)` to fine-tune OCR configurations or support additional languages.
- **Configuration Management**: Expand or customize `config.ini` to include more settings or parameters.

## Support

For any issues, suggestions, or contributions, please reach out through GitHub Issues or contact the developer directly via email.

## License

This project is licensed under the [MIT License](LICENSE).