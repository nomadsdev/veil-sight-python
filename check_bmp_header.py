def check_bmp_header(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_type = file.read(2)
            if file_type != b'BM':
                print("Not a BMP file")
                return False

            file.seek(14)
            header_size = int.from_bytes(file.read(4), 'little')
            
            file.seek(18)
            width = int.from_bytes(file.read(4), 'little')
            height = int.from_bytes(file.read(4), 'little')
            
            print(f"Width: {width}, Height: {height}")
            
            return True

    except Exception as e:
        print(f"Error: {e}")
        return False

file_path = 'path_to_your_image.bmp'
if check_bmp_header(file_path):
    print("The file is a valid BMP image.")
else:
    print("The file is not a valid BMP image.")
