# VeilSight 
 
**VeilSight** is a sophisticated tool designed to automate interactions with the Windows operating system. It includes capabilities for locating windows, finding images on the screen, and extracting text from these images. This tool integrates multiple technologies to streamline tasks and enhance productivity. 
 
## Features 
- **Window Search**: Locate windows in the Windows operating system using the window title from a configuration file. 
- **Image Search**: Find specific images on the screen and display their location. 
- **Text Extraction from Images**: Use Tesseract OCR to extract text from found images, supporting both English and Thai languages. 
- **Error Handling**: Improved error handling for image loading issues. 
- **User Interaction**: Select images to search from the `image/` folder, with options to choose specific images or all images. 
- **Update Logging**: Logs detailed updates about window searches, image searches, and text extraction for better tracking and debugging. 
 
## Installation 
1. **Install the necessary libraries**: 
 
   ```bash 
   pip install pywin32 opencv-python numpy pyautogui pytesseract 
   ``` 
 
2. **Install Tesseract OCR**: 
 
   - Download Tesseract OCR from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract) 
   - Install Tesseract and add its path to your `PATH` environment variable 
 
## Usage 
1. **Configure files and images**: 
   - Place the configuration file containing the window title in `bin/title.config` 
   - Place the images to search for in the `image/` folder 
 
2. **Run the script**: 
   - Use the following Python command to run the script 
   ```bash 
   python main.py 
   ``` 
 
3. **Select Images**: 
   - When prompted, select the images you want to search for by entering their corresponding numbers, or enter `0` to select all images in the `image/` folder. 
 
## Project Structure 
- `main.py`: The main script that performs window and image search operations. 
- `bin/title.config`: Configuration file storing the window title to search for. 
- `image/`: Directory containing images to search for on the screen. 
 
## Development 
- **Window Check**: The function `_f(t)` locates a window by its title. 
- **Configuration File Reading**: The function `_r(f)` reads the window title from the configuration file. 
- **Image Search**: The function `_f_img(p)` locates an image on the screen and handles image loading errors. 
- **Text Extraction from Images**: The function `_e(p, l)` extracts text from the image using OCR. 
- **User Interaction**: The function `main()` manages user input for selecting images and running the search. 
- **Update Logging**: The function `_log_update(message)` logs detailed update messages to track the script's activities and errors. 
 
## Support 
If you have any questions or suggestions regarding this project, please contact through GitHub Issues or email the developer. 
 
## License 
This project is licensed under the [MIT License]. 
