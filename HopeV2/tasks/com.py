import webbrowser
def index(query):
    results=findinglink(query)
    return results

def findinglink(query):
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    res=query.split()
    link= filter(lambda a: '.com' in a, res)
    # Convert the filter object to list
    url1=''
    for ele in link:  
        url1 += ele
    webbrowser.get(chrome_path).open(f"https://www.{url1}")

    return (f"Opening {url1}")        
        