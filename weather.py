import requests

api_key = "807f16b779080d21dc3f7b3f68797237"

def get_weather(city_name):
    # Define the base URL for the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Define the parameters to send with the GET request
    params = {
        "q": city_name,  # City name
        "appid": api_key,  # Your API key
        "units": "metric",  # Optional: temperature in Celsius
    }
    
    # Send GET request to the API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the response data to JSON format
        data = response.json()
        
        # Extract relevant information
        city = data["name"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        
        # Print the weather data
        return (f"Weather in {city}: {temperature}°C, {weather}")
        
    else:
        return(f"Failed to get weather data: {response.status_code}")

# city_name = "London"
# get_weather(city_name, api_key)