#It understand whatever the humans speak and converts the speech to text.
import speech_recognition as sr 
#This package supports text to speech engines on Mac OS x, Windows and on Linux.
import pyttsx3
#This is an inbuilt module in python and it works on date and time.
import datetime
#This package in python extracts data required from Wikipedia.
import wikipedia
#This is an in-built package in python. It extracts data from the web.
import webbrowser
#This module is a in python and it provides the function to interact with operating system.
import os
#The time module helps us to display time.
import time
#This is a standard library use to process various system commands. 
import subprocess
#Wolfram Alpha is used to compute expert-level answers.
import wolframalpha
#The json module is used for storing and exchanging data.
import json
#The request module is used to send all types of HTTP request.
import requests


print('Loading your AI personal assistant - Steve ')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

#Speak function converts text to speech.
def speak(text):
    engine.say(text)
    engine.runAndWait()
#wishMe function is used by AI assistant to greet the user according to time.
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
#takecommand function is used by AI assistant to understand and to accept human language. 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            #recognize_google function uses google audio to recognize speech.
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Steve")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        #To take input from the user and perform the function accordingly.
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak('your personal assistant Steve is shutting down,Good bye')
            print('your personal assistant Steve is shutting down,Good bye')
            break


#This module of code is used to extract information from wikipedia.
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
#This module of the code helps to open youtube.
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
#This module of the code helps to open google.
        elif 'open google' in statement or "google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
#This module of the code helps to open gmail.
        elif 'open gmail' in statement or "gmail" in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
#This module of the code helps to predict the weather.
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


##This module of the code helps to know the current time.
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
#This module of the code helps the user know functionalities of steve.
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Steve version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

##This module of the code tells the user who is developer of the program.
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Sir Prakhar Saxena and Pranjali Ma'am")
            print("I was built by Mr. Prakhar Saxena & Ms. Pranjali Jain")
##This module of the code helps to open stackoverflow.
        elif "open stackoverflow" in statement or "stackoverflow" in statement :
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
#This module of the code keep the user updated about the news.
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
#This module of the code helps the user to click the photo(but currently library is not available)
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")
##This module of the code helps to search anything on web browser.
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
#This module of the code helps to answer computational, mathematical and geographical questions.
        elif 'ask' in statement or "what" in statement or "who" in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
#This module of the code helps steve to write the notes that has been dictated by the user.

            
        elif "write a note" in statement or "write" in statement: 
            speak("What should i write, sir") 
            note = takeCommand() 
            #Kindly change the file path as per the requiremnet.
            file = open('C:\\Users\\prakh\\Desktop\\notes.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
#This module of the code helps steve to show the notes that were dictated by the user.              
        elif "show note" in statement: 
            speak("Showing Notes") 
            #Kindly change the file path as per the requiremnet.
            file = open("C:\\Users\\prakh\\Desktop\\notes.txt", "r") 
            print(file.read()) 
            speak(file.read(6))     
            
            
            
#This module of the code helps steve to perform system commands.         

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)