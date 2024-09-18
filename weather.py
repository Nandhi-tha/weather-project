import requests
from dotenv import load_dotenv
import os
#from pprint import pprint

load_dotenv()

def current_weather():
    print("\n")
    print("****************************************")
    print("*    Get currrent weather conditions   *")
    print("****************************************")
    city = input("\n Enter a city name:\n")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    #print(request_url)

    response = requests.get(request_url)
    weather_data = response.json()
    #pprint(weather_data)

    print(f'\n Current weather for {weather_data["name"]}:')
    print(f'\n The temperature is {weather_data["main"]["temp"]:.1f}°')
    print(f'\n {weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')
    

if __name__ == "__main__":
    current_weather()