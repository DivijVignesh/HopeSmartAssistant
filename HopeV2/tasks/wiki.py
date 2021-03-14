import wikipedia
import requests
def wiki(query):
    if "search about" in query:
        query=query.replace("search about" ,"")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2) 
    return results