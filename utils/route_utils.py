import revAPI
from SoundForm.analyzers.counts import word_frequencies
from SoundForm.analyzers.sentiment import analyze_sentiment

#mock method change later
def get_pol(text):
    return "LEFT"


def analyze_text_full(path, doPol, doSent, doFreq):
    text_format = revAPI.audio_to_text(path)
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
    return full_out
