# Josie.Weather
* Josie.Weather is a Python weather app that retrieves the current weather conditions and daily forecast information for a city entered by the user. 
* My program provides practical reminders and suggestions, including weather-based outfit suggestions, a reminder to bring an umbrella, and a reminder to use sunscreen and wear a hat when the uv is high.
  
## General Information
* I specifically chose this project challenge, because many of the decisions I make day-to-day are dependent on forecast weather, including what I'm going to wear, and what I’ll bring with me when I’m out of the house.
* I wanted to create an app that could help me save time in the morning and help me properly prepare for the upcoming daily weather as there have been many times that I have found myself trapped in torrential rain without an umbrella.
* The service responds with weather data in JSON format, and I use that data to display conditions and make recommendations.
* I have used the weather API WTTR.in to retrieve data , an open-source, “console-oriented weather forecast service” (chubin, 2015), that can be used without requiring the creation of an API key, and it doesn't require any payment.

## Dependencies
* My project uses the python library Requests, which allows me to easily send http requests, so I can retrieve data from the wttr.in web server in only a couple lines of code.
* I also created a VENV (virtual coding environment) to keep project packages separated, and to make sure I don't mess around with my system's python environment.

## Features 
* Input option for users to enter their city
* Current temperature in Celsius
* Humidity
* UV Index
* A description of the weather
* Current Moon phase
* Maximum and minimum temperature in Celsius
* The average temperature in Celsius
* Clothing suggestions based on the maximum temperature and humidity
* An umbrella reminder when its raining or rain is nearby
* Reminder to bring a hat and wear sunscreen when UV is high

## Improvements
* When creating the outfit recommendations I wanted it to be as accurate to the weather as possible, however, by basing the recommendations off the current weather, if I check josie.weather in the morning, as I usually do, the recommendations don’t account for the temperature rising, and I would get too warm.
* I have settled on using the maximum temperature for the outfit recommendations, however this is still not entirely accurate. If, for example, I wanted to go out after the temperature drops in the evening, I'd get a clothing recommendation that wouldn’t apply to the current weather.
 
* Originally I pitched josie.weather as a graphical user interface (GUI), where users can interact with the app by clicking buttons in a window, which I would’ve achieved by using the Tkinter python library.
* Instead Josie.Weather is a command line interface (CLI) which requires users to type in commands and only generates text. With more time i would've made Josie.weather a GUI, however after I completed the core functionality of my app, I felt like I didn’t realistically have enough time to learn, and successfully turn my CLI into a Tkinter app. 

## References
### Josie.Weather is inspired by the following projects
Choudhary, M. (2026, February 2). Python fundamentals: Building a weather app with APIs. Medium. https://medium.com/@maeydhaw/python-fundamentals-building-a-weather-app-with-apis-34536395833d
Flyhigh Tutorials. (2025, November 14). 🌤️ Free: Live weather in 3 lines! (No API key needed!) #Python #coding #programming #tech #weather [Video]. YouTube. https://www.youtube.com/shorts/BbpUBW8Jsaw
Pythons Py. (2026, July 4). Python py day 15/100 simple python weather app 🌍 | using the requests library and the wttr.In API to fetch [Video]. Facebook. https://www.facebook.com/61590496301949/videos/1850288289689044/
Rawat, A. (2021, June 11). Forecast weather using python. DEV Community. https://dev.to/ayushi7rawat/forecast-weather-using-python-896
Sarthakbcomp. (2026, October 3). Building a weather API client in python: When your code starts talking to the sky. Medium. https://medium.com/@sarthakb25comp/building-a-weather-api-client-in-python-when-your-code-starts-talking-to-the-sky-f1a8467ce588

### I used these sources / documentation
Chubin, I. (2015). GitHub - chubin/wttr.In: :Partly_sunny: The right way to check the weather - One Line Output. GitHub. https://github.com/chubin/wttr.in
Cotton, R. (2022). Python cheat sheet for beginners. In Datacamp.com. DataCamp. https://www.datacamp.com/cheat-sheet/getting-started-with-python-cheat-sheet
GeeksforGeeks. (2025a). Response.Text python requests. GeeksforGeeks. https://www.geeksforgeeks.org/python/response-text-python-requests/
GeeksforGeeks. (2025b, January 20). Weather app in python using tkinter module. GeeksforGeeks. https://www.geeksforgeeks.org/python/weather-app-in-python-using-tkinter-module/
GeeksforGeeks. (2025c, February 25). Response.Json() python requests. GeeksforGeeks. https://www.geeksforgeeks.org/python/response-json-python-requests/
GeeksforGeeks. (2026a). Python dictionary GET() method. GeeksforGeeks. https://www.geeksforgeeks.org/python/python-dictionary-get-method/
GeeksforGeeks. (2026b). Python functions. GeeksforGeeks. https://www.geeksforgeeks.org/python/python-functions/
Matthes, E. (2023). Python Crash Course. In O’Reilly Online Learning (3rd edition). No Starch Press, New York. https://doi.org/1098156664/1200w630h
Python Documentation. (2016). 7. Input and output. Python Documentation. https://docs.python.org/3/tutorial/inputoutput.html
Shahrouz Nikseresht. (2026, February 5). Python Dictionaries Explained Simply (Keys, Values, and Access). DEV Community. https://dev.to/shahrouzlogs/python-dictionaries-explained-simply-keys-values-and-access-2g
W3School. (n.d.). Python input() function. Www.W3schools.Com. Retrieved September 11, 2026, from https://www.w3schools.com/python/ref_func_input.asp
W3Schools. (n.d.-a). Python float() function. Www.W3schools.Com. Retrieved October 1, 2026, from https://www.w3schools.com/python/ref_func_float.asp
W3Schools. (n.d.-b). Python requests get method. Www.W3schools.Com. Retrieved September 10, 2026, from https://www.w3schools.com/python/ref_requests_get.asp
WorldWeatherOnline. (n.d.). Weather API documentation | WorldWeatherOnline. WorldWeatherOnline. Retrieved October 9, 2026, from https://www.worldweatheronline.com/weather-api/api/docs/weather-icons.aspx

## Contact
josephine.browne@student.uts.edu.au
