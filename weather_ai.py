import requests

city=input("enter your city name")
url=f"https://wttr.in/{city}?format%t%20%w"

def get_weather(city):
    response=requests.get(url)
    try:
        print(f"the weather of {city} is:{response.text}")
    except:
        print("I couldn't find")

get_weather(city)