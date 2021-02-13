import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import geopandas
from datetime import datetime
import smtplib
import os

MY_LAT = float(53.14118)
MY_LONG = float(8.21467)
my_email = "hamburgertechpreneur@gmail.com"
password = os.environ.get('FACEBOOK_PASSWORD')

def send_notification():
    with smtplib.SMTP ("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
        from_addr=my_email,
        to_addrs=f"{row.email}",
        msg=f"Schau hoch, die ISS ist da! \n\n Es ist dunkel und die ISS ist gerade über uns!")


def ISS_over_us():
    parameters = { "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted":0 }
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise= data["results"]["sunrise"]
    sunrise_hour=int(sunrise.split("T")[1].split(":")[0])

    sunset = data["results"]["sunset"]
    sunset_hour=int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour>=sunset_hour or time_now.hour<=sunrise_hour:
        send_notification()





world = geopandas.read_file(
    geopandas.datasets.get_path('naturalearth_lowres')
)


fig, ax = plt.subplots()
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot(ax=ax)


def animate(i):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    longitude =  float(data["iss_position"]["longitude"])
    latitude =  float(data["iss_position"]["latitude"])
    if (MY_LAT-5) <= latitude <= (MY_LAT+5)  and (MY_LONG-5) <= longitude <= (MY_LONG+5):
        ISS_over_us()
    position = (longitude,latitude)
    plt.cla()
    world.plot(ax=ax)
    ax.plot(longitude,
            latitude,
            marker='o',
            c='black',
            alpha=0.5
        )

ani = animation.FuncAnimation(plt.gcf(),animate, interval=1000)


plt.show()
