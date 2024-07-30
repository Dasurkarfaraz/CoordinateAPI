import os

def save_coordinates_to_file(folder_path, file_name, coordinates, search_text):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        file.write(f"Coordinates of '{search_text}': {coordinates}")
    print(f"Coordinates saved to {file_path}")

def tap_on_coordinates(coordinates, index=0):
    if 0 <= index < len(coordinates):
        x, y = coordinates[index]
        os.system(f"adb shell input tap {x} {y}")
        print(f"Tapped on ({x}, {y})")
    else:
        print(f"Invalid index: {index}. There are only {len(coordinates)} elements.")