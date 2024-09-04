import win32gui as _w32g
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_window_by_title(titles, exact_match=True):
    if isinstance(titles, str):
        titles = [titles]

    results = {}
    for title in titles:
        try:
            if exact_match:
                windows = find_exact_window(title)
            else:
                windows = find_partial_windows(title)
            
            if windows:
                results[title] = windows
        except Exception as e:
            logging.error(f"An error occurred while finding the window titled '{title}': {e}")

    return results

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
    titles = ["Notepad", "Editor"]
    results = find_window_by_title(titles, exact_match=True)
    for title, windows in results.items():
        logging.info(f"Results for title '{title}':")
        for hwnd, window_title in windows:
            logging.info(f" - Handle: {hwnd}, Title: '{window_title}'")
