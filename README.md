# VeilSight

**VeilSight** is a powerful automation tool designed to enhance productivity on Windows by automating repetitive tasks. With advanced window detection, image recognition, and text extraction capabilities, VeilSight is an ideal solution for those looking to streamline their workflow.

## Features

- **Window Detection**: Accurately locate and interact with specific windows using titles defined in a configuration file. Supports exact and partial title matching.
- **Screen Image Search**: Efficiently search for specific images on your screen using multi-scale and Gaussian blur techniques for enhanced accuracy.
- **Text Extraction**: Extract text from images using Tesseract OCR with support for multiple languages, including English and Thai.
- **Multi-Window Support**: Handle multiple windows simultaneously, making it easy to automate tasks across different applications.
- **Configurable Settings**: Customize window titles, image folder paths, and OCR language preferences using a simple `config.ini` file.
- **Robust Error Handling**: Comprehensive error management ensures the tool runs smoothly, even in the face of unexpected issues like file loading errors or missing configurations.
- **User-Friendly Interaction**: Easily select specific images for processing or opt to search all images within a designated folder.
- **Detailed Logging**: Track actions and errors for troubleshooting and review through comprehensive logging.

## Installation

### 1. Install Required Libraries

Ensure all dependencies are installed by running:

```bash
pip install pywin32 opencv-python numpy pyautogui pytesseract
```

### 2. Install Tesseract OCR

Download and install Tesseract OCR from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract). After installation:

- Add Tesseract's installation path to your `PATH` environment variable to ensure it can be called from anywhere.

## Configuration

### 1. Create or Edit the Configuration File

Create a `config.ini` file in the project directory, specifying window titles, image folder paths, and OCR settings. For example:

```ini
[Window]
title = Your Window Title

[Image]
folder = image/

[OCR]
language = eng+tha
```

### 2. Organize Your Images

Place the images you intend to search for within the folder specified in the `config.ini` file (default is `image/`).

## Usage

### 1. Run the Script

Execute the script using Python:

```bash
python main.py
```

### 2. Image Selection

You will be prompted to select images for searching. Enter the corresponding numbers to select specific images or enter `0` to select all images in the folder.

### 3. OCR Language Selection

Choose the OCR language for text extraction, as specified in the `config.ini` file.

## Project Structure

- **`main.py`**: The core script that manages window detection, image searching, and text extraction.
- **`config.ini`**: Configuration file where you define window titles, image folder paths, and OCR settings.
- **`image/`**: Directory containing images to be used for screen searches.

## Detailed Functions

- **Window Detection**: `find_window(title, exact_match=True)` locates a window by its title with options for exact or partial matching.
- **Configuration Reading**: `load_config(file_path)` reads settings from the `config.ini` file.
- **Image Search**: `find_image_on_screen(image_path, threshold=0.8)` searches for an image on the screen with multi-scale support and image processing for increased accuracy.
- **Text Extraction**: `extract_text_from_image(image_path, language='eng')` extracts text from images using Tesseract OCR.
- **Result Logging**: `save_results(results, output_file='results.csv')` saves search results, including image locations and extracted text, to a CSV file.

## Development

To further extend or customize VeilSight:

- **Window Interaction**: Enhance `find_window` to support more complex scenarios, such as interacting with multiple instances of the same application.
- **Image Processing**: Improve `find_image_on_screen` by experimenting with different image matching techniques, such as edge detection or feature matching.
- **OCR Customization**: Modify `extract_text_from_image` to better suit specific OCR tasks or to add support for additional languages.
- **Advanced Configuration**: Expand the `config.ini` to include more parameters, such as custom image processing options or additional window search criteria.

## Support

For help, bug reports, or feature requests, please use the GitHub Issues page or contact the developer via email.

## License

VeilSight is licensed under the MIT License. See the LICENSE file for details.
