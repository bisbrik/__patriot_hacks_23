import requests
import json

zipcode = input("enter zipcode: ")
url = f"https://api.tomorrow.io/v4/weather/forecast?location={zipcode}&US&apikey=gidPJT2TE5dTjbryyiof53743SJp3duL"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()


print(data['timelines']['hourly'][0])


def avg_temperature () :
    output = 0
    for i in range(8) :
        output = output + (data['timelines']['hourly'][i]['values']['temperature'])
    output = output / 8
    return output

def avg_temperatureApparent () :
    output = 0
    for i in range(8) :
        output = output + (data['timelines']['hourly'][i]['values']['temperatureApparent'])
    output = output / 8
    return output
    
def avg_humidity () :
    output = 0
    for i in range(8) :
        output = output + (data['timelines']['hourly'][i]['values']['humidity'])
    output = output / 8
    return output

def avg_rainAccumulation () :
    output = 0
    for i in range(8) :
        output = output + (data['timelines']['hourly'][i]['values']['rainAccumulation'])
    output = output / 8
    return output
    
def avg_snowAccumulation () :
    output = 0
    for i in range(8) :
        output = output + (data['timelines']['hourly'][i]['values']['snowAccumulation'])
    output = output / 8
    return output
    
def avg_uvIndex () :
    output = 0
    for i in range(8) :
        output = output + (data['timelines']['hourly'][i]['values']['uvIndex'])
    output = output / 8
    return output
    
def avg_windGust () :
    output = 0
    for i in range(8) :
        output = output + (data['timelines']['hourly'][i]['values']['windGust'])
    output = output / 8
    return output
    
def avg_windSpeed () : 
    output = 0
    for i in range(8) :
        output = output + (data['timelines']['hourly'][i]['values']['windSpeed'])
    output = output / 8
    return output

def if_uvHealhConcern () :
    output = 0
    for i in range(8) :
        if (data['timelines']['hourly'][i]['values']['windSpeed']) == 1 :
            output = 1
    return output