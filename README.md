# Python-API
 
<a name="readme-top"></a>


<div align="center">
<!-- Title: -->
<h1><a href="https://github.com/skthati/Python-API">Python</a> - API Basics </h1>
</div>

<!-- Table of contents -->
<hr>
<hr>
<ol>
    <li><a href="#python-api-basics">Python API Basics</a></li>
    <li><a href="#kanye-quote">Kanye Quote</a></li>
    <li><a href="#bloopers">Bloopers</a></li>
</ol>
<hr>
<hr>


## Kanye Quotes <a name="kanye-quote"></a>
Simple API pulls a quote from URL api.kanye.rest and displays the quote in local TKinter window. Everytime the button is clicked, Quote will be refreshed.

![Alt text](kanye/kanye-quotes.gif)

[Code file main.py](kanye/main.py)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  

# Python API Basics
 Below is basic code to request an API. 
--> To find the position of the ISS- Satellite.

```Python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# To catch any exceptions
response.raise_for_status()

data = response.json()

print(response) #Prints the response. In this case [200]

print(data)
```

`response.json()["iss_position"]` narrows down the data.

```Python
print(f"Right now ISS position is: Latitude - {data['iss_position']['latitude']} and Longitude - {data['iss_position']['longitude']}.")
```
Above code narrows down more data.

### Pass the ISS-position data a website.

To graphically locate the position of the satellite we can use the website latlong.net and below code can generate the link which can be opened in browser.

```Python
# Prints the link to console.
print(f"https://www.latlong.net/c/?lat={data['iss_position']['latitude']}&long={data['iss_position']['longitude']}")

```

```Python
# Opens default brower with the URL

import webbrowser
webbrowser.open(f"https://www.latlong.net/c/?lat={data['iss_position']['latitude']}&long={data['iss_position']['longitude']}")
```

## API to API <a name="api-to-api"></a>
Get data from one API and pass the data to Another API.

Here is a simple application which get the latitude and Longitude of IIS Satellite from api.open-notify.org and pass that data to api.sunrise-sunset.org to find the sunrise and sunset times at that location.

```Python
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
    "lng": iss_lon
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

data = response.json()

print(data)

```



<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  





 
