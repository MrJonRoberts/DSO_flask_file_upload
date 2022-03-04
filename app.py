from flask import Flask, abort, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
# set up the folders
UPLOAD_FOLDER = 'UPLOADS'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/')
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            msg = "File saved"
            return render_template("home.html", msg=msg)

    return render_template('home.html')



if __name__ == '__main__':
    app.run()