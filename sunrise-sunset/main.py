import requests

iss_response = requests.get("http://api.open-notify.org/iss-now.json")

location_data = iss_response.json()

print(location_data)

iss_lat = location_data['iss_position']['latitude']
iss_lon = location_data['iss_position']['longitude']

# print(iss_lat)
# print(iss_lon)

parameters = {
    "lat": iss_lat,
    "lng": iss_lon,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

data = response.json()

sunrise = data['results']['sunrise']
print(sunrise)
sunrise = sunrise.split('T')[1].split('+')[0]
print(sunrise)

sunset = data['results']['sunset']
sunset = sunset.split('T')[1].split('+')[0]
print(sunset)