from flask import Flask, render_template, request
from config import Config
from mp3_form import MP3Form
from upload import upload_file
import templates

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['mp3','mp4','wav'])

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from flask_uploads import UploadSet, AUDIO, configure_uploads
audios = UploadSet('sounds', AUDIO)
configure_uploads(app, audios)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    form = MP3Form()
    return render_template("sound.html", form=form)

@app.route('/uploadMP3', methods=['POST'])
def post_mp3():
#   upload_file(request)
    filename = audios.save(request.files['audio'])
    url = audios.url(filename)
    return url + ""

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run()
