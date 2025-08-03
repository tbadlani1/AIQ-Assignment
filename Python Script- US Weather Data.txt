import requests
import pandas as pd
import time
from urllib.parse import quote

# OpenWeather API Key
API_KEY = "b64128dc1dd5493eea4001d3165a4bb3"

US_STATES = [
    {"state": "Alabama", "capital": "Montgomery"},
    {"state": "Alaska", "capital": "Juneau"},
    {"state": "Arizona", "capital": "Phoenix"},
    {"state": "Arkansas", "capital": "Little Rock"},
    {"state": "California", "capital": "Sacramento"},
    {"state": "Colorado", "capital": "Denver"},
    {"state": "Connecticut", "capital": "Hartford"},
    {"state": "Delaware", "capital": "Dover"},
    {"state": "Florida", "capital": "Tallahassee"},
    {"state": "Georgia", "capital": "Atlanta"},
    {"state": "Hawaii", "capital": "Honolulu"},
    {"state": "Idaho", "capital": "Boise"},
    {"state": "Illinois", "capital": "Springfield"},
    {"state": "Indiana", "capital": "Indianapolis"},
    {"state": "Iowa", "capital": "Des Moines"},
    {"state": "Kansas", "capital": "Topeka"},
    {"state": "Kentucky", "capital": "Frankfort"},
    {"state": "Louisiana", "capital": "Baton Rouge"},
    {"state": "Maine", "capital": "Augusta"},
    {"state": "Maryland", "capital": "Annapolis"},
    {"state": "Massachusetts", "capital": "Boston"},
    {"state": "Michigan", "capital": "Lansing"},
    {"state": "Minnesota", "capital": "Saint Paul"},
    {"state": "Mississippi", "capital": "Jackson"},
    {"state": "Missouri", "capital": "Jefferson City"},
    {"state": "Montana", "capital": "Helena"},
    {"state": "Nebraska", "capital": "Lincoln"},
    {"state": "Nevada", "capital": "Carson City"},
    {"state": "New Hampshire", "capital": "Concord"},
    {"state": "New Jersey", "capital": "Trenton"},
    {"state": "New Mexico", "capital": "Santa Fe"},
    {"state": "New York", "capital": "Albany"},
    {"state": "North Carolina", "capital": "Raleigh"},
    {"state": "North Dakota", "capital": "Bismarck"},
    {"state": "Ohio", "capital": "Columbus"},
    {"state": "Oklahoma", "capital": "Oklahoma City"},
    {"state": "Oregon", "capital": "Salem"},
    {"state": "Pennsylvania", "capital": "Harrisburg"},
    {"state": "Rhode Island", "capital": "Providence"},
    {"state": "South Carolina", "capital": "Columbia"},
    {"state": "South Dakota", "capital": "Pierre"},
    {"state": "Tennessee", "capital": "Nashville"},
    {"state": "Texas", "capital": "Austin"},
    {"state": "Utah", "capital": "Salt Lake City"},
    {"state": "Vermont", "capital": "Montpelier"},
    {"state": "Virginia", "capital": "Richmond"},
    {"state": "Washington", "capital": "Olympia"},
    {"state": "West Virginia", "capital": "Charleston"},
    {"state": "Wisconsin", "capital": "Madison"},
    {"state": "Wyoming", "capital": "Cheyenne"}
]

def get_weather(city_name, api_key, retries=3, delay=2):
    """
    Fetch weather data for a given city using the OpenWeather API with retries.

    Args:
        city_name (str): Name of the city.
        api_key (str): OpenWeather API key.
        retries (int): Number of retry attempts.
        delay (int): Delay between retries in seconds.

    Returns:
        dict: Weather data for the city or None if failed.
    """
    city_name_encoded = quote(city_name)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_encoded},US&appid={api_key}&units=imperial"

    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)  
        except Exception as e:
            print(f"Unexpected error: {e}")
            break
    return None

def fetch_state_weather_data(states, api_key):
    """
    Fetch weather data for all states in the US.

    Args:
        states (list): List of states and their capitals.
        api_key (str): OpenWeather API key.

    Returns:
        pd.DataFrame: Weather data for all states.
    """
    weather_data = []
    for state_info in states:
        state = state_info["state"]
        capital = state_info["capital"]
        print(f"Fetching weather data for {capital}, {state}")
        data = get_weather(capital, api_key)
        if data:
            weather_data.append({
                "State": state,
                "Capital": capital,
                "Temperature (F)": data["main"]["temp"],
                "Feels Like (F)": data["main"]["feels_like"],
                "Min Temperature (F)": data["main"]["temp_min"],
                "Max Temperature (F)": data["main"]["temp_max"],
                "Pressure (hPa)": data["main"]["pressure"],
                "Humidity (%)": data["main"]["humidity"],
                "Visibility (meters)": data.get("visibility", "N/A"),
                "Weather Description": data["weather"][0]["description"],
                "Cloudiness (%)": data["clouds"]["all"],
                "Wind Speed (mph)": data["wind"]["speed"],
                "Wind Direction (degrees)": data["wind"]["deg"],
                "Latitude": data["coord"]["lat"],
                "Longitude": data["coord"]["lon"]
                
                
            })
        else:
            print(f"Failed to fetch data for {capital}, {state}")
    return pd.DataFrame(weather_data)


try:
    weather_df = fetch_state_weather_data(US_STATES, API_KEY)
    if weather_df.empty:
        print("No data was returned. Check API key or city names.")
    else:
        print(weather_df)
except Exception as e:
    print(f"An error occurred: {e}")
