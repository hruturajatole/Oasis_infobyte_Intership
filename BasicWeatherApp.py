import requests
import json

# Function to get weather data from API
def get_weather(city=None, lat=None, lon=None):
    WeatherAppAPIKey = "150a697994141d05857145c68b95ac7c"  # Replace with your actual API key
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    
    if city:
        complete_url = f"{base_url}q={city}&appid={WeatherAppAPIKey}&units=metric"
    elif lat and lon:
        complete_url = f"{base_url}lat={lat}&lon={lon}&appid={WeatherAppAPIKey}&units=metric"
    else:
        print("Please provide either a city name or latitude and longitude.")
        return

    response = requests.get(complete_url)
    data = response.json()

    print("API Response:", data)  # Print full response for debugging

    if data["cod"] == 200:
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temperature = main['temp']
        humidity = main['humidity']

        print(f"Weather in {city or f'coordinates ({lat}, {lon})'}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_desc.capitalize()}")
    else:
        print("City or location not found, please check the input and try again.")

# Main function to handle user input
def main():
    choice = input("Do you want to enter a city name or coordinates? (city/coords): ").strip().lower()
    
    if choice == 'city':
        city = input("Enter city name (e.g., London or Paris,FR): ")
        get_weather(city=city)
    elif choice == 'coords':
        lat = input("Enter latitude: ")
        lon = input("Enter longitude: ")
        get_weather(lat=lat, lon=lon)
    else:
        print("Invalid choice. Please enter 'city' or 'coords'.")

if __name__ == "__main__":
    main()
