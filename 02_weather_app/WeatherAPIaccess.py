import requests

def get_weather_data(city, api_key):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.

    Parameters:
    city (str): The name of the city to fetch weather data for.
    api_key (str): Your OpenWeatherMap API key.

    Returns:
    dict: A dictionary containing weather data if the request is successful.
    None: If the request fails.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    data = get_weather_data(city, api_key)
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        return {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None