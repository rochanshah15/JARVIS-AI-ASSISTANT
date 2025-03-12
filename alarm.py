# building JARVIS AI Assistant using Python
import pyttsx3
import speech_recognition
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    alarmTime = str(time)
    print(alarmTime)
    while True:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        if currentTime == alarmTime:
            speak("Alarm Ringing!!")
            os.startfile("ringtone.m4a")
        elif (currentTime + ("00:00:30")) == alarmTime:
            exit()
            
ring(time)