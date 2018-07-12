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
    sentences = []
    tones = []
    i = 0
    if "sentences_tone" in tone_dict:
        sentences = tone_dict.get("sentences_tone")
    else:
        sentences = tone_dict.get("document_tone")
    for sentence in sentences:
        tone = sentence.get("tones")[0].get("tone_id")
        if tone in {"anger", "disgust", "fear", "conscientiousness", "emotional range"}:
            tone = "Uncertainty"
        elif tone == "sadness":
            tone = "Apology"
        else:
            tone = "Good News"
        tones.append(tone)
    for sentence in nltk.sent_tokenize(text):
        sentences_with_tones.append("<express-as type=" + tones[i] + ">" + sentence + "</express-as>")
        i += 1
    print (sentences_with_tones)
    return sentences_with_tones

if __name__ == '__main__':
    getTones("I love you! I hate you! I hate everyone! No wait, I love everyone!")
