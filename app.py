from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
from utils import encode_message, decode_message

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploaded/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    image = request.files['image']
    message = request.form['message']

    if image and message:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(filepath)

        encoded_path = encode_message(filepath, message)
        return send_from_directory(app.config['UPLOAD_FOLDER'], encoded_path, as_attachment=True)

    return redirect(url_for('index'))

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(filepath)
            message = decode_message(filepath)
            return render_template('decode.html', message=message)

    return render_template('decode.html', message=None)

if __name__ == '__main__':
    app.run(debug=True)
