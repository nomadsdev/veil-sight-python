
# VeilSight

**VeilSight** is a powerful automation tool designed to interact with the Windows operating system seamlessly. It provides functionalities such as window detection, image recognition, and text extraction, making it an essential utility for automating repetitive tasks and enhancing productivity.

## Features

- **Window Detection**: Locate specific windows by their title, as defined in a configuration file.
- **Screen Image Search**: Search for and identify specific images on your screen, with adjustable thresholds for accuracy.
- **Text Extraction**: Extract text from identified images using Tesseract OCR, with support for English and Thai languages.
- **Enhanced Error Handling**: Includes comprehensive error handling for file loading and image processing.
- **User-Friendly Interaction**: Allows users to select specific images to search or choose all available images in the `image/` folder.
- **Detailed Logging**: Logs actions and errors to facilitate debugging and tracking.

## Installation

1. **Install Required Libraries**:

   ```bash
   pip install pywin32 opencv-python numpy pyautogui pytesseract
   ```

2. **Install Tesseract OCR**:

   - Download and install Tesseract OCR from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).
   - Ensure Tesseract’s installation path is added to your `PATH` environment variable.

## Usage

1. **Prepare Configuration and Images**:
   - Place the window title in the `bin/title.config` file.
   - Store the images to be searched for in the `image/` directory.

2. **Run the Script**:
   - Execute the script using Python:

   ```bash
   python main.py
   ```

3. **Image Selection**:
   - Upon running, the script will prompt you to select images for the search. You can choose specific images by entering their corresponding numbers or select all images by entering `0`.

## Project Structure

- **`main.py`**: The primary script that handles window detection, image searching, and text extraction.
- **`bin/title.config`**: Configuration file where the window title to search for is specified.
- **`image/`**: Folder containing images to be used in the screen search.

## Detailed Functions

- **Window Detection**: `_f(t)` locates a window based on the title provided.
- **Configuration File Reading**: `_r(f)` reads the window title from a specified configuration file.
- **Image Search and Processing**: `_f_img(p, th)` searches for the image on the screen, applying Gaussian blur for better accuracy.
- **Text Extraction**: `_e(p, l)` extracts and processes text from images using OCR.
- **User Interaction and Execution**: The `main()` function orchestrates the overall process, including user input and image processing.
- **Logging**: `_log_update(message)` logs detailed updates about the script's activities and errors.

## Development

To further develop or modify this project:

- **Window Interaction**: Adjust `_f(t)` for more complex window searches or handle multiple windows.
- **Image Search Logic**: Enhance `_f_img(p, th)` for different image matching techniques or thresholds.
- **Text Extraction Settings**: Modify `_e(p, l)` to fine-tune OCR configurations or support additional languages.

## Support

For any issues, suggestions, or contributions, please reach out through GitHub Issues or contact the developer directly via email.

## License

This project is licensed under the [MIT License](LICENSE).
