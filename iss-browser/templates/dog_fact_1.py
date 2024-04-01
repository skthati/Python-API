import requests

url = "https://dogapi.dog/api/v2/facts"

response = requests.get(url)

data = response.json()

random_data_1 = data['data'][0]['attributes']['body']
print(random_data_1)

html_file = open('index.html', "w")

new_html_file = html_file.read()
print(new_html_file)

