import json
import re
import nltk
from watson_developer_cloud import ToneAnalyzerV3

nltk.download('punkt')
tone_analyzer = ToneAnalyzerV3(
    version ='2017-09-21',
    username =  "12f49ec9-2bc1-447c-824b-42236c61d8e6",
    password = "labRRKqSDxLj"
)
content_type = 'application/json'
check_sentences = True

def getTones(text):
    tone_dict = tone_analyzer.tone({"text": text}, content_type, check_sentences)
    sentences_with_tones = []
    split_text = nltk.sent_tokenize(text)
    i = 0
    if text != "":
        if "sentences_tone" in tone_dict:
            for sentence in tone_dict.get("sentences_tone"):
                if len(sentence.get("tones")) == 0:
                    sentences_with_tones.append(split_text[i])
                else:
                    tone = sentence.get("tones")[0].get("tone_id")
                    if tone in {"anger", "disgust", "fear", "consciousness", "emotionalRange"}:
                        tone = "Uncertainty"
                    elif tone == "sadness":
                        tone = "Apology"
                    else:
                        tone = "GoodNews"
                    sentences_with_tones.append("<speak><express-as type=\"" + tone + "\">" + split_text[i] + "</express-as></speak>")
                i += 1
        else:
            sentences_with_tones = [text]
    print(sentences_with_tones)
    return sentences_with_tones

if __name__ == '__main__':
    getTones("I love you!")
