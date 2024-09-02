import win32gui as _w32g
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_window_by_title(title, exact_match=True):
    try:
        if exact_match:
            return find_exact_window(title)
        else:
            return find_partial_windows(title)
    except Exception as e:
        logging.error(f"An error occurred while finding the window: {e}")
        return []

def find_exact_window(title):
    h = _w32g.FindWindow(None, title)
    if h:
        if is_window_visible(h):
            logging.info(f"Found visible window: '{title}' with handle: {h}")
            return [(h, title)]
        else:
            logging.info(f"Found window: '{title}' but it is not visible.")
            return []
    else:
        logging.info(f"No window found with the exact title: '{title}'")
        return []

def find_partial_windows(title):
    matching_windows = []

    def enum_windows_proc(hwnd, param):
        window_title = _w32g.GetWindowText(hwnd)
        if window_title and title.lower() in window_title.lower():
            if is_window_visible(hwnd):
                matching_windows.append((hwnd, window_title))
        return True

    _w32g.EnumWindows(enum_windows_proc, None)

    if matching_windows:
        logging.info(f"Found {len(matching_windows)} visible window(s) containing '{title}':")
        for hwnd, window_title in matching_windows:
            logging.info(f" - Handle: {hwnd}, Title: '{window_title}'")
    else:
        logging.info(f"No visible windows found containing the title: '{title}'")

    return matching_windows

def is_window_visible(hwnd):
    return _w32g.IsWindowVisible(hwnd) == 1

if __name__ == "__main__":
    find_window_by_title("Notepad", exact_match=True)
    find_window_by_title("Editor", exact_match=False)
