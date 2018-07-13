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
    print(tone_dict)
    sentences_with_tones = []
    sentences = []
    tones = []
    i = 0
    if text != "":
        if "sentences_tone" in tone_dict:
            sentences = tone_dict.get("sentences_tone")
            for sentence in sentences:
                #print("-----sentences-------------")
                #print(sentences)
                #print("-----sentence-------------")
                #print(sentence)
                if len(sentence.get("tones")) == 0:
                    tone = ""
                else:
                    tone = sentence.get("tones")[0].get("tone_id")
                    if tone in {"anger", "disgust", "fear", "consciousness", "emotionalRange"}:
                        tone = "Uncertainty"
                    elif tone == "sadness":
                        tone = "Apology"
                    else:
                        tone = "GoodNews"
                tones.append(tone)
            print(tones)
            print(nltk.sent_tokenize(text))
            for sentence in nltk.sent_tokenize(text):
                if tones[i] == "":
                    sentences_with_tones.append(sentence)
                else:
                    sentences_with_tones.append("<speak><express-as type=\"" + tones[i] + "\">" + sentence + "</express-as></speak>")
                i += 1
        else:
            sentences_with_tones = [text]
    print(sentences_with_tones)
    return sentences_with_tones

if __name__ == '__main__':
    getTones("I love you!")
