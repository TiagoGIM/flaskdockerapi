import os
from flask import request
from werkzeug.utils import secure_filename


def upload_file():
    file = request.files['file']
    if file.filename == '' or not file.filename.endswith('.xlsx'):
        return 'Invalid file', 400
    filename = secure_filename(file.filename)
    print(filename)
    file.save(os.path.join('./data', filename))
    return 'file uploaded successfully'
