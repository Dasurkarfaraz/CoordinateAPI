from flask import Flask, request, jsonify
import os
from PIL import Image
import pytesseract
from src import ocr


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# Specify the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed

# def extract_text_coordinates(image_path, search_text):
#     image = Image.open(image_path)
#     data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
#     print(data)
#     search_text = search_text.lower()
#     print(search_text)
#     coordinates_list = []
    
#     for i in range(len(data['text'])):
#         if search_text in data['text'][i].lower():
#             x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
#             coordinates_list.append((x + w // 2, y + h // 2))
    
#     return coordinates_list
# Specify the path to the Tesseract executable

@app.route('/extract-coordinates', methods=['POST'])
def extract_coordinates():
    if 'image' not in request.files or 'text' not in request.form:
        return jsonify({"error": "Please provide an image file and text to search."}), 400
    
    image_file = request.files['image']
    search_text = request.form['text']
    
    image_path = os.path.join('uploads', image_file.filename)
    image_file.save(image_path)
    
    coordinates = ocr.extract_text_coordinates(image_path, search_text)
    
    if coordinates:
        return jsonify({"coordinates": coordinates})
    else:
        return jsonify({"error": "Text not found in the image."}), 404

# if __name__ == '__main__':
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(host='0.0.0.0', port=5000)
