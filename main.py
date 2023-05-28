
from flask import Flask, jsonify, request
from PIL import Image
import easyocr
import numpy as np

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def perform_ocr():
    # Get the uploaded image file from the request
    image_file = request.files['image']
    
    # Load the image using PIL
    image = Image.open(image_file)
    
    # Convert the image to grayscale if needed
    image = image.convert('L')
    
    # Convert the PIL image to a numpy array
    image_np = np.array(image)
    
    # Perform OCR on the image
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_np)
    
    # Extract the OCR results
    ocr_results = [entry[1] for entry in result]
    
    # Return the OCR results as JSON
    return jsonify({'results': ocr_results})

 #    curl -X POST -F "image=@C:\Users\khera\OneDrive\Desktop\aa.jpg" http://localhost:5000/ocr


@app.route('/')
def home():
    return 'API is running'


if __name__ == '__main__':
    app.run(debug=True)
