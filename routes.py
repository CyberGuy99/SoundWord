from flask import Flask, render_template, request, flash
from config import Config
from mp3_form import MP3Form
import revAPI
from counts import word_frequencies
from sentiment import analyze_sentiment
import templates

ALLOWED_EXTENSIONS = set(['mp3','mp4','wav'])

app = Flask(__name__)
app.config.from_object(Config)

from flask_uploads import UploadSet, AUDIO, configure_uploads
audios = UploadSet('sounds', AUDIO)
configure_uploads(app, audios)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    form = MP3Form()
    return render_template("sound.html", form=form)

def get_pol(text):
    return "LEFT"

@app.route('/uploadMP3', methods=['POST'])
def post_mp3():
    form = MP3Form()
    if form.validate_on_submit():
        filename = audios.save(request.files['audio'])
        url = audios.url(filename)
        doPol = form.pol.data
        doSent = form.sent.data
        doFreq = form.sent.data

        full_file = app.config['UPLOADS_DEFAULT_DEST'] + "/sounds/" + filename)
        print(full_file)
        text_format = revAPI.audio_to_text(full_file)
        full_out = ["pol: {} sent: {} freq: {}".format(doPol,doSent,doFreq)]
        for log in text_format:
            output = "Speaker {}: "
            if doPol:
                output += "political: {} ".format(get_pol(text_format))
            if doSent:
                output += "sentiment: {} ".format(analyze_sentiment(text_format))
            if doFreq:
                output += "frequencies: {} ".format(word_frequencies(text_format))
            full_out.append(output)
        return '\n'.join(full_out)
    else:
        #not working at the moment, need to fix this for UI
        flash_errors(form)
        flash("ERROR!")
    return render_template("sound.html", form=form)

#from flask import send_from_directory

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field – %s" % (getattr(form, field).label.text, error),'info')

'''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADS_DEFAULT_DEST'], filename)
'''

if __name__ == "__main__":
    app.run()
