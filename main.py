from src import capture, ocr, utils

def main():
    # Capture the screenshot
    screenshot_path = "screenshots/image.jPG"
    capture.capture_screenshot(screenshot_path)
    
    # Extract coordinates
    search_text = "OFF"
    coordinates = ocr.extract_text_coordinates(screenshot_path, search_text)
    
    # Save coordinates
    folder_path = "output"
    file_name = "coordinates.txt"
    if coordinates:
        utils.save_coordinates_to_file(folder_path, file_name, coordinates, search_text)
                # Specify which element to tap on (e.g., the second element)
        element_index = 0  # 0-based index for the second element
        utils.tap_on_coordinates(coordinates, index=element_index)

    else:
        print("Text not found in the screenshot.")

if __name__ == "__main__":
    main()
