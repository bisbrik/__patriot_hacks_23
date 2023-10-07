import json

global avgTemp
global avgApparentTemp
global avgHumidity
global avgRainAccumulation
global avgSnowAccumulation
global uvIndex
global uvHealthConcern
global windGusts
global windSpeed

test_dict = {}

clothing = {'top': ''; 'bottom': ''; 'windbreaker': False; 'sun_protection': False; 'umbrella': False; 'snow_gear': False}

def getAppropriateClothing():
    if (avgTemp >= 25):
        clothing['top'] = 'short_sleeve'
        clothing['bottom'] = 'long_sleeve'
    elif (avgTemp >= 15):
        clothing.append('short sleeves')
        clothing.append('long pants')
    else:
        clothing.append('long sleeves')
        clothing.append('long pants')
    if (uvHealthConcern)
