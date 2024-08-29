# VeilSight

**VeilSight** is an advanced tool designed to automate interactions with the Windows operating system by locating windows, finding images on the screen, and extracting text from these images. It integrates various technologies to streamline tasks and enhance productivity.

## Features

- **Window Search**: Locate windows in the Windows operating system using the window title from a configuration file.
- **Image Search**: Find a specific image on the screen and display its location.
- **Text Extraction from Images**: Use Tesseract OCR to extract text from the found image, supporting both English and Thai languages.
- **Update Logging**: Logs detailed updates about the status of window searches, image searches, and text extraction for better tracking and debugging.

## Installation

1. **Install the necessary libraries**:

    ```bash
    pip install pywin32 opencv-python numpy pyautogui pytesseract
    ```

2. **Install Tesseract OCR**:

    - Download Tesseract OCR from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)
    - Install Tesseract and add its path to your `PATH` system

## Usage

1. **Configure files and images**:
    - Place the configuration file containing the window title in `bin/title.config`
    - Place the image to search for in `bin/image.png`

2. **Run the script**:
    - Use the following Python command to run the script

    ```bash
    python main.py
    ```

## Project Structure

- `main.py`: The main script that performs window and image search operations.
- `bin/title.config`: Configuration file storing the window title to search for.
- `bin/image.png`: The image to search for on the screen.

## Development

- **Window Check**: The function `_f(t)` is used to locate a window by its title.
- **Configuration File Reading**: The function `_r(f)` is used to read the window title from the configuration file.
- **Image Search**: The function `_f_img(p)` is used to locate an image on the screen.
- **Text Extraction from Images**: The function `_e(p, l)` is used to extract text from the image.
- **Update Logging**: The function **_log_update(message)** is used to log detailed update messages to track the script's activities and errors.

## Support

If you have any questions or suggestions regarding this project, you can contact through GitHub Issues or email the developer.

## License

This project is licensed under the [MIT License]
