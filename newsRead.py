import pyttsx3
import json
import requests
import speech_recognition

# 835a6252d0b8449bacf3b28a47b8efbd
# 8edf24126c92f8a4c3bc86a7d580f959 : GNews

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

def latestNews():
    api_dict = {
        "business" : "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=835a6252d0b8449bacf3b28a47b8efbd",
        "entertainment" : "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=835a6252d0b8449bacf3b28a47b8efbd",
        "health" : "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=835a6252d0b8449bacf3b28a47b8efbd",
        "science" : "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=835a6252d0b8449bacf3b28a47b8efbd",
        "sports" : "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=835a6252d0b8449bacf3b28a47b8efbd",
        "technology" : "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=835a6252d0b8449bacf3b28a47b8efbd"
    }
    
    content = None
    url = None
    speak("Which category of news you want to hear (business, entertainment, health, science, sports, technology)?")
    query = takeCommand().lower()
    if query in api_dict.keys():
        url = api_dict[query]
        print("url found")
    else:
        url = True
        speak("Sorry, I am not able to find the category you requested.")
        print("Sorry, I am not able to find the category you requested.")
        return
    
    news = requests.get(url).text
    data = json.loads(news)
    arts = data["articles"]
    
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print("For more info, visit:",news_url)
        speak("For more info, visit the provided link")
        
        speak("Do you wanna continue?")
        cont = takeCommand().lower()
        if "no" in cont:
            break
        elif "yes" in cont:
            continue
        else:
            speak("Please respond with yes or no.")
            cont = takeCommand().lower()
            if "no" in cont:
                break
            elif "yes" in cont:
                continue
    speak("that's all")