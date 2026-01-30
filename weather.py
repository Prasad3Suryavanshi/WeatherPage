import requests
import json
import os

# Set your default city coordinates here
LAT = "40.71"
LON = "-74.00"

def get_weather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&timezone=auto"
    try:
        response = requests.get(url)
        data = response.json()
        
        # We save this so the website can read it instantly
        with open("weather_data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Weather data synced successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_weather()
