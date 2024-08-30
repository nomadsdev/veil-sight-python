def read_first_line(file_path):
    try:
        with open(file_path, 'r') as file:
            line = file.readline().strip()
            if not line:
                raise ValueError("Config file is empty")
        return line
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except ValueError as e:
        print(e)
        return None

def list_images(folder):
    import os
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    try:
        return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(valid_extensions)]
    except FileNotFoundError:
        print(f"Folder not found: {folder}")
        return []