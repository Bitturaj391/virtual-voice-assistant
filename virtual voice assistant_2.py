import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    username =("Aaryabhatta 1 point o")
    speak("I am your Assistant")
    speak(username)
    speak("made by the Team Aaryabhatta")
def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    usrname()
    while True:
         
        query = takeCommand().lower()
        if 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = ""
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            speak(datetime.datetime.now().strftime('%I:%M%p'))
            print(datetime.datetime.now().strftime('%b-%d-%G-%I:%M%p'))
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("Aaryabhatta")
            print("My friends call me Aaryabhatta")
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        elif "why you came to world" in query:
            speak("Thanks to Team Aaryabhatta, who had made me to assist you")
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Aaryabhatta Camera ", "img.jpg")
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        elif 'weather' in query:
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        elif "i love you" in query:
            speak("sorry, i am already commited to Bittu")   
        elif 'exit' in query:
            speak("Thanks for giving me your time, i Hope you are satisfied with my work")
            exit()
        elif 'thank you' in query:
            speak("you are  most welcome, I hape you are satisfied with my work")
            exit()        