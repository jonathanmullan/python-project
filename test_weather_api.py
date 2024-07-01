import requests
import pytest

API_KEY = "2a553cd932a744cead374cf2a0c24174"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "Belfast"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY


# response = requests.get(url).json()


def get_weather_data(CITY):
    params = {
        'q': CITY,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()


def test_weather_data():
    data = get_weather_data(CITY)

    assert "temp_min" in data["main"], "Minimum temperature not found in response"
    assert "temp_max" in data["main"], "Maximum temperature not found in response"
    assert "humidity" in data["main"], "Humidity not found in response"

    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    humidity = data["main"]["humidity"]

    print("\n\n----------\n")
    print(f"Minimum Temperature: {temp_min}°C")
    print(f"Maximum Temperature: {temp_max}°C")
    print(f"Humidity: {humidity}%")
    print("\n----------\n\n")


if __name__ == "__main__":
    pytest.main()
