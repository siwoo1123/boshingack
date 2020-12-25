from gtts import gTTS

text ="The new year of 2021 has dawned."
filename = "helloKO.mp3"

tts = gTTS(text=text, lang='en')
tts.save(filename)