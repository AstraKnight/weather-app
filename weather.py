import requests
from dotenv import load_dotenv
import os
from pprint import pprint  # make json easier to read

load_dotenv()

def get_current_weather(city="New York"):
     
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data = requests.get(request_url).json()
    
    return weather_data



# when the file is called directly
if __name__ == "__main__":
    print(f'\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")

    # check for empty strings or strings with only spaces:
    if not bool(city.strip()):
        city = "New York"  # default value

    weather_data = get_current_weather(city)
    
    print("\n")
    pprint(weather_data)