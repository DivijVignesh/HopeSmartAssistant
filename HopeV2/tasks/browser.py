import os
import webbrowser
def index(tag,query):

    if tag=='mail':
        results=mail()
    elif tag=='discord':
        results=discord()
    elif tag=="youtube":
        results=youtube()    
    elif tag=="google":
        results=google(query)    
    return results

def mail():
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open("https://www.gmail.com")  
    return "Opening Gmail"

def discord():
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open("https://www.discord.com")
    return "opening discord"

def youtube():
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open("https://www.youtube.com")
    return "opening youtube"

def google(query):
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" 
    webbrowser.get(chrome_path).open(f"https://www.google.com/search?q={query}")    
    return ("Opening.... ")   