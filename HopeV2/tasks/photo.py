from ecapture import ecapture as ec

def index():
    ec.capture(0,"Hope Cam","image.jpg")
    return "capturing photo"   
