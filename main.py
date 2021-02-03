import requests
from datetime import datetime
import smtplib
import time

MY_LAT = ["Latitude "]
MY_LONG = ["Longitude"]
MY_EMAIL = "[Your Email Address]"
PASSWORD = "[Your Email Password]"


def is_iss_overhead():
    # using requests.get to get the data from the API using API URL
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # getting the status code, 200 means successful
    response.raise_for_status()
    # saving the data in data
    data = response.json()

    # Parsing the latitude and longitude of the ISS
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    # Your position is within +5 or -5 degrees of the ISS position.
    # check if the ISS is within +5 or -5 degree within my location
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True



def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # using requests.get to get the data from the API using API URL
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    # getting the status code, 200 means successful
    response.raise_for_status()
    # saving the data in data
    data = response.json()

    # Parsing the sunrise and sunset time form the API data
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # it will return true when my current time equals to sunset time
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


#If the ISS is close to my current position
# and it is currently dark

while True:
    # run the code every 60s, by running the code every 60s
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587)as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="[Destination Email Address]",
                                msg="Subject: ISS\n\nLOOK UP!!!!"
                                )




