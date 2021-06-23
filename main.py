from twilio.rest import Client
import requests
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = os.environ.get("api_key")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

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
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Gonna rain son, bring an umbrella",
        from_={'your twilio number'},
        to={'your number'}
    )

    print(message.status)

# print(weather_data["hourly"][0]["weather"])
