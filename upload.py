from os.path import join
from werkzeug.utils import secure_filename
from flask import request, redirect, url_for, flash



def upload_file(request):
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    # if user does not select file, browser also
    # submit a empty part without filename
    if not file or file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    filename = file.filename
    if allowed_file(filename):
        filename = secure_filename(filename)
        file.save(join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
