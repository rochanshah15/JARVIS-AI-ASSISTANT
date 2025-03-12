import speech_recognition
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser
from time import sleep

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
        print("Say that again",e)
        return "None"
    return query

query = takeCommand().lower()

def searchGoogle(query):
    if 'google' in query:
        import wikipedia as google
        query=query.replace('google','')
        query=query.replace('search','')
        query=query.replace('for','')
        speak("Here is what I found on the web")
        
        try:
            pywhatkit.search(query)
            result = google.summary(query,1)
            speak(result)
        except Exception as e:
            speak("Sorry, the output can't be speaked")
            
def searchYoutube(query):
    if 'youtube' in query:
        query=query.replace('youtube','')
        query=query.replace('search','')
        query=query.replace('for','')
        web = 'https://www.youtube.com/results?search_query='+query
        webbrowser.open(web)
        speak("Here is what I found on youtube")

def playYoutube(query):
    if 'youtube' in query:
        query=query.replace('youtube','')
        query=query.replace('on','')
        query=query.replace('play','')
        try:
            pywhatkit.playonyt(query)
            speak("Here is what I found on youtube")
            sleep(2)
        except Exception as e:
            speak("Sorry, I couldn't find anything on youtube")
  
def searchWikipedia(query):
    if 'wikipedia' in query:
        query=query.replace('wikipedia','')
        query=query.replace('search','')
        query=query.replace('for','')
        results = wikipedia.summary(query, sentences = 2)
        speak("According to Wikipidea..")
        print(results)
        speak(results)