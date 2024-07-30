from PIL import Image
import pytesseract

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed

def extract_text_coordinates(image_path, search_text):
    image = Image.open(image_path)
   
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    print(data)
    search_text = search_text.lower()
    coordinates_list = []
   
    for i in range(len(data['text'])):
        # Check for the exact match of the search text in the recognized text
        if search_text in data['text'][i].lower():
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            coordinates_list.append((x + w // 2, y + h // 2))
    
    return coordinates_list
