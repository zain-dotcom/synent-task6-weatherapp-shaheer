"""
Synent Technologies - Python Development Internship
Task 6: Weather App (API Integration)
Author: [Your Full Name]
"""

import sys
import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city_name):
    """
    Fetch current weather metrics for a specified city using OpenWeatherMap API.
    Handles network errors, invalid cities, and authorization problems.
    """
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Metric returns Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        # Check HTTP response codes
        if response.status_code == 404:
            print(f"\n[Error] City '{city_name}' not found. Please verify spelling.")
            return
        elif response.status_code == 401:
            print("\n[Error] Invalid API key. Please check your OpenWeatherMap configuration.")
            return
        
        response.raise_for_status()
        data = response.json()

        # Parse required fields
        city = data.get("name", "Unknown")
        country = data.get("sys", {}).get("country", "")
        temp = data.get("main", {}).get("temp", "N/A")
        feels_like = data.get("main", {}).get("feels_like", "N/A")
        humidity = data.get("main", {}).get("humidity", "N/A")
        description = data.get("weather", [{}])[0].get("description", "N/A").title()
        wind_speed = data.get("wind", {}).get("speed", "N/A")

        # Display structured output
        print("\n" + "=" * 42)
        print(f" Weather Report: {city}, {country}")
        print("=" * 42)
        print(f" Condition   : {description}")
        print(f" Temperature : {temp}°C (Feels like {feels_like}°C)")
        print(f" Humidity    : {humidity}%")
        print(f" Wind Speed  : {wind_speed} m/s")
        print("=" * 42)

    except requests.exceptions.Timeout:
        print("\n[Error] Connection timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("\n[Error] Network error. Check your internet connection.")
    except requests.exceptions.RequestException as err:
        print(f"\n[Error] Unexpected API request error: {err}")


def main():
    if API_KEY == "ca841235986709a633912c272ea73fdd" or not API_KEY.strip():
        print("[Error] Please set your OpenWeatherMap API key in main.py before running.")
        sys.exit(1)

    print("========================================")
    print("    LIVE WEATHER APPLICATION (CLI)     ")
    print("========================================")

    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == "exit":
            print("\nThank you for using Weather App. Goodbye!\n")
            break
        
        if not city:
            print("[Warning] City name cannot be empty.")
            continue
            
        fetch_weather(city)


if __name__ == "__main__":
    main()