
#import modules
import hacks_weather as hw


#global variables for determining values in dictionary; meant to be used throughout program
#all values are in metric
#float values
global avgTemp
global avgApparentTemp
global avgHumidity
global avgRainAccumulation
global avgSnowAccumulation
global uvIndex
global avgWindSpeed
#bool value
global uvHealthConcern

#determines what clothing to wear for user
#            long sleeve or shorts    dependent on windSpeed    uvHealthConcern     avgRainAccumulation avgSnowAccumulation
clothing = { 'top': '', 'bottom': '', 'windbreaker': False, 'sun_protection': False, 'umbrella': False, 'snow_gear': False }


#determines values in dictioanary
def getAppropriateClothing():
    #avgTemp based on degrees C
    #Hot weather
    if (avgTemp >= 25):
        clothing['top'] = 'short_sleeve'
        clothing['bottom'] = 'long_sleeve'
    #cool weather
    elif (avgTemp >= 15):
        clothing['top'] = 'short_sleeve'
        clothing['bottom'] = 'long_sleeve'
    # <= 10 degrees C, generally cold
    else:
        clothing['top'] = 'short_sleeve'
        clothing['bottom'] = 'long_sleeve'
    
    # uvHealthConcern is truthy or falsy int (0 or 1 in json)
    if (uvHealthConcern):
        clothing['sun_protection'] = True

    #Strong breeze
    if (avgWindSpeed >= 12):
        clothing['windbreaker'] = True

    #0.1 currently being used as placeholder
    if (avgRainAccumulation > 0.1):
        clothing['umbrella'] = True
    if (avgSnowAccumulation > 0.1):
        clothing['snow_gear'] = True
