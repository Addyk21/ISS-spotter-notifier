import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 22.3511148  # my latitude
MY_LONG = 78.6677428  # my longitude
MY_EMAIL = "samplemail@gmail.com"
MY_PASSWORD = "sample_password"


def is_iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data_iss_position = response.json()

    iss_latitude = float(data_iss_position["iss_position"]["latitude"])
    iss_longitude = float(data_iss_position["iss_position"]["longitude"])

    # checking if iss coordinates are within +-5 difference of my own coordinates
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data_time = response.json()

    sunrise = int(
        data_time["results"]["sunrise"].split("T")[1].split(":")[0])  # using split function to get only the hour
    sunset = int(data_time["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    # checking whether it's dark outside or not
    if sunset <= time_now or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_near() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: The ISS is passing over you👆🏻"
        )
