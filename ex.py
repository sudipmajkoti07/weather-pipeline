import requests
import datetime as dt
import pandas as pd


url='https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=c4122119fa5241657e38321c4283919d'

#this is the function to convert the kelvin value to celsius and fahrenheit
def convert(kvalue):
    Celsius=kvalue-273.15
    Fahrenheit=((Celsius-273.15))*(9/5) +32
    return (round(Celsius,2),round(Fahrenheit,2))

cell=[]
fahren=[]
humid=[]
dis=[]
sunrise=[]
sunset=[]
wind=[]


#extraction part is here
response=requests.get(url).json()
tem_kelvin=response['main']['temp']
cel,fah=convert(tem_kelvin)
humidity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise_time=dt.date.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time=dt.date.fromtimestamp(response['sys']['sunset'] + response['timezone'])
'''we add the time zone to sunrise to get
the local time of london'''
windspeed=response['wind']['speed']


#adding the extracted data into list 
cell.append(cel)
fahren.append(fah)
humid.append(humidity)
dis.append(description)
sunrise.append(sunrise_time)
sunset.append(sunset_time)
wind.append(windspeed)


data = {'celsius': cell, 
        'fahrenheit': fahren, 'humidity': humid, 
        'discription': dis,'sunrisetime':sunrise,
        'sunsettime':sunset,'windspeed':wind}

df=pd.DataFrame(data=data)
df.to_csv('hi.csv') 






