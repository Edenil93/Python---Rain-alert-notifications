import requests
from twilio.rest import Client

account_sid = "Your Twilio account sid"
auth_token = "Your Twilio token"

parameters_weather = {
    "lat": 48.704575,
    "lon": 8.918906,
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": "3d4caf39c6ac6633f7539a4d54588864"
}

response_weather = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters_weather)
response_weather.raise_for_status()
weather_json = response_weather.json()

condition_code = weather_json['hourly'][0]['weather'][0]['id']

condition_codes = [condition_code for weather_json['hourly'] in weather_json['hourly'][:12]]

if condition_code in condition_codes and condition_code < 600:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella!",
        from_='Twilio phone number',
        to='Your phone number'
    )
    print(message.status)