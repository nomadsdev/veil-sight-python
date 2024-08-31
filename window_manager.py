import win32gui as _w32g

def find_window(title, exact_match=True):
    try:
        if exact_match:
            h = _w32g.FindWindow(None, title)
            if h:
                print(f"Found window: '{title}' with handle: {h}")
                return h
            else:
                print(f"No window found with the exact title: '{title}'")
                return None
        else:
            matching_windows = []

            def enum_windows_proc(hwnd, param):
                window_title = _w32g.GetWindowText(hwnd)
                if title.lower() in window_title.lower():
                    matching_windows.append((hwnd, window_title))
                return True

            _w32g.EnumWindows(enum_windows_proc, None)

            if matching_windows:
                print(f"Found {len(matching_windows)} window(s) containing '{title}':")
                for hwnd, window_title in matching_windows:
                    print(f" - Handle: {hwnd}, Title: '{window_title}'")
                return matching_windows
            else:
                print(f"No windows found containing the title: '{title}'")
                return None

    except Exception as e:
        print(f"An error occurred while finding the window: {e}")
        return None
