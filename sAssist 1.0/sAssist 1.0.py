# Modules

import pyaudio, pyttsx3, speech_recognition as sr, random, os, sys, datetime, webbrowser, time, socket

import pyaudio, pyttsx3, speech_recognition as sr, random, os, sys, datetime, wikipedia, webbrowser, time, socket

from colorama import Fore, Back, Style
# Information
version = '1.0'
mode = 'Audio'

# To Get Info about the user
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
username = os.getlogin()

# Voice Engine For Speaking
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)


# Functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def speech_to_text():
    while True:
            # This takes microphone input from the user and returns string output
        r = sr.Recognizer()

        with sr.Microphone() as source:
            speak("Listening")
            print("\nListening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            speak("Recognizing")
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    
def wikipediafunc(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

    
# Banner
print(Fore.GREEN + '''             
                     ____ ____ ____ ____ _ ____ ___ 
                     [__  |__| [__  [__  | [__   |  
                     ___] |  | ___] ___] | ___]  |   
            ''')

# Normal Details
print(Fore.RED + "Version       [>] " + Fore.WHITE + version)
print(Fore.MAGENTA + "Mode          [>] " + Fore.WHITE + mode)
print(Fore.YELLOW + "Hostname      [>] " + Fore.WHITE + os.getlogin()) 
print(Fore.GREEN + "IP Address    [>] " + Fore.WHITE + ip_address)
print(Fore.CYAN  + "Your Username [>] " + Fore.WHITE + username + Fore.WHITE)

if __name__ == "__main__":
    while True:
        # Taking Input from the user
        query = speech_to_text().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
        
        elif 'play music' in query:
            music_dir = '\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time now' == query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"The Time Is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\"+ getlogin() +"\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open edge' in query:
            edgepath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(edgepath)
        elif 'open chrome' in query:
            chromepath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
            os.startfile(chromepath)
