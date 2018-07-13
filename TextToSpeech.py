from watson_developer_cloud import TextToSpeechV1
import TextToTone as tone
text_to_speech = TextToSpeechV1(
    username='469c306e-f6d0-4d31-87b3-f603817fb40d',
    password='DOr8056Wp22g'
)


words1 = ["<express-as type='GoodNews'>I love you!</express-as>",
            "<express-as type='Anger'>I hate you!</express-as>",
                "<express-as type='Anger'>I hate everyone!</express-as>",
                    "<express-as type='GoodNews'>No wait, I love everyone!</express-as>"]
words2 = ["I love you!",
            "I hate you!",
                "I am so sorry",
                    "No wait, I love everyone!"]
def convert_text_to_speech(words):
    with open('hello_world123.wav', 'wb') as audio_file:
        for word in words:
            audio_file.write(
                text_to_speech.synthesize(
                    word, 'audio/wav', 'en-US_AllisonVoice').content)


if __name__ == "__main__":
    # convert_text_to_speech(words)
    words = tone.getTones("I love you! Hello World. I hate you!")
    convert_text_to_speech(words)
    # convert_text_to_speech(words3)
