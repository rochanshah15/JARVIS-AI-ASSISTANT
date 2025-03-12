import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictApp = {"command prompt":"cmd", 
           "paint":"mspaint", 
           "word":"winword", 
           "excel":"excel", 
           "chrome":"chrome",
           "vs code":"code",
           "powerpoint":"powerpnt", 
           "whatsapp": "whatsapp",
           "notepad": "notepad", 
           "calculator": "calc", 
           "task manager": "taskmgr", 
           "file explorer": "explorer", 
           "settings": "ms-settings:", 
           "snipping tool": "SnippingTool", 
           "edge": "msedge", 
           "media player": "wmplayer", 
           "mail": "outlook",
        #    "whatsapp": "whatsapp:", 
           "spotify": "spotify", 
        #    "discord": "discord", 
        #    "telegram": "telegram:", 
    }

def openAppWeb(query):
    speak("Launching boss")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("launch", "")
        query = query.replace("www.", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictApp[app]}")
                
def closeAppWeb(query):
    speak("Closing boss")
    if "one tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("Done boss")
    elif "two tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Done boss")
    elif "three tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        speak("Done boss")
        pyautogui.hotkey("ctrl", "w")
    elif "all tabs" in query:
        pyautogui.hotkey("ctrl", "shift", "w")
        speak("Done boss")
    elif "app":
        pyautogui.hotkey("alt", "f4")
        speak("Done boss")
    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /im {dictApp[app]}")
        