from gtts import gTTS
import os
red = open("sample.txt")
text = red.read()
language ='en'

obj = gTTS(text = text, lang=language, slow=False)

obj.save("saample.mp3")

os.system('saample.mp3')
