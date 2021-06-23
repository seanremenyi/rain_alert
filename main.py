import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "bc652ccdd33dd01f43f161c59197514e"

weather_param = {
    "lat": -37.814,
    "lon": 144.9633,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_param)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain == True:
    print("Bring an umbrella")

# print(weather_data["hourly"][0]["weather"])
