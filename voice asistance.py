import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from AppOpener import open
from googlesearch import search
import pywhatkit as pwt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 16:
        speak("good afternoon")
    elif hour >= 16 and hour <= 23:
        speak("good evening")
    else:
        speak("good night")
    speak("hello I am Tanmay your personal A.I. assistant ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hearing")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing your commands....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again")
        return "None"
    return query

def googsearch(querry):
    for i in search(querry, tld="com", num=10, stop=10):
        print(i)


def ytsearch(querry):
    speak("here is your video")
    pwt.playonyt(querry)


def opengoogle(querry):
    speak("here are your search results")
    pwt.search(querry)


wishMe()
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('searcching Wiki')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("Wikipedia says")
        speak(results)
        print(results)
    elif 'stop' in query:
        speak("thank you for using tanmay")
        break
    elif 'open youtube' in query:
        webbrowser.open('http://www.youtube.com')
    elif 'open google' in query:
        webbrowser.open('http://www.google.com')
    elif 'result' in query:
        googsearch(query)
    elif 'search' in query:
        opengoogle(query)
    elif 'play' in query:
        ytsearch(query)
    elif 'open twitter ' in query:
        webbrowser.open('http://www.twitter.com')
    elif 'open map' in query:
        webbrowser.open('https://www.google.com/maps')
    elif 'open gmail' in query:
        webbrowser.open('https://mail.google.com/mail/')
    elif 'open github' in query:
        webbrowser.open('https://github.com/')
    elif 'open stackoverflow' in query:
        webbrowser.open('https://stackoverflow.com/')
    elif 'music' in query:
        music_dir = 'D:\\arnav all\\pai porject\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'time' in query:
        strt = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"the time is {strt}")
    elif 'open code' in query:
        codePath = '"C:\\Users\\91995\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"'
        os.startfile(codePath)
    elif 'gta' in query:
        gtapath = 'com.epicgames.launcher://apps//0584d2013f0149a791e7b9bad0eec102%3A6e563a2c0f5f46e3b4e88b5f4ed50cca%3A9d2d0eb64d5c44529cece33fe2a46482?action=launch&silent=true'
        os.startfile(gtapath)
    elif 'open canva' in query:
        canvapath = 'C:\\Users\\91995\\AppData\\Local\\Programs\\Canva\\Canva.exe'
        os.startfile(canvapath)
    elif 'open desk' in query:
        daskpath = "D:\\Samsung DeX\\SamsungDeX.exe"
        os.startfile(daskpath)
    elif 'epic game' in query:
        epicpath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
        os.startfile(epicpath)
    elif 'whatsapp' in query:
        open("whatsapp")
    elif 'game' in query:
        open("forza motorsports 6 apex", match_closest=True)
    elif 'app store' in query:
        open("Microsoft Store", match_closest=True)
    elif 'edge' in query:
        open("Microsoft Edge", match_closest=True)
    elif 'terminal' in query:
        open("Microsoft Terminal", match_closest=True)
    elif 'word' in query:
        open("Microsoft Word", match_closest=True)
    elif 'powepoint' in query:
        open("Microsoft Powepoint", match_closest=True)
    elif 'excel' in query:
        open("Microsoft Excel", match_closest=True)
    elif 'calendar' in query:
        open("Microsoft Calendar", match_closest=True)
    elif 'shutdown' in query:
        shutdown = input(
            "Do you wish to shutdown your computer ? (yes / no): ")
        if shutdown == 'no':
            exit()
        else:
            os.system("shutdown /s /t 1")

    # elif 'send email'  in query:
    #     try:
    #         speak("what to write ??")
    #         content=takeCommand()
    #         to="arnavbhatia2003@gmail.com"
    #         sendEmail(to,content)
    #         speak("email sent ")
    #     except Exception as e:
    #         print(e)
    #         speak("sorry! email could not be sent")
