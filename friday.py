import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import requests 
from bs4 import BeautifulSoup
import webbrowser
import os 
import smtplib
from wikipedia.wikipedia import search
from requests import get



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',220)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

       
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!") 

    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 

    else:
        speak("Good Evening!") 

        
    speak(" hi I am A I friday sir. please tell me how may I help youu  Sir")  

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio)
        print(query) 

    except Exception as e:
        #print(e)

        print("Say that again  please....")
        return "None"
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vinaykumar05111978@gmail.com', 'Anish@2003')
    server.sendmail('vinaykumar05111978@gmail.com', to, content)
    server.close()    


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia....')
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
            music_dlr = 'D:\\Favourite Songs'
            songs = os.listdir(music_dlr)
            print(songs)
            os.startfile(os.path.join(music_dlr,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")  
            print(f"Sir, the time is {strTime}") 

        elif 'ip address' in query:
             ip = get('https://api.ipify.org').text
             speak(f"your ip address is {ip}") 
             print (f"your ip address is {ip}") 

        elif 'search on google' in query:
            speak("sir,what can i search on google for you")
            cm =takeCommand().lower()
            webbrowser.open(f"{cm}")
             
         

       

        elif 'email to anish' in query:

            try :
                speak("What should I say?")
                content = takeCommand()
                to = "anishkaran15@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")    

        elif 'temperature' in query:
            search = "temperature in Chandigarh"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div" , class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")

        