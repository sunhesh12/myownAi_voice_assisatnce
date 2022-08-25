

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import os
import webbrowser as wb
import wikipedia
import subprocess
import pyjokes
from time import sleep
import pyautogui   # pip install PyAutoGUI

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 140
engine.setProperty('rate', voicespeed)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 or 0
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please..")

        return "---"
    return query

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)

def date():
    year  = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date  = int(datetime.datetime.now().day)

    speak("the current date is")
    speak(year)
    speak(month)
    speak(date)

def wishme():
    speak("welcome to jaavas ")
    print("welcome to jaavas ")
    time()
    print(time)
    date()
    print(date)
    hour = datetime.datetime.now().hour

    if hour >=6 and hour <= 12:
        speak("Good morning")
        print("Good morning")
    elif hour>=12 and hour <= 15:
        speak("Good afternoon")
        print("Good afternoon")
    elif hour>=15 and hour <= 20:
        speak("Good evening")
        print("Good evening")
    else:
        speak("Good night")
        print("Good night")


    speak("sir how can i help u?")

#open chhrome/website
def open_chrome():
    # url u want to open
    url = 'https://www.google.com/'

    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # replace chrome_path with the correct path for your platform."
    wb.get(chrome_path).open(url)


if __name__ == "__main__":

        wishme()

        while True:
            query = takeCommand().lower()  # take command in queary
            print(query)

            if "time" in query:  # quit to end the program
                time()

            elif "date" in query:  # if date in query than assistance will say time
                date()

            elif "offline" in query:  # quit to end the program
                speak("going offline")
                quit()

            elif "open chrome" in query:
                speak("chrome opening...")
                open_chrome()

             #wikipeadia seach
            elif "wikipedia" in query:
                speak("searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(result)
                print(result)

            #chrome search
            elif "search" in query:
                speak("what should i search?")
                search = takeCommand().lower()
                wb.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                       ).open_new_tab(search + ".com")
            # launch aplication
            elif "open notepad" in query:
                speak("opening notepad")
                location="C:/WINDOWS/system32/notepad.exe"
                notepad =subprocess.Popen(location)

            elif "close notepad" in query:
                speak("closing notepad")
                # noinspection PyUnboundLocalVariable
                notepad.terminate()

            elif "open WhatsApp" in query:
                speak("opening notepad")
                location = "C:/WINDOWS/system32/notepad.exe"
                notepad = subprocess.Popen(location)

            elif "close notepad" in query:
                speak("closing notepad")
                # noinspection PyUnboundLocalVariable
                notepad.terminate()

            #randome jokes
            elif "joke" in query:
                speak(pyjokes.get_jokes())

            #logout/restart/shutdown
            elif "log out" in query:
                speak("Loging out in 5 second")
                sleep(5)
                os.system("shutdown - l")

            elif "shutdown" in query:
                speak("shoutting down in 5 second")
                sleep(5)
                os.system("shutdown /s /t 1")

            elif "reatart" in query:
                speak("restarting in 5 second")
                sleep(5)
                os.system("shutdown /r /t 1")

            #<---------------PYAUTOGUI FEATURES--------------->
            elif "hidden menu" in query:
                #win+x = open the hidden menu
                 pyautogui.hotkey('winleft', 'x')

            elif "task manager" in query:
                #ctrl+shift+Esc = open the task manager
                 pyautogui.hotkey('ctrl', 'shift', 'Esc')

            elif "task view" in query:
                #win+tab:open the task view
                 pyautogui.hotkey('winleft','tab')

            elif "take a screenshot" in query:
                 #win+prt sc
                 pyautogui.hotkey('winleft', 'prtscr')
                 speak("done")

           #elif "snip" or "nip" in query:
               # pyautogui.hotkey('winleft', 'shift', 's')

            elif "close the app" in query:
                pyautogui.hotkey('winleft', 'i')

            elif "new virtual desktop" in query:
                pyautogui.hotkey('winleft', 'ctrl', 'd')






takeCommand()







