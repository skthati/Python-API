import requests
import datetime as dt
import smtplib

# ---------- Send email -----------#
my_email = "pythonmail@sloka.co.nz"
my_password = "Today@123"
to_email = "nsd1026@gmail.com"

def send_email():
    with smtplib.SMTP_PORT("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)

        connection.sendmail(
            from_addr=my_email, 
            to_addrs=to_email, 
            msg="Subject: ISS Satellite in the sky!! 1\n\nSatellite is above Auckland, Go and look outside."
        )



# ------------- My city location ------------#
MY_LAT = -36.848461
MY_LNG = 174.763336


# ---------- ISS POSITION -----------#
iss_data = requests.get("http://api.open-notify.org/iss-now.json")

iss_data = iss_data.json()

iss_lat = iss_data['iss_position']['latitude']
iss_lng = iss_data['iss_position']['longitude']

# ------- Sunrise and Sunset times at my location -----#
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
sunrise_sunset_data = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

sunrise_sunset_data = sunrise_sunset_data.json()

sunrise = sunrise_sunset_data['results']['sunrise']
sunrise = sunrise.split('T')[1].split(':')[0]

sunset = sunrise_sunset_data['results']['sunset']
sunset = sunset.split('T')[1].split(':')[0]

# Time at my location.

now = dt.datetime.now()
current_hour = now.hour

if float(iss_lat)-5 < MY_LAT < float(iss_lat) +5 and float(iss_lng)-5 < MY_LNG < float(iss_lng)+5:
    if 0 <= current_hour <= int(sunset) or int(sunrise) <= current_hour <= 24:
        send_email()