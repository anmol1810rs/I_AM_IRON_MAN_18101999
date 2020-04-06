import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("goodmorning anmol")
    elif hour>=12 and hour<18:
        speak("good afternoon anmol")
    else:
        speak("good evening anmol")

    speak("i am jarvis how may i help you")

def takeCommand():
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  #second before speaking audio
        audio = r.listen(source)

    try:
        print("Recognising")
        query=r.recognize_google(audio, language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        #  print(e)
        print("Say That Again Please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('96anmolmalhotra@gmail.com','XXXXWESEWDDAS')
    server.sendmail('96anmolmalhotra@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #logics and tasks to be executed
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Desktop\\songs'
            songs = os.listdir(music_dir)
            value=random.randint(0,1)
            os.startfile(os.path.join(music_dir, songs[value]))
            print(songs)

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,The Time is {strTime}")

        elif 'open code' in query:
            code_path = "G:\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'kaisa hai' in query:
            speak('badhiya, tum bataao!')

        
        elif  'email to dad' in query:
            try:
                speak("What should i say ?")
                content = takeCommand()
                to = "malhautraopticians@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend anmol bhai .I am tired Right Now .I need Some Sleep")
