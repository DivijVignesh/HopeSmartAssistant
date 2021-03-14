import datetime
def index():
    hour = int(datetime.datetime.now().hour)
    str=""
    if hour>=0 and hour<12:
        str="Good morning"
    elif hour>=12 and hour<18:
        str = "Good Afternoon"
    elif hour>=18 and hour<23:
        str="Good Evening"
    else:
        str="Good Night"    

    str= str + "What can i do for you?"
    return str