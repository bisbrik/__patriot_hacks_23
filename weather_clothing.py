class weather_clothing:
    #field variables for determining values in dictionary; meant to be used throughout program
    #all values are in metric
  
    def __init__(self, data_list):
        #float values
        self.avgTemp = data_list[0]
        self.avgApparentTemp = data_list[1]
        self.avgHumidity = data_list[2]
        self.avgRainAccumulation = data_list[3]
        self.avgSnowAccumulation = data_list[4]
        self.uvIndex = data_list[5]
        #float value
        self.avgWindGust = data_list[6]
        self.avgWindSpeed = data_list[7]
        self.uvHealthConcern = data_list[8]
        
        #determines what clothing to wear for user
        #            long sleeve or shorts    dependent on windSpeed    uvHealthConcern     avgRainAccumulation avgSnowAccumulation
        self.clothing = { 'top': '', 'bottom': '', 'windbreaker': False, 'sun_protection': False, 'umbrella': False, 'snow_gear': False }
    
    def __str__(self):
        return self.clothing
    
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
    
    def get_avg_wind_gust(self):
        return self.avgWindGust
    
    def get_if_uv_health_concern(self):
        return self.uvHealthConcern
    
    #determines values in dictioanary
    def get_clothing(self):
        #avgTemp based on degrees C
        #Hot weather
        if (self.avgTemp >= 25):
            self.clothing['top'] = 'short_sleeve'
            self.clothing['bottom'] = 'short_sleeve'
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
        if (self.avgWindSpeed >= 12 or self.avgWindGust >= 7):
            self.clothing['windbreaker'] = True

        #0.1mm currently being used as placeholder
        if (self.avgRainAccumulation > 0.1):
            self.clothing['umbrella'] = True
        if (self.avgSnowAccumulation > 0.1):
            self.clothing['snow_gear'] = True

        return self.clothing
    
'''
#test driver
def main():
    #all units in metric
    temp = 20.0
    apparent_temp = 21.0
    humidity = 80.2
    rainfall = 22.0
    snowfall = 0
    uv = 1
    uv_problem = 0
    wind_speed = 13
    wind_gusts = 8
    clothes = weather_clothing(temp, apparent_temp, humidity, rainfall, snowfall, uv, uv_problem, wind_speed, wind_gusts)

    print(clothes.get_clothing())

if __name__ == "__main__":
    main()
'''