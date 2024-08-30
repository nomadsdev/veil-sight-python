import win32gui as _w32g

def find_window(title):
    h = _w32g.FindWindow(None, title)
    if h:
        print(f"Found window: {title} with handle: {h}")
        return h
    else:
        print(f"No window found with title: {title}")
        return None