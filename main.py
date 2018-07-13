import TextToTone as tone
import TextToSpeech as speech
import time
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__, static_url_path='')

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def input_text_post():
    inputText = request.form['inputText']
    # Put conversion methods here and use inputText as the parameter
    tones = tone.getTones(inputText)
    file = speech.convert_text_to_speech(tones)
    time.sleep(5)
    return render_template("audio.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
