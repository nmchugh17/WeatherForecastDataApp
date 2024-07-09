import requests

API_KEY = "ba04df4e469843fe853154302240907"


def get_data(place, forecast_days=None):
    url = f"http://api.weatherapi.com/v1/forecast.json?q={place}&key={API_KEY}&days={forecast_days}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['forecast']['forecastday']
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Dublin", forecast_days=5))
