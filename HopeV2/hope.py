import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser 
import wolframalpha
import os,sys,string,winsound
import subprocess
import re
from ecapture import ecapture as ec
import json
import requests
import hopeChatBot #userdefined 
from tasks import wiki,weather,time,wishme,vscode,browser,photo,com,wolf


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[0])
engine.setProperty('voice', voices[0].id)
winsound.Beep(500,100)
def speak(audio):
  engine.say(audio)

  engine.runAndWait()  # Without this command, speech will not be audible to us.



def takeCommand():
     #takes VOICE input via microphone and returns voice to text converted note
     r = sr.Recognizer()
     with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 5)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("after audio")
     try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

     except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
     return query    


    
 
               
if __name__ == "__main__":
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"  #chrome path should be pasted over here depending on your chrome app location in your local device
    while True:
        if True:
            # winsound.Beep(500,200)
            query = takeCommand().lower() #Converting user query into lower case
            # Logic for executing tasks based on query
            if 'turn' and 'temperature sensor' in query:
                if 'on' in query:
                    r=requests.post("https://api.thingspeak.com/update?api_key=ApiKeyHere&field1=1")     #paste your api key here
                    speak("turning on")
                elif 'off' in query:
                    r=requests.post("https://api.thingspeak.com/update?api_key=ApiKeyHere&field1=0")   #paste your api key here
                    speak("turning off")
                print(r)
                continue    
            if 'turn' and 'current sensor' in query:
                if 'on' in query:
                    r=requests.post("https://api.thingspeak.com/update?api_key=ApiKeyHere&field1=1")   #paste your api key here
                    speak("turning on")
                elif 'off' in query:
                    r=requests.post("https://api.thingspeak.com/update?api_key=ApiKeyHere&field1=0")   #paste your api key here
                    speak("turning off")
                print(r)
                continue          
            if query=="none":
                continue
            ints , res=hopeChatBot.index(query)
            tag=ints[0]['intents']
            speak(res)
            if tag=="wikipedia":
                results=wiki.wiki(query)
                speak("According to Wikipedia:")
                print(results)
                speak(results)
            elif tag=="weather":
                results=weather.index()
                speak(results)  
            elif tag=="time":
                results=time.index()
                speak(results)
            elif tag=="greetings":
                #do nothing because already the response from the intenst json file is getting printed
                print(" ")
            elif tag=="wishme":
                results=wishme.index()
                speak(results)    
            elif tag=="goodbye":
                speak("bye")
                winsound.Beep(500,100)
                break
            elif tag=="vscode":
                results = vscode.index()
                speak(results)    
            elif tag== "mail":
                results = browser.index(tag,query)
                speak(results)
            elif tag== "discord":
                results = browser.index(tag,query)
                speak(results)
            elif tag== "youtube":
                results = browser.index(tag,query)
                speak(results)
            elif tag== "photo":
                results = photo.index()
                speak(results)       
            elif tag=="com":
                results= com.index(query)
                speak(results)
            elif tag=="google":
                query=query.replace("search","")
                results= browser.index(tag,query)
                speak(results)
            elif tag=="wolf":
                results= wolf.index(query)
                speak(results)
  
            if 'who created you' in query:
                speak("i was created by my good friend E D V")    

