from flask import Flask, request, jsonify
import os
import tempfile
from PIL import Image
import pytesseract
from src import ocr

app = Flask(__name__)

@app.route('/extract-coordinates', methods=['POST'])
def extract_coordinates():
    if 'image' not in request.files or 'text' not in request.form:
        return jsonify({"error": "Please provide an image file and text to search."}), 400
    
    image_file = request.files['image']
    search_text = request.form['text']
    
    # Create a temporary file in the /tmp directory
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png', dir='/tmp') as temp_file:
        image_path = temp_file.name
        image_file.save(image_path)
    
    # Process the image
    coordinates = ocr.extract_text_coordinates(image_path, search_text)
    
    # Cleanup the temporary file
    os.remove(image_path)
    
    if coordinates:
        return jsonify({"coordinates": coordinates})
    else:
        return jsonify({"error": "Text not found in the image."}), 404