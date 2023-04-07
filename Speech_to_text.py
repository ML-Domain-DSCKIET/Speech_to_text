# -*- coding: utf-8 -*-


import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Now..")
    audio = r.listen(source)
    
try:
    text = r.recognize_google(audio)
    print(f"You Said: {text}")
    
except sr.UnknownValueError:
    print("Sorry, I counldn't understand what you said")
except sr.RequestError as e:
    print(f"Request error: {e}")
