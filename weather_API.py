import requests
import json

class weather_API:
    # intializes the values
    def __init__(self):
        self.data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.avg_temperature = 0
        self.avg_temperatureApparent = 0
        self.avg_humidity = 0
        self.avg_rainAccumulation = 0
        self.avg_snowAccumulation = 0
        self.avg_uvIndex = 0
        self.avg_windGust = 0
        self.avg_windSpeed = 0
        self.if_uvHealthConcern = 0
    # gets the averages of the parameters from an 8 hour period given a zipcode
    def get_averages (self, zipcode):
        url = f"https://api.tomorrow.io/v4/weather/forecast?location={zipcode}&US&apikey=o2Vfm23Ix9MavCUeV9xra39aFb9Z3Yul"
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
        self.data_list[0] = self.avg_temperature
        self.data_list[1] = self.avg_temperatureApparent
        self.data_list[2] = self.avg_humidity
        self.data_list[3] = self.avg_rainAccumulation
        self.data_list[4] = self.avg_snowAccumulation
        self.data_list[5] = self.avg_uvIndex
        self.data_list[6] = self.avg_windGust
        self.data_list[7] = self.avg_windSpeed
        self.data_list[8] = self.if_uvHealthConcern
        
    def get_data_list (self):
        return self.data_list
