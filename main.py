import requests

OWM_Endpoint= "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "bc652ccdd33dd01f43f161c59197514e"

weather_param = {
    "lat": -37.814,
    "lon": 144.9633,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_param)
print(response.json())

