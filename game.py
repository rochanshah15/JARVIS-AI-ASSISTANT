import pyttsx3
import speech_recognition
import random

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

def play():
    speak("Let's play a game")
    speak("You can choose from the following games")
    speak("1. Rock Paper Scissors")
    speak("2. Guess the Number")
    try:
        game = int(takeCommand())
        if game == 1:
            speak("Let's play Rock Paper Scissors")
            speak("You can choose from Rock, Paper, Scissors")
            user = takeCommand().lower()
            choices = ["rock", "paper", "scissors"]
            computer = random.choice(choices)
            speak(f"You chose {user}, computer chose {computer}")
            if user == computer:
                speak("It's a tie")
            elif user == "rock":
                if computer == "scissors":
                    speak("Rock smashes scissors, you win")
                else:
                    speak("Paper covers rock, you lose")
            elif user == "paper":
                if computer == "rock":
                    speak("Paper covers rock, you win")
                else:
                    speak("Scissors cuts paper, you lose")
            elif user == "scissors":
                if computer == "paper":
                    speak("Scissors cuts paper, you win")
                else:
                    speak("Rock smashes scissors, you lose")
        
        elif game == 2:
            speak("Let's play Guess the Number")
            speak("I'm thinking of a number between 1 and 100")
            speak("You have to guess the number")
            # max. 5 guess
            speak("After each guess, I'll tell you if the number is higher or lower")
            speak("You have 5 chances")
            number = random.randint(1, 100)
            guess = 0
            while guess < 5:
                speak("What's your guess?")
                user = takeCommand()
                try:
                    user = int(user)
                except:
                    speak("Invalid input, please enter a number")
                    continue
                guess += 1
                if user < number:
                    speak("The number is higher")
                elif user > number:
                    speak("The number is lower")
                elif user == number:
                    speak("You guessed the number in " + str(guess) + " guesses")
                    break
                if guess == 5 and user != number:
                    speak("You didn't guess the number, it was " + str(number))
                    break
    except:
        speak("Invalid input, please enter a number or a choice")