from flask import Flask, render_template, request, flash
from config import Config
from mp3_form import MP3Form
#import route_utils #uncomment this after revAPI complete

app = Flask(__name__)
app.config.from_object(Config)

from flask_uploads import UploadSet, AUDIO, configure_uploads
audios = UploadSet('sounds', AUDIO)
configure_uploads(app, audios)

@app.route("/")
def home():
    form = MP3Form()
    return render_template("sound.html", form=form)

@app.route('/uploadMP3', methods=['POST'])
def post_mp3():
    form = MP3Form()
    if form.validate_on_submit():
        filename = audios.save(request.files['audio'])
        url = audios.url(filename)
        doPol = form.pol.data
        doSent = form.sent.data
        doFreq = form.sent.data

        full_file = app.config['UPLOADS_DEFAULT_DEST'] + "/sounds/" + filename
        print(full_file)
        return full_file
        analysis = analyze_text_full(full_file, doPol, doSent, doFreq)
        return '\n'.join(analysis)
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
