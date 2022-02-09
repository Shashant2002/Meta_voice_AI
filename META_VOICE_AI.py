from socket import if_nameindex
from threading import main_thread


from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")


    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am META Sir, How may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... :)")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("User said: " + query)
    except Exception as e:
        print(e)

        print("Say that again please..:(")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('metavoiceai@gmail.com', 'metavoiceai@gmail.com')
    server.sendmail('metavoiceai@gmail.com', 'metavoiceai@gmail.com',
                    'Hello, my name is META ,I am a personalised AI working for Mr.Legend')
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak(' Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\shash\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[67]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is :" + strTime)
        elif 'open f1' in query:
            path = '"C:\\Users\\shash\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\F1_2018.lnk"'
            os.startfile(path)
        elif 'write an email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "metavoiceai@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry, unable to send email +_+")
