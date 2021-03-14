import requests

def index():

    api_key="5c6c369abeb5bee9f76229a09a750098"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    # speak("what is the city name")
    city_name='Visakhapatnam'    #takeCommand()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature in kelvin unit = " +
                str(current_temperature) +
                "\n humidity (in percentage) = " +
                str(current_humidiy) +
                "\n description = " +
                str(weather_description))   
        return (" Temperature in kelvin unit is " +
                str(current_temperature) +
                "\n humidity (in percentage) of " +
                str(current_humidiy) +
                "\n and is mostly " +
                str(weather_description)  )      