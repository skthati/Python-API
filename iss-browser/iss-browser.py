import requests
import webbrowser

url = "http://api.open-notify.org/iss-now.json"
reverse_location = "https://www.latlong.net/c/?lat=0.000000&long=0.000000"
sunraise_sunset = "https://api.sunrise-sunset.org/json"
response = requests.get(url)
data = response.json()
print(response)
print(data)

iss_latitude = data['iss_position']['latitude']
iss_longitude = data['iss_position']['longitude']
print(iss_latitude)
print(iss_longitude)

parameters = {
   "lat": iss_latitude,
   "lng": iss_longitude 
}

sun_response = requests.get(sunraise_sunset, params=parameters)
print(sun_response)

sun_data = sun_response.json()
print(sun_data)

sun_raise_time = sun_data['results']['sunrise']
print(sun_raise_time)

iss_position_now = f"https://www.latlong.net/c/?lat={iss_latitude}&long={iss_longitude}"
print(iss_position_now)
print(reverse_location)

webbrowser.open_new_tab(iss_position_now)