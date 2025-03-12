from time import sleep
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pyttsx3
import speech_recognition
import os
from playsound import playsound

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source, 0, 3)        
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again", e)
        return None  # Return None when it can't understand
    return query

def translate(query):
    if query is None or query.strip() == "":
        speak("I didn't hear anything. Please try again.")
        return
    
    speak("Sure boss!")
    langs = {"english": "en", "gujarati": "gu", "hindi": "hi", "marathi": "mr", "bengali": "bn"}
    print(langs)

    speak("Choose the language in which you want to translate")
    lang = takeCommand().lower()
    
    if lang not in langs:
        speak("Sorry, I didn't recognize that language. Please try again.")
        return
    
    try:
        print(f"Translating to {lang}: {query}")
        translator = Translator()
        translation = translator.translate(query, dest=langs[lang])
        text = translation.text
        print(f"Translation: {text}")
        speak(text)
    except Exception as e:
        speak("Sorry, something went wrong with the translation.")
        print("Error during translation:", e)

