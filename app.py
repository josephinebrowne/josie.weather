import requests

# import some sun ascii art!
import sunsymbol

# ask user to type in their city
city = input("Welcome to Josie.Weather! Please enter your city: ") 

# create a variable for the url, ?format=j1 returns weather information in json format
url = f"https://wttr.in/{city}?format=j1"

# retrieve weather data from the wttr.in web server
# parse the json response object into a python disctionary (Sarthakbcomp, 2026)
data = requests.get(url).json() # (Pythons Py, 2026)


# enter the "current_condition" part of the dictionary for current weather
condition = data["current_condition"][0]  # (Pythons Py, 2026)

# enter the weather section of the dictionary, so I can get weather forcasts
forecast = data["weather"][0]


# access individual values from the response, and store them in variables (Pythons Py, 2026)(Sarthakbcomp, 2026)
temp = condition["temp_C"] 
humidity = condition["humidity"] 
weather_code = condition["weatherCode"] 
uv = condition["uvIndex"] 

# access the average temp, and the minimum and maximum temp from the "weather" section of the json response (Borck, 2025)
maxtemp = forecast["maxtempC"]
mintemp = forecast["mintempC"]
average = forecast["avgtempC"]
moon = forecast["astronomy"][0]["moon_phase"]


# import a function from weathercodes.py that converts the numerical weather code into its corresponding description (Matthes, 2023, ch. 10)
from weathercodes import describe_weather 

# create a variable that applies the describe_weather function to the current weather code
weatherdes = describe_weather(weather_code) 


#import the umbrella_rec function from rain.py
from rain import umbrella_rec


# print the results: temp, weather and humidity 
print("🌡️ Current Temparature for", city, ":", temp, "°C")
print("💧 Humidity:", humidity, "%")
print("🌦️ Weather Description:", weatherdes)
print("☀️ UV Index:", uv)


# create a variable for the moon icon that changes based on the moon phase
if moon == "New Moon":
   moonicon = ("🌑")

if moon == "Waxing Crescent":
   moonicon = ("🌒")

if moon == "First Quarter":
   moonicon = ("🌓")

if moon == "Waxing Gibbous":
   moonicon = ("🌔")

if moon == "Full Moon":
   moonicon = ("🌕")

if moon == "Waning Gibbous":
   moonicon = ("🌖 ")

if moon == "Last Quarter":
   moonicon = ("🌗")
   
if moon == "Waning Crescent":
   moonicon = ("🌘")


# print out the moon phase with the icon
print("Moon Phase:", moon, moonicon)

# print minimum and maximum temp
print("🔥 Maximum Temperature:", maxtemp, "°C,")
print("❄️ Minimum Temperature:", mintemp, "°C")
print("Average Temperature:", average)



# Weather-based Reccomendations

# Convert strings into integers that they can be understood in the if/else statement
uv = int(uv)
maxtemp = int(maxtemp)
humidity = int(humidity)


# Give outfit suggestion based on the maximum daily temperature using an "if-elif-else Chain" (Matthes, 2023, ch. 5)
if maxtemp > 20 or humidity > 60:
   print("👗 Wear a short-sleeve top and skirt/shorts.")
elif maxtemp > 17:
   print("👕 Wear a 3/4-sleeve top, or a short sleeve and bring a light cardigan.")
elif maxtemp > 15:
   print("🧥 Wear a long-sleeve top and pants/tights.")
else:
   print("🧣 Wear a warm jacket and bundle up!")


# print 'bring an umbreella' if the current weather code is in the array of my chosen rain codes in rain.py
if umbrella_rec(weather_code):
    print("☔ Bring an umbrella.")
else:
   print("No umbrella needed")


# print wear sunscreen if the uv index is over 5
if uv > 5:
   print("⛱️ Wear sunscreen and a hat.")
else:
   print("")


