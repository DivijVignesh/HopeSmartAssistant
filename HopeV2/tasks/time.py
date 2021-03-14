import datetime
def index():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    print(strTime)
    return strTime
