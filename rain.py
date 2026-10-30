# list of all weather codes that represent rain, showers, snow, sleet, ice pellets, blizzard, and thunder conditions
rain_codes = [176, 179, 182, 185, 200, 230, 263, 
266, 281, 284, 293, 296, 299, 302, 305, 308,
311, 314, 317, 320, 350, 353, 356, 359, 362,
365, 368, 371, 374, 377, 386, 389, 392, 395]


# check to see if the current weather code is in rain_codes list

# code is the parameter name for the current weather code that is returned from app.py, 
# when umbrella_rec(weather_code) is run in app.py, code is assigned the value of the current numerical weather code
def umbrella_rec(code):
   code = int(code) # turn code into an integer so it can be compareed
   return code in rain_codes # this line check if the current numerical weather code (code) is in the rain_codes list
