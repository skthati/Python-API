import requests
import webbrowser

url = "https://dogapi.dog/api/v2/facts"

response = requests.get(url)

data = response.json()

random_data_1 = data['data'][0]['attributes']['body']
#print(random_data_1)

#html_file = open('index.html', "r")
#print(html_file)
#new_html_file = html_file.read()
#print(new_html_file)

with open('index.html', 'r') as file:
    #data1 = file.read().rstrip()
    data1 = file.read().replace("*random_fact*", random_data_1)

print(data1)

webbrowser.open_new_tab('index.html')

