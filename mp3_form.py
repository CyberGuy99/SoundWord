from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class MP3Form(FlaskForm):
    filename = StringField('MP3 Name', validators=[DataRequired()])
    pol = BooleanField('Classify Wing of Politics')
    sent = BooleanField('Classify Sentiment')
    freq = BooleanField('Compute Important Word Frequencies')
    submit = SubmitField('Upload')
