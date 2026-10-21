import requests
import smtplib
import os

api_key = os.getenv("API_KEY")
sender = os.environ.get("sender")
receiver = os.environ.get("receiver")
password = os.environ.get("password")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 30.046680,
    "lon": 72.343361,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())

print(response.status_code)

if response.status_code == 200:

    weather_data = response.json()

    will_rain = False

    # Check the next 8 forecasts (24 hours)
    weather_slice = weather_data["list"][:8]

    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        print(condition_code)

        if condition_code < 700:
            will_rain = True

    if will_rain:
        message = "Subject: Weather Alert\n\nIt's going to rain today. Bring an umbrella âک”ï¸ڈ"
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(sender, password)
            connection.sendmail(sender, receiver, message)

        print("Email sent!")

