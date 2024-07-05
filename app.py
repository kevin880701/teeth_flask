import json
from flask import Flask
import os
from datetime import datetime

IMAGE_FOLDER = './Image/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['IMAGE_FOLDER']):
    os.makedirs(app.config['IMAGE_FOLDER'])

@app.route('/')
def hello_world():
    return "Hello so fast"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)
