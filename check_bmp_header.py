def check_bmp_header(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_type = file.read(2)
            if file_type != b'BM':
                print("Not a BMP file")
                return False

            file_size = int.from_bytes(file.read(4), 'little')

            file.seek(4, 1)

            header_size = int.from_bytes(file.read(4), 'little')
            if header_size not in [40, 124, 108]:  # Checking common header sizes
                print("Unexpected BMP header size")
                return False
            
            width = int.from_bytes(file.read(4), 'little')
            height = int.from_bytes(file.read(4), 'little')

            color_planes = int.from_bytes(file.read(2), 'little')
            bits_per_pixel = int.from_bytes(file.read(2), 'little')
            
            compression = int.from_bytes(file.read(4), 'little')

            if width <= 0 or height <= 0:
                print("Invalid image dimensions")
                return False
            
            if color_planes != 1:
                print("Invalid number of color planes")
                return False
            
            if bits_per_pixel not in [1, 4, 8, 24, 32]:
                print("Unsupported bits per pixel")
                return False

            if compression != 0:
                print("Compression not supported")
                return False

            print(f"File Size: {file_size} bytes")
            print(f"Header Size: {header_size} bytes")
            print(f"Width: {width}, Height: {height}")
            print(f"Color Planes: {color_planes}")
            print(f"Bits Per Pixel: {bits_per_pixel}")
            print(f"Compression: {compression}")

            return True

    except Exception as e:
        print(f"Error: {e}")
        return False

file_path = 'path_to_your_image.bmp'
if check_bmp_header(file_path):
    print("The file is a valid BMP image.")
else:
    print("The file is not a valid BMP image.")
