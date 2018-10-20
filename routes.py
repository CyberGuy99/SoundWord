from flask import Flask
from flask import render_template
from config import Config
from mp3_form import MP3Form
import templates

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    form = MP3Form()
    return render_template("sound.html", form=form)


if __name__ == "__main__":
    app.run()
