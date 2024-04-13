"""
        *** Speech Recognition ***
            -- setup python latest version
            -- add pip to environment variables
            Installing Packages ==>
                               - pip install SpeechRecognition
                               - pip install gTTS
                               - pip install playsound
                               - pip install pyttsx3
                               - pip install pyaudio
"""

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer() 
"""while True:
        with sr.Microphone() as mic: 
            recognizer.adjust_for_ambient_noise(mic, duration=0.4) 
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")"""

"""def speekText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()"""
with sr.Microphone() as mic:
    print("Silence Please, calibrating background noise")
    r.adjust_for_ambient_noise(mic, duration=2)
    print("calibrated, Now speak.....")

#speekText("Hello World")
    