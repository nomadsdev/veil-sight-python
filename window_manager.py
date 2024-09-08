import win32gui as _w32g
import logging
import ctypes
from ctypes import wintypes

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user32 = ctypes.windll.user32
user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
user32.IsWindowVisible.argtypes = [wintypes.HWND]
user32.IsWindowVisible.restype = wintypes.BOOL

def find_window_by_title(titles, exact_match=True):
    if isinstance(titles, str):
        titles = [titles]

    results = {}
    for title in titles:
        try:
            windows = find_windows(title, exact_match)
            if windows:
                results[title] = windows
        except Exception as e:
            logging.error(f"Error finding windows with title '{title}': {e}")

    return results

def find_windows(title, exact_match):
    if exact_match:
        return find_exact_window(title)
    else:
        return find_partial_windows(title)

def find_exact_window(title):
    hwnd = _w32g.FindWindow(None, title)
    if hwnd:
        if is_window_visible(hwnd):
            logging.info(f"Found visible window: '{title}' with handle: {hwnd}")
            return [(hwnd, title)]
        else:
            logging.info(f"Window '{title}' found but not visible.")
    else:
        logging.info(f"No window found with title '{title}'")
    return []

def find_partial_windows(title):
    matching_windows = []

    def enum_windows_proc(hwnd, param):
        title_len = user32.GetWindowTextLengthW(hwnd)
        if title_len > 0:
            buffer = ctypes.create_unicode_buffer(title_len + 1)
            user32.GetWindowTextW(hwnd, buffer, title_len + 1)
            window_title = buffer.value

            if title.lower() in window_title.lower() and is_window_visible(hwnd):
                matching_windows.append((hwnd, window_title))
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
    return user32.IsWindowVisible(hwnd)

if __name__ == "__main__":
    titles = ["Notepad", "Editor"]
    results = find_window_by_title(titles, exact_match=True)
    for title, windows in results.items():
        logging.info(f"Results for title '{title}':")
        for hwnd, window_title in windows:
            logging.info(f" - Handle: {hwnd}, Title: '{window_title}'")
