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

import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer() 
while True:
        with speech_recognition.Microphone() as mic: 
            recognizer.adjust_for_ambient_noise(mic, duration=0.4) 
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

    