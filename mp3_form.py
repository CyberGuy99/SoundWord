from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from flask_uploads import UploadSet, AUDIO

class MP3Form(FlaskForm):
    filename = StringField('MP3 Name', validators=[DataRequired()])
    pol = BooleanField('Classify Wing of Politics')
    sent = BooleanField('Classify Sentiment')
    freq = BooleanField('Compute Important Word Frequencies')

    audios = UploadSet('sounds', AUDIO)
    audio = FileField('Audio File', validators=[FileRequired(), FileAllowed(audios, "Audio Files Only!")])
    submit = SubmitField('Upload')
