import requests

API_KEY = "ba04df4e469843fe853154302240907"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.weatherapi.com/v1/forecast.json?q={place}&key={API_KEY}&days={forecast_days}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['forecast']['forecastday']

    if kind == "Temperature":
        filtered_data = [dict["day"]["avgtemp_c"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["day"]["condition"]["text"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Sky"))
