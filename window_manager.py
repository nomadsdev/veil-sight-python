import win32gui as _w32g
import logging
import ctypes
from ctypes import wintypes
from concurrent.futures import ThreadPoolExecutor, as_completed
import configparser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user32 = ctypes.windll.user32
user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
user32.IsWindowVisible.argtypes = [wintypes.HWND]
user32.IsWindowVisible.restype = wintypes.BOOL

def load_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        return config
    except Exception as e:
        logging.error(f"Error loading config file '{file_path}': {e}")
        return None

def find_window_by_title(titles, exact_match=True):
    if isinstance(titles, str):
        titles = [titles]

    results = {}
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(find_windows, title, exact_match): title for title in titles}

        for future in as_completed(futures):
            title = futures[future]
            try:
                windows = future.result()
                if windows:
                    results[title] = windows
            except Exception as e:
                logging.error(f"Error finding windows with title '{title}': {e}")

    return results

def find_windows(title, exact_match):
    """ค้นหาหน้าต่างตามชื่อ ถ้าต้องการหาตรงเป๊ะก็จะใช้ exact match"""
    return find_exact_window(title) if exact_match else find_partial_windows(title)

def find_exact_window(title):
    hwnd = _w32g.FindWindow(None, title)
    if hwnd and is_window_visible(hwnd):
        logging.info(f"Found visible window: '{title}' with handle: {hwnd}")
        return [(hwnd, title)]
    else:
        logging.info(f"No visible window found with title '{title}'")
    return []

def find_partial_windows(title):
    matching_windows = []

    def enum_windows_proc(hwnd, param):
        try:
            title_len = user32.GetWindowTextLengthW(hwnd)
            if title_len > 0:
                buffer = ctypes.create_unicode_buffer(title_len + 1)
                user32.GetWindowTextW(hwnd, buffer, title_len + 1)
                window_title = buffer.value

                if title.lower() in window_title.lower() and is_window_visible(hwnd):
                    matching_windows.append((hwnd, window_title))
        except Exception as e:
            logging.error(f"Error while enumerating windows: {e}")
        return True

    _w32g.EnumWindows(enum_windows_proc, None)

    if matching_windows:
        logging.info(f"Found {len(matching_windows)} visible window(s) containing '{title}':")
        for hwnd, window_title in matching_windows:
            logging.info(f" - Handle: {hwnd}, Title: '{window_title}'")
    else:
        logging.info(f"No visible windows found containing '{title}'")

    return matching_windows

def is_window_visible(hwnd):
    try:
        return user32.IsWindowVisible(hwnd)
    except Exception as e:
        logging.error(f"Error checking window visibility for hwnd {hwnd}: {e}")
        return False

if __name__ == "__main__":
    config = load_config('config.ini')
    if config:
        titles = config.get('Settings', 'titles', fallback='').split(',')
        if titles:
            results = find_window_by_title(titles, exact_match=True)
            for title, windows in results.items():
                logging.info(f"Results for title '{title}':")
                for hwnd, window_title in windows:
                    logging.info(f" - Handle: {hwnd}, Title: '{window_title}'")
        else:
            logging.warning("No titles found in config.")
    else:
        logging.error("Configuration file could not be loaded.")
