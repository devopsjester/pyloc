import re
import requests
import sys

def get_location(zipcode):
    url = f"https://api.zippopotam.us/us/{zipcode}"
    response = requests.get(url)
    data = response.json()
    city = data['places'][0]['place name']
    state = data['places'][0]['state']
    return city, state

def get_weather(city, state):
    api_key = "1b123c9a91468b0da3e0a39c238b2a01"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    weather = data['weather'][0]['description']
    return weather

if len(sys.argv) < 2:
    print("Please provide a zipcode as an argument")
else:
    zipcode = sys.argv[1]
    if not re.match(r"^\d{5}(?:-\d{4})?$", zipcode):
        print("Invalid zipcode format")
    else:
        city, state = get_location(zipcode)
        weather = get_weather(city, state)
        print(f"The zipcode {zipcode} is in {city}, {state} and the weather is {weather}")

