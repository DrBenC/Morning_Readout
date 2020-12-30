from pygooglenews import GoogleNews
import pyttsx3
import time
import datetime
import requests
import json
import random

def r(list):
    return (list[random.randint(0, len(list)-1)])

#starts up a text-to-speech engine
engine = pyttsx3.init()

#sorts out today in a nice format
now = datetime.datetime.now()
c_time = now.strftime("%H %M")
day=now.strftime("%A")
date = now.strftime("%B  %d")

#decides what to call the listener
part_1 = ["Now then", "Alright then", "Let's see"]
part_2 = ["Handsome", "Gorgeous", "Fuckface", "Dickhead", "Sunshine", "Boss", "Chief"]

if int(c_time[0:1]) < 12:
    part_1.append("Good morning")
if int(c_time[0:1])  > 18:
    part_1.append("Good Evening")
    
address_human_as = str(r(part_1)+" "+r(part_2))

#addresses listener and reads the time
engine.say(address_human_as)
output=("It is "+str(c_time)+" on "+str(day)+" "+str(date))
engine.say(str(output))


#this connects to openweather and collects the local data (for York - can change the 7 digit code after id to change city
api_key = "a27b4d09a4832f7bbe8af8a437e9216f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = "http://api.openweathermap.org/data/2.5/weather?id=2633352&appid=a27b4d09a4832f7bbe8af8a437e9216f"

response = requests.get(complete_url)
x = response.json()

temperature_data=(x["main"]["temp"])
(temperature_data)-=273.15
temperature = "{:.1f}".format(temperature_data)
weather_data = (x["weather"][0]["main"])
wind_data = "{:.1f}".format(x["wind"]["speed"]*2.23694)

#reads out the weather to you
weather_output=("It is "+str(weather_data)+" outside at "+str(temperature)+" celsius with "+str(wind_data)+" mile per hour wind.")
engine.say(weather_output)

#then we connect to Google news
gn = GoogleNews()

engine.say("Today's headlines are as follows: ")

top = gn.geo_headlines("United Kingdom")

#I know I could probably optimise this better but I can't be bothered, it's 3am
for n in range(1,3):
    headline=(top["entries"][n]["title"])
    engine.say(headline)
    time.sleep(0.5)

world= gn.topic_headlines("World")
engine.say(world["entries"][0]["title"])

world= gn.topic_headlines("World")
engine.say(world["entries"][1]["title"])

science = gn.topic_headlines("Science")
engine.say(science["entries"][0]["title"])

business = gn.topic_headlines("Business")
engine.say(business["entries"][0]["title"])

engine.say("Good luck, try to be good")

engine.runAndWait()

