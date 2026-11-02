# Josie.Weather
* Josie.Weather is a Python weather app that retrieves current weather conditions and daily forecast information for a city entered by the user. Josie.Weather also provides useful reminders and outfit suggestions based on the weather.
* Based on the forecast, Josie.Weather provides practical suggestions, including weather-based outfit suggestions, a reminder to bring an umbrella, and a reminder to use sunscreen and wear a hat when the uv is high.
 

## General Information
* I specifically chose this project challenge, because many of the decisions I make day-to-day are dependent on forecast weather, including what I'm going to wear, and what I’ll bring with me when I’m out of the house.
* I wanted to create an app that could help me save time in the morning and help me properly prepare for the upcoming daily weather as there have been many times that I have found myself trapped in torrential rain without an umbrella.The service responds with weather data in JSON format, and your program uses that data to display conditions and make recommendations.
* I have used the weather API WTTR.in to retrieve data , an open-source, “console-oriented weather forecast service” (chubin, 2015), that can be used without requiring the creation of an API key, and it doesn't require any payment.


## Dependencies
* My project uses the python library Requests, which allows me to easily send http requests, so I can retrieve data from the wttr.in web server in only a couple lines of code.
* I also created a VENV (virtual coding environment) to keep project packages separated, and to make sure I don't mess around with my system's python environment.


## Features 
### weather information:
* Current temperature in Celsius
* Humidity
* UV Index
* A description of the weather
* Current Moon phase
* Maximum and minimum temperature in Celsius
* The average temperature in Celsius
  
### Reminders:
* Clothing suggestions based on the maximum temperature and humidity
* An umbrella reminder when its raining or rain is nearby
* Reminder to bring a hat and wear sunscreen when UV is high
