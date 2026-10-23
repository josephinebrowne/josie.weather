import requests

#ask user for their city
city = input("Enter city name: ") 

# create a variable for the url, ?format=j1 returns structured json data 
url = f"https://wttr.in/{city}?format=j1"

# retrieve weather data from the wttr.in web server
# parse the json response into a python disctionary (Sarthakbcomp, 2026)
data = requests.get(url).json() # (Pythons Py, 2026)


# enter the "current_condition" section of the json output returned by wttr.in, and access the first item in the list 
condition = data["current_condition"][0]  # (Pythons Py, 2026)

# enter the weather section of the json response, so I can access weather forcasts, and access the first item
forecast = data["weather"][0]


# access individual values from the response, and store them in variables (Pythons Py, 2026)(Sarthakbcomp, 2026)
temp = condition["temp_C"] # return temperature in celcius and stor in in a variable
humidity = condition["humidity"] # humidity retrieves the humidity for current_condition and stores it in a variable
weather_code = condition["weatherCode"] # return a code relating to the current weather condition and store it in weather_code
uv = condition["uvIndex"] # return the current UV index


# access the average temp, and the minimum and maximum temp from the "weather" section of the json response (Borck, 2025)
maxtemp = forecast["maxtempC"]
mintemp = forecast["mintempC"]
average = forecast["avgtempC"]


# import a function from weathercodes.py that converts the numerical weather code into its corresponding description (Matthes, 2023, ch. 10)
from weathercodes import describe_weather 
# create a variable that applies the describe_weather function to the current weather code stored in weather_code.
weatherdes = describe_weather(weather_code) 


#import the umbrella_rec function from rain.py
from rain import umbrella_rec


# print the results: temp, weather and humidity 
print("🌡 Current Temparature for", city, ":", temp, "°C")
print("🌫 Humidity:", humidity, "%")
print("Weather:", weatherdes)
print("☀️ UV Index:", uv)

# print minimum and maximum temp
print("🔥 Maximum Temperature:", maxtemp, "°C,")
print("❄️ Minimum Temperature:", mintemp, "°C")

print("Average Temperature:" average, "°C")


# Convert strings into integers that can be understood in the if/else statement
uv = int(uv)
average = int(average)


# Give outfit suggestion based on the average daily temperature using an "if-elif-else Chain" (Matthes, 2023, ch. 5)
if average > 20:
   print("👗 Wear a short-sleeve top and skirt/shorts.")
elif average > 17:
   print("👕 Wear a 3/4-sleeve top, or short sleeve and bring a light cardigan")
elif average > 15:
   ("🧥 Wear a long-sleeve top and pants/tights.")
else:
   print("🧣 Wear a warm jacket and bundle up!")



# print 'bring an umbreella' if the current weather code is in the array of my chosen rain codes in rain.py
if umbrella_rec(weather_code):
    print("☔ Bring an umbrella.")



# print wear sunscreen if the uv index is over 7
if uv > 5:
   print("Wear Sunscreen.")
else:
   print("")
