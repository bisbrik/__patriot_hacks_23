class weather_clothing:
    #field variables for determining values in dictionary; meant to be used throughout program
    #all values are in metric
    #float values
    def __init__(self, avgTemp, avgApparentTemp, avgHumidity, avgRainAccumulation, avgSnowAccumulation, uvIndex, avgWindSpeed, uvHealthConcern):
        self.avgTemp = avgTemp
        self.avgApparentTemp = avgApparentTemp
        self.avgHumidity = avgHumidity
        self.avgRainAccumulation = avgRainAccumulation
        self.avgSnowAccumulation = avgSnowAccumulation
        self.uvIndex = uvIndex
        self.avgWindSpeed = avgWindSpeed
        #bool value
        self.uvHealthConcern = uvHealthConcern
        #determines what clothing to wear for user
        #            long sleeve or shorts    dependent on windSpeed    uvHealthConcern     avgRainAccumulation avgSnowAccumulation
        self.clothing = { 'top': '', 'bottom': '', 'windbreaker': False, 'sun_protection': False, 'umbrella': False, 'snow_gear': False }
    
    def get_avg_temp(self):
        return self.avgTemp
    
    def get_avg_apparent_temp(self):
        return self.avgApparentTemp
    
    def get_avg_humidity(self):
        return self.avgHumidity
    
    def get_avg_rain_accumulation(self):
        return self.avgRainAccumulation
    
    def get_avg_snow_accumulation(self):
        return self.avgSnowAccumulation
    
    def get_uv_index(self):
        return self.uvIndex
    
    def get_avg_wind_speed(self):
        return self.avgWindSpeed
    
    def get_uv_health_concern(self):
        return self.uvHealthConcern
    
    #determines values in dictioanary
    def get_clothing(self):
        #avgTemp based on degrees C
        #Hot weather
        if (self.avgTemp >= 25):
            self.clothing['top'] = 'short_sleeve'
            self.clothing['bottom'] = 'long_sleeve'
        #cool weather
        elif (self.avgTemp >= 15):
            self.clothing['top'] = 'short_sleeve'
            self.clothing['bottom'] = 'long_sleeve'
        # <= 10 degrees C, generally cold
        else:
            self.clothing['top'] = 'short_sleeve'
            self.clothing['bottom'] = 'long_sleeve'
        
        # uvHealthConcern is truthy or falsy int (0 or 1 in json)
        if (self.uvHealthConcern):
            self.clothing['sun_protection'] = True

        #Strong breeze
        if (self.avgWindSpeed >= 12):
            self.clothing['windbreaker'] = True

        #0.1mm currently being used as placeholder
        if (self.avgRainAccumulation > 0.1):
            self.clothing['umbrella'] = True
        if (self.avgSnowAccumulation > 0.1):
            self.clothing['snow_gear'] = True

        return self.clothing


