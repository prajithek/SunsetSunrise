import requests
from geopy.geocoders import Nominatim
from pytz import timezone
from dateutil import parser
format = "%H:%M:%S"


#Getting city name from user
city = input("Enter City Name :")
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode(city)
print(getLoc.address)
Latitude = getLoc.latitude
Longitude = getLoc.longitude


#Parameters for API requests
parameters = {"lat" : Latitude,"lng" : Longitude,"formatted" : 0,}


#Using sunrise-Sunset API

responce = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
data = responce.json()

print(data)
#Parsing responce Time
sunrise = parser.parse(responce.json()["results"]["sunrise"])
sunset = parser.parse(responce.json()["results"]["sunset"])

#Convert to Asia/kolkata Time Zone
sunrise = sunrise.astimezone(timezone('Asia/kolkata')).strftime(format)
sunset = sunset.astimezone(timezone('Asia/Kolkata')).strftime(format)


print("Sunrise Time :",sunrise)
print("Sunset TIme :",sunset)
