from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username='469c306e-f6d0-4d31-87b3-f603817fb40d',
    password='DOr8056Wp22g'
)
words = ["hello", "hi", "jana"]

def text_to_speech():
    with open('hello_world.wav', 'wb') as audio_file:
        for word in words:
            audio_file.write(
                text_to_speech.synthesize(
                    word, 'audio/wav', 'en-US_AllisonVoice').content)
