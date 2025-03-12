import pyttsx3
import speech_recognition
import datetime
import pywhatkit
from time import sleep
from datetime import timedelta
from datetime import datetime
import pyautogui

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


def sendMessage():
    speak("Who do you wanna message?")
    name = takeCommand().lower()
    dict_nums = {'meet':'9106801951', 'viraj':'7043168047', 'vatsal':'8320735065', 'rc':'9825327667'}
    if name in ['meet','viraj', 'vatsal', 'rc']:
        speak("What's the message?")
        message = takeCommand()
        strTime = int(datetime.now().strftime("%H"))
        update = int((datetime.now()+timedelta(minutes=1)).strftime("%M"))
        print(strTime, update)
        pywhatkit.sendwhatmsg(f"+91{dict_nums[name]}", message, time_hour=strTime, time_min=update)
        sleep(5)
        pyautogui.press('enter')
        speak("Message sent successfully!")
    else:
        speak("Sorry, I don't have that person's number.")