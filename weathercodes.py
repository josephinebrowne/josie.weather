# WorldWeatherOnline (n.d.) Condition Code Reference

# create a dictionary containing the "weatherCode values [...] and their corresponding English descriptions" (WorldWeatherOnline, n.d.)
weathercodelist = {
    113: "Sunny / Clear",
    116: "Partly Cloudy",
    119: "Cloudy",
    122: "Overcast",
    143: "Mist",
    176: "Patchy rain nearby",
    179: "Patchy snow nearby",
    182: "Patchy sleet nearby",
    185: "Patchy freezing drizzle nearby",
    200: "Thundery outbreaks in nearby",
    227: "Blowing snow",
    230: "Blizzard",
    248: "Fog",
    260: "Freezing fog",
    263: "Patchy light drizzle",
    266: "Light drizzle",
    281: "Freezing drizzle",
    284: "Heavy freezing drizzle",
    293: "Patchy light rain",
    296: "Light rain",
    299: "Moderate rain at times",
    302: "Moderate rain",
    305: "Heavy rain at times",
    308: "Heavy rain",
    311: "Light freezing rain",
    314: "Moderate or heavy freezing rain",
    317: "Light sleet",
    320: "Moderate or heavy sleet",
    323: "Patchy light snow",
    326: "Light snow",
    329: "Patchy moderate snow",
    332: "Moderate snow",
    335: "Patchy heavy snow",
    338: "Heavy snow",
    350: "Ice pellets",
    353: "Light rain shower",
    356: "Moderate or heavy rain shower",
    359: "Torrential rain shower",
    362: "Light sleet showers",
    365: "Moderate or heavy sleet showers",
    368: "Light snow showers",
    371: "Moderate or heavy snow showers",
    374: "Light showers of ice pellets",
    377: "Moderate or heavy showers of ice pellets",
    386: "Patchy light rain in area with thunder",
    389: "Moderate or heavy rain in area with thunder",
    392: "Patchy light snow in area with thunder",
    395: "Moderate or heavy snow in area with thunder",
}


# Define a function that returns the weather description (value) for the numerical weather code (key)
# when describe_weather(weather_code) is run in app.py, it assigns 'code' the value of the current numerical weather code

def describe_weather(code): # code represents a key in the weathercodelist dictionary, eg "113"
    code = int(code)   # int() makes sure the key is returned as an integer
    return weathercodelist.get(code)  
    
# .get() "returns the value associated with a given key" (GeeksforGeeks, 2026a)
# returns the corresponding value for the weather code returned from app.py from the weathercodelist dictionary (Matthes, 2023, ch. 6)



