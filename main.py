import requests

import webbrowser

response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()

print(response)

print(data)

position = data['iss_position']

print(position['latitude'])

print(f"Right now ISS position is: Latitude - {data['iss_position']['latitude']} and Longitude - {data['iss_position']['longitude']}.")

print(f"https://www.latlong.net/c/?lat={data['iss_position']['latitude']}&long={data['iss_position']['longitude']}")

webbrowser.open(f"https://www.latlong.net/c/?lat={data['iss_position']['latitude']}&long={data['iss_position']['longitude']}")