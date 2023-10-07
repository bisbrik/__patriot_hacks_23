import requests
import json

class weather_API:
    
    def __init__(self):
        self.avg_temperature = 0
        self.avg_temperatureApparent = 0
        self.avg_humidity = 0
        self.avg_rainAccumulation = 0
        self.avg_snowAccumulation = 0
        self.avg_uvIndex = 0
        self.avg_windGust = 0
        self.avg_windSpeed = 0
        self.if_uvHealthConcern = 0
    
    def get_averages (self, zipcode):
        url = f"https://api.tomorrow.io/v4/weather/forecast?location={zipcode}&US&apikey=gidPJT2TE5dTjbryyiof53743SJp3duL"
        headers = {"accept": "application/json"}
        for i in range(8) :
            response = requests.get(url, headers=headers)
            data = response.json()
            self.avg_temperature += (data['timelines']['hourly'][i]['values']['temperature'])
            self.avg_temperatureApparent += (data['timelines']['hourly'][i]['values']['temperatureApparent'])
            self.avg_humidity += (data['timelines']['hourly'][i]['values']['humidity'])
            self.avg_rainAccumulation += (data['timelines']['hourly'][i]['values']['rainAccumulation'])
            self.avg_snowAccumulation += (data['timelines']['hourly'][i]['values']['snowAccumulation'])
            self.avg_uvIndex += (data['timelines']['hourly'][i]['values']['uvIndex'])
            self.avg_windGust += (data['timelines']['hourly'][i]['values']['windGust'])
            self.avg_windSpeed += (data['timelines']['hourly'][i]['values']['windSpeed'])
            if (data['timelines']['hourly'][i]['values']['windSpeed']) == 1:
                self.if_uvHealthConcern = 1
        self.avg_temperature /= 8
        self.avg_temperatureApparent /= 8
        self.avg_humidity /= 8
        self.avg_rainAccumulation /= 8
        self.avg_snowAccumulation /= 8
        self.avg_uvIndex /= 8
        self.avg_windGust /= 8
        self.avg_windSpeed /= 8
        
    def get_avg_temperature (self):
        return self.avg_temperature

    def get_avg_temperatureApparent (self):
        return self.avg_temperatureApparent
    
    def get_avg_humidity (self):
        return self.avg_humidity
    
    def get_avg_rainAccumulation (self):
        return self.avg_rainAccumulation
    
    def get_avg_snowAccumulation (self):
        return self.avg_snowAccumulation
    
    def get_avg_uvIndex (self):
        return self.avg_uvIndex
    
    def get_avg_windGust (self):
        return self.avg_windGust
    
    def get_avg_windSpeed (self):
        return self.avg_windSpeed
    
    def get_if_uvHealthConcern (self):
        return self.if_uvHealthConcern