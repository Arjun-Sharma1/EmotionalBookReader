from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
import TextToTone as tone
import TextToSpeech as speech
import time

@app.route("/")
def main():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def input_text_post():
    inputText = request.form['inputText']
    # Put conversion methods here and use inputText as the parameter
    tones = tone.getTones(inputText)
    file = speech.convert_text_to_speech(tones)
    time.sleep(20)
    return ('', 204)

if __name__ == "__main__":
    app.debug = True
    app.run()
