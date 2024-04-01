import requests
from flask import Flask, render_template

app = Flask(__name__)

url = "https://dogapi.dog/api/v2/facts"

response = requests.get(url)

print(response)

data = response.json()

#print(data)

random_fact = data['data'][0]['attributes']['body']

print(random_fact)


@app.route("/")
def index():
    return render_template('index.html', random_fact = random_fact)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)