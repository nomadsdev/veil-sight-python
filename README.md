# VeilSight

**VeilSight** is a versatile automation tool designed to enhance productivity on Windows by automating repetitive tasks. It offers advanced capabilities for window detection, image recognition, and text extraction, making it an ideal solution for streamlining workflows.

## Features

- **Window Detection**: Accurately locate and interact with specific windows using titles defined in a configuration file. Supports both exact and partial title matching.
- **Screen Image Search**: Efficiently search for specific images on your screen using multi-scale and Gaussian blur techniques to enhance accuracy.
- **Text Extraction**: Extract text from images using Tesseract OCR with support for multiple languages, including English and Thai.
- **Multi-Window Support**: Manage multiple windows simultaneously, facilitating automation across various applications.
- **Configurable Settings**: Customize window titles, image folder paths, and OCR language preferences via a `config.ini` file.
- **Robust Error Handling**: Comprehensive error management ensures smooth operation even in the face of issues like missing files or invalid configurations.
- **User-Friendly Interaction**: Select specific images for processing or opt to search all images within a designated folder.
- **Detailed Logging**: Track actions and errors through comprehensive logging for easier troubleshooting and review.
- **Optimized Performance**: Utilize multi-threading for efficient processing of multiple images simultaneously.

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

Create a `config.ini` file in the project directory to specify window titles, image folder paths, and OCR settings. Example configuration:

```ini
[Settings]
image_folder = image/
config_file = config.txt
ocr_language = eng+tha
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
- **`result_saver.py`**: Contains functions for saving search results to a CSV file.
- **`file_manager.py`**: Manages file operations such as reading lines and listing images.
- **`config_manager.py`**: Handles loading and validating the configuration file.
- **`window_manager.py`**: Manages window detection and interaction.
- **`image_processing.py`**: Contains functions for image searching and text extraction.

## Detailed Functions

- **Window Detection**: `find_window(title: str, exact_match: bool = True) -> Path` locates a window by its title with options for exact or partial matching.
- **Configuration Reading**: `load_config(file_path: str) -> Optional[configparser.ConfigParser]` reads settings from the `config.ini` file.
- **Image Search**: `find_image_on_screen(image_path: str, threshold: float = 0.8) -> bool` searches for an image on the screen with multi-scale support and image processing for increased accuracy.
- **Text Extraction**: `extract_text_from_image(image_path: str, language: str = 'eng') -> str` extracts text from images using Tesseract OCR.
- **Result Logging**: `save_results(results: list, output_file: str = 'results.csv') -> None` saves search results, including image locations and extracted text, to a CSV file.

## Development

To extend or customize VeilSight:

- **Window Interaction**: Enhance `find_window` to support more complex scenarios, such as interacting with multiple instances of the same application.
- **Image Processing**: Improve `find_image_on_screen` by experimenting with different image matching techniques, such as edge detection or feature matching.
- **OCR Customization**: Modify `extract_text_from_image` to better suit specific OCR tasks or to add support for additional languages.
- **Advanced Configuration**: Expand the `config.ini` to include more parameters, such as custom image processing options or additional window search criteria.
- **Optimized Performance**: Enhance multi-threading capabilities and explore additional optimization techniques to handle larger image datasets more efficiently.

## Support

For help, bug reports, or feature requests, please use the GitHub Issues page or contact the developer via email.

## License

VeilSight is licensed under the MIT License.
