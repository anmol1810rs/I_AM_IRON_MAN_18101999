import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from twilio.rest import Client
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Say
from sys import exit

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

    speak("i am odin, you are just like my son, thor, so, how can i help you")

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
    server.login('96xxxil.com','#password')
    server.sendmail('96xxxil.com', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #logics and tasks to be executed
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("what should i open on youtube")
            content=takeCommand()
            webbrowser.open("https://www.youtube.com/results?search_query="+content)
        
        elif 'open google' in query:
            speak("what should i open in google")
            content=takeCommand()
            webbrowser.open("https://www.google.com/search?q="+content+"&rlz=1C1OKWM_enIN895IN896&oq="+content+"&aqs=chrome..69i57j0l7.3322j0j8&sourceid=chrome&ie=UTF-8")
        
        elif 'open music online' in query:
            speak('what do you want to play')
            content=takeCommand()
            webbrowser.open('https://music.youtube.com/watch?v='+content+'&feature=share')

        elif 'buy' in query:
            speak('i feel, amazon is a great sight to buy products, what do you want to buy')
            content=takeCommand()
            speak('give me a second Anmol!')
            webbrowser.open("https://www.amazon.in/s?k="+content+"&ref=nb_sb_noss_2")

        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Desktop\\songs'
            songs = os.listdir(music_dir)
            value=random.randint(0,1)
            os.startfile(os.path.join(music_dir, songs[value]))
            print(songs)

        elif 'who is pratyush' in query:
            speak("He is that guy who, ate fuckinnnnnnng 20 momos in one go!!!!")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,The Time is {strTime}")
            speak('Tick, Tock, Tick, Tock')

        elif 'open code' in query:
            code_path = "G:\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'thanks a lot' in query:
            speak('haha, i am happy now!')

        elif 'say hi to my friend' in query:
            speak("anmol, what is your friends name")
            content=takeCommand()
            speak("Hey, "+content+", hope you are doing great")


        elif 'open netflix' in query:
            webbrowser.open('xxxxxx-4913-a5a1-21be8b85efd1-30330052xxxxxxxx23083602X3XX1586150276788%2C19595478-04cf-4968-ac5d-e5e254a2838a_ROOT')
       
        elif  'email my friend' in query:
            try:
                speak("What should i say ?")
                content = takeCommand()
                to = "axxxx.chaxxxxxx.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend anmol bhai .I am tired Right Now .I need Some Sleep")
        
        elif 'whatsapp' in query:
            client = Client("#client_id","#auth_id")
            from_whatsapp_number='whatsapp:+14xxxxxxx6'
            to_whatsapp_number='whatsapp:+91xxxxxx3'
            speak("whom should i send a whatsapp to")
            name=takeCommand()
            speak('what should i send to, '+name)
            content=takeCommand()
            speak('message sent')
            client.messages.create(body=content, from_=from_whatsapp_number,
                                    to=to_whatsapp_number)

        elif  'good night' in query:
            speak('good night anmol, i was really tired to be honest, haha')
            exit(0)
            

        
        
      

            