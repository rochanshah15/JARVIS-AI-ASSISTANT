import wolframalpha
import pyttsx3
import speech_recognition

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

def get_wolfram(query):
    apikey = "QP3T42-7JX5XUPGJQ"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    try:                
        answer = next(requested.results).text
        return answer
    except Exception as e:
        print(e)
        speak("Sorry, Value isn't answerable.")
        
def calc(query):
    term = str(query)
    term = term.replace("multiply", "*")
    term = term.replace("by", "/")
    term = term.replace("plus", "+")
    term = term.replace("minus", "-")
    final_term = str(term)
    try:
        result = get_wolfram(final_term)
        print(f"calc: {result}")
        speak(f"{result}")
    except Exception as e:
        print(e)
        speak("Sorry, I am unable to calculate that.")