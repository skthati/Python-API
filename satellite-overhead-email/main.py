import requests
import datetime as dt

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
print(now)

if float(iss_lat)-5 < MY_LAT < float(iss_lat) +5 and float(iss_lng)-5 < MY_LNG < float(iss_lng)+5:
    pass