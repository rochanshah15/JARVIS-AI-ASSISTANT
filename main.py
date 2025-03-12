# building Saarthi AI Assistant using Python
import pyttsx3  # for mic inp
import speech_recognition  # for speech recognition
import datetime
from datetime import datetime
import os  # for shutdown and open files or apps
import pyautogui  # for hotkeys and press
import webbrowser  # for searching
import random  # for tired (custom playlist)

# custom methods made in different files
from greetMe import greetMe
from weather import get_weather  # for weather
from newsRead import latestNews  # for news
from calculate import calc   # for calculations
from whatsApp import sendMessage  # for wp msgs
from game import play
import pyjokes

from plyer import notification  # for notifications
import speedtest 

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

def set_alarm():
    speak("Please tell me the time you want to set the alarm for.")
    query = takeCommand()

    if query:
        try:
            if "set alarm for" in query:
                time_str = query.split("for")[-1].strip()
                alarm_time = datetime.strptime(time_str, "%H:%M")
                
                timehere = open("Alarmtext.txt","a")
                timehere.write(alarm_time.strftime('%H:%M:%S'))
                timehere.close()
                
                os.startfile("alarm.py")
                print(alarm_time.strftime('%H:%M:%S %p'))
                speak(f"Alarm set for {alarm_time.strftime('%H:%M %p')}")
        except ValueError:
            speak("Sorry, I couldn't understand the time format. Please try again.")


if __name__ == '__main__':
    speak("Hello, I'm Saaarthi your personalized AI Assistant.")
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            greetMe()
            while True:
                query = takeCommand().lower()

                # basics
                if "hello" in query:
                    speak("Hello boss, how are you?")
                elif "i am fine" in query:
                    speak("Good to hear that, how can I help you today?")
                elif "how r u" in query:
                    speak("I am doing great, thanks for asking!")
                elif "go to sleep" in query:
                    speak("Okay boss! Wake me up when you need me.")
                    break
                elif "bye" in query:
                    speak("Goodbye, have a great day!")
                    exit()

                # open app
                elif "open" in query:
                    # from dictApp import openAppWeb
                    # openAppWeb(query)
                    query = query.replace("open","")
                    query = query.replace(" ","")
                    speak(f"Opening {query}")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                    
                # close app
                elif "close" in query:
                    from dictApp import closeAppWeb
                    closeAppWeb(query)
                    
                # alarms
                elif "alarm" in query:
                    set_alarm()
                    
                    
                # search and redirect to google
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                    
                # play on youtube
                elif "play" in query and "on youtube" in query:
                    from searchNow import playYoutube
                    playYoutube(query)
                    
                # search & redirect to youtube
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                    
                # customized playlist
                elif "tired" in query or "favourite song" in query:
                    speak("No worries boss, I have something for you")
                    songs = ["https://www.youtube.com/watch?v=-_5dLLUbXNc",
                             "https://www.youtube.com/watch?v=7KKVb0_IdD4",
                             "https://www.youtube.com/watch?v=D21Di3NXcYM",
                             "https://www.youtube.com/watch?v=7nDKFPWbJMU",
                             "https://www.youtube.com/watch?v=7JdEZoffm-Q"]
                    webbrowser.open(random.choice(songs))

                # games
                elif "game" in query:
                    play()
                    
                elif "joke" in query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                    print(joke)
                    
                # ss
                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("screenshot.png")
                    
                # click my photo
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("Smile!!")
                    pyautogui.press("enter")
                    
                # translate
                elif "translate" in query:
                    from translator import translate
                    query = query.replace("translate ","")
                    translate(query)
                
                # search & speak from wikipedia
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)
                      
                # tell time
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Boss, the time is {strTime}")

                # tell date
                elif "date" in query:
                    strTime = datetime.datetime.now().strftime("%d %B, %Y")
                    speak(f"Boss, the date is {strTime}")
                
                # pause video
                elif "stop" in query:
                    pyautogui.press("k")
                    speak("Video Paused boss")
                
                # play video
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video Playing boss")
                
                # mute video
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted boss")
                
                # unmute video
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Video unmuted boss")
                
                # volume up
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up boss")
                    volumeup()
                
                # volume down
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down boss")
                    volumedown()
                
                # change tab (ALT + TAB)
                elif "change tab" in query:
                    speak("Changing tab boss")
                    pyautogui.hotkey("alt", "tab")
                
                # change internal tabs (CTRL + TAB)
                elif "change internal tab" in query:
                    speak("Changing internal tab boss")
                    pyautogui.hotkey("ctrl", "tab")
                
                # remembering
                elif "remember that" in query:
                    rememberMsg = query.replace("remember that", "")
                    speak("Boss, You told me to remember that"+rememberMsg)
                    remember = open("remember.txt", "w")
                    remember.write(rememberMsg)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("Boss, you told me to remember that"+remember.read())
                    remember.close()
                
                # weather
                elif "weather" in query or "temperature" in query:
                    # api_key = "your api key"
                    # base_url = "http://api.openweathermap.org/data/2.5/weather?"
                    speak("Boss, what city do you want to know the weather for?")
                    city = takeCommand().lower()
                    temp = get_weather(city)
                    print(temp)
                    speak(temp)
                                    
                # news
                elif "news" in query:
                    latestNews()
                
                # calculate
                elif "calculate" in query:
                    query.replace("calculate","")
                    calc(query)
                    
                # wp msg
                elif "whatsapp" in query:
                    print("whatsapp messaging")
                    sendMessage()
                
                # schedule
                elif "schedule my day" in query:
                    speak("Okay Boss")
                    speak("Do you want clear old schedule? (reply with a yes or no)")
                    ans = takeCommand().lower()
                    if "yes" in ans:
                        file = open("schedule.txt", "w")
                        file.write("")
                        file.close()
                        speak("How many tasks you want to add?")
                        try:
                            num = int(takeCommand())
                            for i in range(num):
                                speak("Tell Task " + str(i+1) + " to enter:")
                                task = takeCommand()
                                file = open("schedule.txt", "a")
                                file.write(f"{i+1}. {task}\n")
                                file.close()
                            speak("That's it")
                        except:
                            speak("Invalid input")
                    elif "no" in ans:
                        speak("How many tasks you want to add?")
                        try:
                            num = int(takeCommand())
                            for i in range(num):
                                speak("Tell Task " + str(i+1) + " to enter:")
                                task = takeCommand()
                                file = open("schedule.txt", "a")
                                file.write(f"{i+1}. {task}\n")
                                file.close()
                            speak("That's it")
                        except:
                            speak("Invalid input")
                    
                elif "show my schedule" in query:
                    speak("Here is your schedule")
                    try:
                        message = open("schedule.txt", "r").read()
                        notification.notify(title = "Schedule", message = message, timeout = 10)
                    except:
                        speak("No schedule available")
                        
                elif "internet speed" in query or "speed test" in query:
                    speak("Checking internet speed")
                    wifi = speedtest.Speedtest()
                    download = wifi.download()/1048576
                    upload = wifi.upload()/1048576   # Bytes to MB
                    speak(f"Upload speed is {upload} MB/s")
                    print(f"Upload speed is {upload} MB/s")
                    speak(f"Download speed is {download} MB/s")
                    print(f"Download speed is {download} MB/s")
                
                # shutdown
                elif "shutdown" in query:
                    speak("Are you sure you want to shutdown?")
                    confirm = takeCommand().lower()
                    if confirm == "yes":
                        speak("Shutting down")
                        os.system("shutdown /s /t 1")
                    else:
                        speak("Okay, I won't shut down")
                    
        elif "bye" in query:
            speak("Goodbye, have a great day!")
            exit()